Argon2
======

.. note::

  **TL;DR**: Use :class:`argon2.PasswordHasher` with its default parameters to securely hash your passwords.

  You do **not** need to read or understand anything below this box.

Argon2 is a secure password hashing algorithm.
It is designed to have both a configurable runtime as well as memory consumption.

This means that you can decide how long it takes to hash a password and how much memory is required.

Argon2 comes in three variants:

Argon2d
  is faster and uses data-depending memory access, which makes it less suitable for hashing secrets and more suitable for cryptocurrencies and applications with no threats from side-channel timing attacks.

Argon2i
  uses data-independent memory access, which is preferred for password hashing and password-based key derivation.
  Argon2i is slower as it makes more passes over the memory to protect from tradeoff attacks.

Argon2id
  is a hybrid of Argon2i and Argon2d, using a combination of data-depending and data-independent memory accesses, which gives some of Argon2i's resistance to side-channel cache timing attacks and much of Argon2d's resistance to GPU cracking attacks.


Why “just use bcrypt” Is Not the Best Answer (Anymore)
------------------------------------------------------

The current workhorses of password hashing are unquestionably bcrypt_ and PBKDF2_.
And while they're still fine to use, the password cracking community embraced new technologies like GPU_\ s and ASIC_\ s to crack password in a highly parallel fashion.

An effective measure against extreme parallelism proved making computation of password hashes also *memory* hard.
The best known implementation of that approach is to date scrypt_.
However according to the `Argon2 paper`_, page 2:

  […] the existence of a trivial time-memory tradeoff allows compact implementations with the same energy cost.

Therefore a new algorithm was needed.
This time future-proof and with committee-vetting instead of single implementors.

.. _bcrypt: https://en.wikipedia.org/wiki/Bcrypt
.. _PBKDF2: https://en.wikipedia.org/wiki/PBKDF2
.. _GPU: https://hashcat.net/hashcat/
.. _ASIC: https://en.wikipedia.org/wiki/Application-specific_integrated_circuit
.. _scrypt: https://en.wikipedia.org/wiki/Scrypt
.. _Argon2 paper: https://password-hashing.net/argon2-specs.pdf


Password Hashing Competition
----------------------------

The `Password Hashing Competition`_ took place between 2012 and 2015 to find a new, secure, and future-proof password hashing algorithm.
Previously the NIST was in charge but after certain events and revelations_ their integrity has been put into question by the general public.
So a group of independent cryptographers and security researchers came together.

In the end, Argon2 was announced_ as the winner.

.. _Password Hashing Competition: https://password-hashing.net/
.. _revelations: https://en.wikipedia.org/wiki/Dual_EC_DRBG
.. _announced: https://groups.google.com/forum/#!topic/crypto-competitions/3QNdmwBS98o
