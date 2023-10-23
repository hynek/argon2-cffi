API Reference
=============

.. module:: argon2

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

.. autoclass:: Type()

   .. attribute:: D

      Argon2\ **d** is faster and uses data-depending memory access.
      That makes it less suitable for hashing secrets and more suitable for cryptocurrencies and applications with no threats from side-channel timing attacks.

   .. attribute:: I

      Argon2\ **i** uses data-independent memory access.
      Argon2i is slower as it makes more passes over the memory to protect from tradeoff attacks.

   .. attribute:: ID

      Argon2\ **id** is a hybrid of Argon2i and Argon2d, using a combination of data-depending and data-independent memory accesses, which gives some of Argon2i's resistance to side-channel cache timing attacks and much of Argon2d's resistance to GPU cracking attacks.

      .. versionadded:: 16.3.0

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
Therefore, it is OK to use ``argon2.low_level.ffi`` and ``argon2.low_level.lib`` when working with it.
For example, if you wanted to check the :rfc:`9106` test vectors for Argon2id that include a secret and associated data that both get mixed into the hash and aren't exposed by the high-level APIs:

.. doctest::

  >>> from argon2.low_level import Type, core, ffi, lib

  >>> def low_level_hash(password, associated, salt, secret, hash_len, version):
  ...     cout = ffi.new("uint8_t[]", hash_len)
  ...     cpwd = ffi.new("uint8_t[]", password)
  ...     cad = ffi.new("uint8_t[]", associated)
  ...     csalt = ffi.new("uint8_t[]", salt)
  ...     csecret = ffi.new("uint8_t[]", secret)
  ...
  ...     ctx = ffi.new(
  ...         "argon2_context *",
  ...         {
  ...             "out": cout,
  ...             "outlen": hash_len,
  ...             "version": version,
  ...             "pwd": cpwd,
  ...             "pwdlen": len(cpwd) - 1,
  ...             "salt": csalt,
  ...             "saltlen": len(csalt) - 1,
  ...             "secret": csecret,
  ...             "secretlen": len(csecret) - 1,
  ...             "ad": cad,
  ...             "adlen": len(cad) - 1,
  ...             "t_cost": 3,
  ...             "m_cost": 32,
  ...             "lanes": 4,
  ...             "threads": 4,
  ...             "allocate_cbk": ffi.NULL,
  ...             "free_cbk": ffi.NULL,
  ...             "flags": lib.ARGON2_DEFAULT_FLAGS,
  ...         },
  ...     )
  ...
  ...     assert lib.ARGON2_OK == core(ctx, Type.ID.value)
  ...
  ...     return bytes(ffi.buffer(ctx.out, ctx.outlen)).hex()

  >>> password = bytes.fromhex(
  ...    "0101010101010101010101010101010101010101010101010101010101010101"
  ... )
  >>> associated = bytes.fromhex("040404040404040404040404")
  >>> salt = bytes.fromhex("02020202020202020202020202020202")
  >>> secret = bytes.fromhex("0303030303030303")

  >>> assert (
  ...     "0d640df58d78766c08c037a34a8b53c9d01ef0452d75b65eb52520e96b01e659"
  ...     == low_level_hash(password, associated, salt, secret, 32, 19)
  ... )

All constants and types on ``argon2.low_level.lib`` are guaranteed to stay as long they are not altered by Argon2 itself.

.. autofunction:: error_to_str


Deprecated APIs
---------------

These APIs are from the first release of *argon2-cffi* and proved to live in an unfortunate mid-level.
On one hand they have defaults and check parameters but on the other hand they only consume byte strings.

Therefore the decision has been made to replace them by a high-level (:class:`argon2.PasswordHasher`) and a low-level (:mod:`argon2.low_level`) solution.
They will be removed in 2024.

.. autofunction:: argon2.hash_password
.. autofunction:: argon2.hash_password_raw
.. autofunction:: argon2.verify_password
