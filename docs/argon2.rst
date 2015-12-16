Argon2
======

.. note::

  **TL;DR**: Use Argon2\ **i** to securely hash your passwords.

Argon2 is a secure password hashing algorithm.
It is designed to have both a configurable runtime as well as memory consumption.

This means that you can decide how long it takes to hash a password and how much memory is required.

Argon2 comes in two variants:
Argon2\ **d** is faster and uses data-depending memory access, which makes it suitable for cryptocurrencies and applications with no threats from side-channel timing attacks.
Argon2\ **i** uses data-independent memory access, which is preferred for password hashing and password-based key derivation. Argon2i is slower as it makes more passes over the memory to protect from tradeoff attacks.


Why “just use bcrypt” Is Not the Answer
---------------------------------------

There's an unfortunate meme to respond to questions of storage of secrets like passwords to “just use bcrypt_”.
The problem is, neither bcrypt nor its closest NIST-approved competitor PBKDF2_ are fit for hashing passwords in the days of ASIC_ password breakers.
In a nutshell, password crackers are able to create highly parallelized hardware specifically tailored to crack computationally expensive password hashes.

An effective measure against extreme parallelism proved making computation of password hashes also *memory* hard.
The best known implementation of that approach is to date scrypt_.
However according to the `Argon2 paper`_, page 2:

  […] the existence of a trivial time-memory tradeoff allows compact implementations with the same energy cost.


Therefore a new algorithm was needed.

.. _bcrypt: https://en.wikipedia.org/wiki/Bcrypt
.. _PBKDF2: https://en.wikipedia.org/wiki/PBKDF2
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
