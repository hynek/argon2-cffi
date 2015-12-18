API Reference
=============

.. module:: argon2

``argon2_cffi`` comes with hopefully reasonable defaults for Argon2 parameters that result in a verification time of between 0.5ms and 1ms on recent-ish hardware.

So unless you have any special needs, all you need to know is:

.. doctest::

  >>> import argon2
  >>> hash = argon2.hash_password(b"s3kr3tp4ssw0rd")
  >>> hash  # doctest: +SKIP
  b'$argon2i$m=512,t=2,p=2$0FFfEeL6JmUnpxwgwcSC8g$98BmZUa5A/3t5wb3ZxFLBg'
  >>> argon2.verify_password(hash, b"s3kr3tp4ssw0rd")
  True
  >>> argon2.verify_password(hash, b"t0t411ywr0ng")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerificationError: Decoding failed

But of course, ``argon2_cffi`` gives you more control should you need it:


.. autofunction:: hash_password

.. doctest::

  >>> argon2.hash_password(
  ...     b"secret", b"somesalt",
  ...     time_cost=1,         # number of iterations
  ...     memory_cost=8,       # used memory in KiB
  ...     parallelism=1,       # number of threads used; changes hash!
  ...     hash_len=64,         # length of resulting raw hash
  ...     type=argon2.Type.D,  # choose Argon2i or Argon2d
  ... )
  b'$argon2d$m=8,t=1,p=1$c29tZXNhbHQ$H0oN1/L3H8t8hcg47pAyJZ8toBh2UbgcMt0zRFrqt4mEJCeKSEWGxt+KpZrMwxvr7M5qktNcc/bk/hvbinueJA'


.. autofunction:: verify_password


The raw hash can also be computed:

.. autofunction:: hash_password_raw

.. code-block:: pycon

  >>> argon2.hash_password_raw(b"secret", b"somesalt")
  b'\xd8\x87h5X%U<[\xf7\x0e\x18T\x9a\x96\xf3'


.. autoclass:: Type
  :members: D, I
