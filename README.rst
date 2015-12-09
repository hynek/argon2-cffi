=====================================
CFFI-based Argon2 Bindings for Python
=====================================

.. image:: https://travis-ci.org/hynek/argon2_cffi.svg?branch=master
  :target: https://travis-ci.org/hynek/argon2_cffi

.. image:: https://codecov.io/github/hynek/argon2_cffi/coverage.svg?branch=master
  :target: https://codecov.io/github/hynek/argon2_cffi

.. image:: https://www.irccloud.com/invite-svg?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1
    :target: https://www.irccloud.com/invite?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1

.. begin


`Argon2 <https://github.com/p-h-c/phc-winner-argon2>`_ won the `Password Hashing Competition <https://password-hashing.net/>`_ in 2015.
``argon2_cffi`` is the simplest way to use it in Python and PyPy:

.. code-block:: pycon

  >>> import argon2
  >>> encoded_hash = argon2.hash_password(b"secret", b"somesalt")
  >>> encoded_hash
  b'$argon2i$m=4096,t=3,p=2$c29tZXNhbHQ$FNqxwHC2l1liWu3JTgGn6w'
  >>> argon2.verify_password(encoded_hash, b"secret")
  True
  >>> argon2.verify_password(encoded_hash, b"wrong")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerificationError: Decoding failed

You can omit the ``salt`` argument for a secure random salt of length ``argon2.DEFAULT_RANDOM_SALT_LENGTH``:

.. code-block:: pycon

  >>> argon2.hash_password(b"secret")  # doctest: +SKIP
  b'$argon2i$m=4096,t=3,p=2$GIESi4asMZaP051OPlH/zw$s5bQHIupLB1Fep/U5NXIVQ'


Installation
============

A working C compiler is required because the official Argon2 C implementation is shipped along with the Python CFFI bindings.
Otherwise a plain ``pip install argon2_cffi`` should just work.


Hands-on
========

``argon2_cffi`` comes with hopefully reasonable defaults for Argon2 parameters.
But of course, you can set them yourself if you wish:

.. code-block:: pycon

  >>> argon2.hash_password(
  ...     b"secret", b"somesalt",
  ...     time_cost=1,         # number of iterations
  ...     memory_cost=8,       # used memory in KiB
  ...     parallelism=1,       # number of threads used; changes hash!
  ...     hash_len=64,         # length of resulting raw hash
  ...     type=argon2.Type.D,  # choose Argon2i or Argon2d
  ... )
  b'$argon2d$m=8,t=1,p=1$c29tZXNhbHQ$H0oN1/L3H8t8hcg47pAyJZ8toBh2UbgcMt0zRFrqt4mEJCeKSEWGxt+KpZrMwxvr7M5qktNcc/bk/hvbinueJA'

The raw hash can also be computed.
The function takes the same parameters as ``hash_password()``:

.. code-block:: pycon

  >>> argon2.hash_password_raw(b"secret", b"somesalt")
  b'\x14\xda\xb1\xc0p\xb6\x97YbZ\xed\xc9N\x01\xa7\xeb'


Choosing Parameters
-------------------

Finding the right parameters for a password hashing algorithm is a daunting task.
The authors of Argon2 specified a method in their `paper <https://github.com/P-H-C/phc-winner-argon2/blob/master/argon2-specs.pdf>`_ but it should be noted that they also  mention that no value for ``time_cost`` or ``memory_cost`` is actually insecure (cf. section 6.4).


#. Choose whether you want Argon2i or Argon2d (``type``).
   If you don't know what that means, choose Argon2i (``Type.I``).
#. Figure out how many threads can be used on each call to Argon2 (``parallelism``).
   They recommend twice as many as the number of cores dedicated to hashing passwords.
#. Figure out how much memory each call can afford (``memory_cost``).
#. Choose a salt length.
   16 Bytes are fine.
#. Choose a hash length (``hash_len``).
   16 Bytes are fine.
#. Figure out how long each call can take.
   One `recommendation <https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2015/march/enough-with-the-salts-updates-on-secure-password-schemes/>`_ for concurent user logins is to keep it under 0.5ms.
#. Measure the time for hashing using your chosen parameters.
   Find a ``time_cost`` that is within your accounted time.
   If ``time_cost=1`` takes too long, lower ``memory_cost``.


CLI
^^^

To aid you with finding the parameters, ``argon2_cffi`` offers a CLI interface that can be accessed using ``python -m argon2``.
It will benchmark Argon2’s *password verification* in the current environment.
You can use command line arguments to set hashing parameters:

.. code-block:: text

  $ python -m argon2 -t 1 -m 512 -p 2
  Running Argon2i 100 times with:
  hash_len: 16
  memory_cost: 512
  parallelism: 2
  time_cost: 1

  Measuring...

  0.418ms per password verification

This should make it much easier to determine the right parameters for your use case and your environment.
