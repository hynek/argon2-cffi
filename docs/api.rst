API Reference
=============

.. module:: argon2

*argon2-cffi* comes with an high-level API and uses the officially recommended low-memory Argon2 parameters that result in a verification time of 40--50ms on recent-ish hardware.

.. warning::

   The current memory requirement is set to rather conservative 64 MB.
   However, in memory constrained environments such as Docker containers that can lead to problems.
   One possible non-obvious symptom are apparent freezes that are caused by swapping.

   Please check :doc:`parameters` for more details.

Unless you have any special needs, all you need to know is:

.. doctest::

  >>> from argon2 import PasswordHasher
  >>> ph = PasswordHasher()
  >>> hash = ph.hash("correct horse battery staple")
  >>> hash  # doctest: +SKIP
  '$argon2id$v=19$m=65536,t=3,p=4$MIIRqgvgQbgj220jfp0MPA$YfwJSVjtjSU0zzV/P3S9nnQ/USre2wvJMjfCIjrTQbg'
  >>> ph.verify(hash, "correct horse battery staple")
  True
  >>> ph.check_needs_rehash(hash)
  False
  >>> ph.verify(hash, "Tr0ub4dor&3")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerifyMismatchError: The password does not match the supplied hash


A login function could thus look like this:

.. literalinclude:: login_example.py
   :language: python

----

While the :class:`PasswordHasher` class has the aspiration to be good to use out of the box, it has all the parametrization you'll need:

.. autoclass:: PasswordHasher
  :members: from_parameters, hash, verify, check_needs_rehash

If you don't specify any parameters, the following constants are used:

.. data:: DEFAULT_RANDOM_SALT_LENGTH
.. data:: DEFAULT_HASH_LENGTH
.. data:: DEFAULT_TIME_COST
.. data:: DEFAULT_MEMORY_COST
.. data:: DEFAULT_PARALLELISM

They are taken from :data:`argon2.profiles.RFC_9106_LOW_MEMORY`.


Profiles
--------

.. automodule:: argon2.profiles


You can try them out using the :doc:`cli` interface.
For example:

.. code-block:: console

   $ python -m argon2 --profile RFC_9106_HIGH_MEMORY
   Running Argon2id 100 times with:
   hash_len: 32 bytes
   memory_cost: 2097152 KiB
   parallelism: 4 threads
   time_cost: 1 iterations

   Measuring...

   866.5ms per password verification

That should give you a feeling on how they perform in *your* environment.

.. data:: RFC_9106_HIGH_MEMORY

   Called "FIRST RECOMMENDED option" by `RFC 9106`_.

   Requires beefy 2 GiB, so be careful in memory-contrained systems.

   .. versionadded:: 21.2.0

.. data:: RFC_9106_LOW_MEMORY

   Called "SECOND RECOMMENDED option" by `RFC 9106`_.

   The main difference is that it only takes 64 MiB of RAM.

   The values from this profile are the default parameters used by :class:`argon2.PasswordHasher`.

   .. versionadded:: 21.2.0

.. data:: PRE_21_2

   The default values that *argon2-cffi* used from 18.2.0 until 21.2.0.

   Needs 100 MiB of RAM.

   .. versionadded:: 21.2.0

.. data:: CHEAPEST

   This is the cheapest-possible profile.

   .. warning::

      This is only for testing purposes!
      Do **not** use in production!

   .. versionadded:: 21.2.0


.. _`RFC 9106`: https://www.rfc-editor.org/rfc/rfc9106.html


Exceptions
----------

.. autoexception:: argon2.exceptions.VerificationError

.. autoexception:: argon2.exceptions.VerifyMismatchError

.. autoexception:: argon2.exceptions.HashingError

.. autoexception:: argon2.exceptions.InvalidHashError

.. autoexception:: argon2.exceptions.InvalidHash


Utilities
---------

.. autofunction:: argon2.extract_parameters

.. autoclass:: argon2.Parameters


Low Level
---------

.. automodule:: argon2.low_level

.. autoclass:: Type
  :members: D, I, ID

.. autodata:: ARGON2_VERSION

.. autofunction:: hash_secret

.. doctest::

  >>> import argon2
  >>> argon2.low_level.hash_secret(
  ...     b"secret", b"somesalt",
  ...     time_cost=1, memory_cost=8, parallelism=1, hash_len=64, type=argon2.low_level.Type.D
  ... )
  b'$argon2d$v=19$m=8,t=1,p=1$c29tZXNhbHQ$ba2qC75j0+JAunZZ/L0hZdQgCv+tOieBuKKXSrQiWm7nlkRcK+YqWr0i0m0WABJKelU8qHJp0SZzH0b1Z+ITvQ'


.. autofunction:: verify_secret


The raw hash can also be computed:

.. autofunction:: hash_secret_raw

.. doctest::

  >>> argon2.low_level.hash_secret_raw(
  ...     b"secret", b"somesalt",
  ...     time_cost=1, memory_cost=8, parallelism=1, hash_len=8, type=argon2.low_level.Type.D
  ... )
  b'\xe4n\xf5\xc8|\xa3>\x1d'

The super low-level ``argon2_core()`` function is exposed too if you need access to very specific options:

.. autofunction:: core

In order to use :func:`core`, you need access to *argon2-cffi*'s FFI objects.
Therefore it is OK to use ``argon2.low_level.ffi`` and ``argon2.low_level.lib`` when working with it:

.. doctest::

  >>> from argon2.low_level import ARGON2_VERSION, Type, core, ffi, lib
  >>> pwd = b"secret"
  >>> salt = b"12345678"
  >>> hash_len = 8
  >>> # Make sure you keep FFI objects alive until *after* the core call!
  >>> cout = ffi.new("uint8_t[]", hash_len)
  >>> cpwd = ffi.new("uint8_t[]", pwd)
  >>> csalt = ffi.new("uint8_t[]", salt)
  >>> ctx = ffi.new(
  ...     "argon2_context *", dict(
  ...         version=ARGON2_VERSION,
  ...         out=cout, outlen=hash_len,
  ...         pwd=cpwd, pwdlen=len(pwd),
  ...         salt=csalt, saltlen=len(salt),
  ...         secret=ffi.NULL, secretlen=0,
  ...         ad=ffi.NULL, adlen=0,
  ...         t_cost=1,
  ...         m_cost=8,
  ...         lanes=1, threads=1,
  ...         allocate_cbk=ffi.NULL, free_cbk=ffi.NULL,
  ...         flags=lib.ARGON2_DEFAULT_FLAGS,
  ...     )
  ... )
  >>> ctx
  <cdata 'struct Argon2_Context *' owning 120 bytes>
  >>> core(ctx, Type.D.value)
  0
  >>> out = bytes(ffi.buffer(ctx.out, ctx.outlen))
  >>> out
  b'\xb4\xe2HjO\x14d\x9b'
  >>> out == argon2.low_level.hash_secret_raw(pwd, salt, 1, 8, 1, 8, Type.D)
  True

All constants and types on ``argon2.low_level.lib`` are guaranteed to stay as long they are not altered by Argon2 itself.

.. autofunction:: error_to_str


Deprecated APIs
---------------

These APIs are from the first release of *argon2-cffi* and proved to live in an unfortunate mid-level.
On one hand they have defaults and check parameters but on the other hand they only consume byte strings.

Therefore the decision has been made to replace them by a high-level (:class:`argon2.PasswordHasher`) and a low-level (:mod:`argon2.low_level`) solution.
There are no immediate plans to remove them though.

.. autofunction:: argon2.hash_password
.. autofunction:: argon2.hash_password_raw
.. autofunction:: argon2.verify_password
