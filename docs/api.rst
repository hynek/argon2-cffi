API Reference
=============

.. module:: argon2

``argon2_cffi`` comes with hopefully reasonable defaults for Argon2 parameters that result in a verification time of between 0.5ms and 1ms on recent-ish hardware.
But of course, you can set them yourself if you wish:


.. autofunction:: hash_password

.. code-block:: pycon

  >>> import argon2
  >>> argon2.hash_password(
  ...     b"secret", b"somesalt",
  ...     time_cost=1,         # number of iterations
  ...     memory_cost=8,       # used memory in KiB
  ...     parallelism=1,       # number of threads used; changes hash!
  ...     hash_len=64,         # length of resulting raw hash
  ...     type=argon2.Type.D,  # choose Argon2i or Argon2d
  ... )
  b'$argon2d$m=8,t=1,p=1$c29tZXNhbHQ$H0oN1/L3H8t8hcg47pAyJZ8toBh2UbgcMt0zRFrqt4mEJCeKSEWGxt+KpZrMwxvr7M5qktNcc/bk/hvbinueJA'

The raw hash can also be computed:

.. autofunction:: hash_password_raw

.. code-block:: pycon

  >>> argon2.hash_password_raw(b"secret", b"somesalt")
  b'\xd8\x87h5X%U<[\xf7\x0e\x18T\x9a\x96\xf3'

.. autoclass:: Type
  :members: D, I
