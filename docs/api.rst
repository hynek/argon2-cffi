API Reference
=============

.. module:: argon2

``argon2_cffi`` comes with an high-level API and hopefully reasonable defaults for Argon2 parameters that result in a verification time of between 0.5ms and 1ms on recent-ish hardware.

Unless you have any special needs, all you need to know is:

.. doctest::

  >>> from argon2 import PasswordHasher
  >>> ph = PasswordHasher()
  >>> hash = ph.hash("s3kr3tp4ssw0rd")
  >>> hash  # doctest: +SKIP
  u'$argon2i$m=512,t=2,p=2$0FFfEeL6JmUnpxwgwcSC8g$98BmZUa5A/3t5wb3ZxFLBg'
  >>> ph.verify(hash, "s3kr3tp4ssw0rd")
  True
  >>> ph.verify(hash, "t0t411ywr0ng")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerificationError: Decoding failed

But of course the :class:`PasswordHasher` class has all the parametrization you'll need:

.. autoclass:: PasswordHasher
  :members: hash, verify


.. autoexception:: argon2.exceptions.VerificationError

.. autoexception:: argon2.exceptions.HashingError


Low Level
---------

Use these functions if you want to build your own high-level abstraction.

.. autoclass:: Type
  :members: D, I


.. module:: argon2.low_level

.. autofunction:: hash_secret

.. doctest::

  >>> import argon2
  >>> argon2.low_level.hash_secret(
  ...     b"secret", b"somesalt",
  ...     time_cost=1, memory_cost=8, parallelism=1, hash_len=64, type=argon2.Type.D
  ... )
  b'$argon2d$m=8,t=1,p=1$c29tZXNhbHQ$H0oN1/L3H8t8hcg47pAyJZ8toBh2UbgcMt0zRFrqt4mEJCeKSEWGxt+KpZrMwxvr7M5qktNcc/bk/hvbinueJA'


.. autofunction:: verify_secret


The raw hash can also be computed:

.. autofunction:: hash_secret_raw

.. code-block:: pycon

  >>> argon2.low_level.hash_password_raw(b"secret", b"somesalt")
  b'\xd8\x87h5X%U<[\xf7\x0e\x18T\x9a\x96\xf3'


Deprecated APIs
---------------

These APIs are from the first release of ``argon2_cffi`` and proved to live in an unfortunate mid-level.
On one hand they have defaults and check parameters but on the other hand they only consume byte strings.

Therefore the decision has been made to replace them by a high-level (:class:`argon2.PasswordHasher`) and a low-level (:mod:`argon2.low_level`) solution.
There are no immediate plans to remove them though.

.. autofunction:: argon2.hash_password
.. autofunction:: argon2.hash_password_raw
.. autofunction:: argon2.verify_password
