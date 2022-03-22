What is *Argon2*?
=================

.. note::

  **TL;DR**: Use :class:`argon2.PasswordHasher` with its default parameters to securely hash your passwords.

  You do **not** need to read or understand anything below this box.

*Argon2* is a secure password hashing algorithm.
It is designed to have both a configurable runtime as well as memory consumption.

This means that you can decide how long it takes to hash a password and how much memory is required.

In September 2021, *Argon2* has been properly standardized by the IETF in :rfc:`9106`.

*Argon2* comes in three variants: Argon2\ **d**, Argon2\ **i**, and Argon2\ **id**.
Argon2\ **d**'s strength is the resistance against `time–memory trade-offs`_, while Argon2\ **i**'s focus is on resistance against `side-channel attacks`_.

Accordingly, Argon2\ **i** was originally considered the correct choice for password hashing and password-based key derivation.
In practice it turned out that a *combination* of d and i -- that combines their strenghts -- is the better choice.
And so Argon2\ **id** was born and is now considered the *main variant* (and the only variant required by the RFC to be implemented).

.. _`time–memory trade-offs`: https://en.wikipedia.org/wiki/Space–time_tradeoff
.. _`side-channel attacks`: https://en.wikipedia.org/wiki/Side-channel_attack


Why “just use bcrypt” Is Not the Best Answer (Anymore)
------------------------------------------------------

The current workhorses of password hashing are unquestionably bcrypt_ and PBKDF2_.
And while they're still fine to use, the password cracking community embraced new technologies like GPU_\ s and ASIC_\ s to crack password in a highly parallel fashion.

An effective measure against extreme parallelism proved making computation of password hashes also *memory* hard.
The best known implementation of that approach is to date scrypt_.
However according to the `Argon2 paper`_ [#outdated]_, page 2:

  […] the existence of a trivial time-memory tradeoff allows compact implementations with the same energy cost.

Therefore a new algorithm was needed.
This time future-proof and with committee-vetting instead of single implementors.

.. [#outdated] Please note that the paper is in some parts outdated.
   For instance it predates the genesis of Argon2\ **id**.
   Generally please refer to :rfc:`9106` instead.

.. _bcrypt: https://en.wikipedia.org/wiki/Bcrypt
.. _PBKDF2: https://en.wikipedia.org/wiki/PBKDF2
.. _GPU: https://hashcat.net/hashcat/
.. _ASIC: https://en.wikipedia.org/wiki/Application-specific_integrated_circuit
.. _scrypt: https://en.wikipedia.org/wiki/Scrypt
.. _Argon2 paper: https://www.password-hashing.net/argon2-specs.pdf


Password Hashing Competition
----------------------------

The `Password Hashing Competition`_ took place between 2012 and 2015 to find a new, secure, and future-proof password hashing algorithm.
Previously the NIST was in charge but after certain events and revelations_ their integrity has been put into question by the general public.
So a group of independent cryptographers and security researchers came together.

In the end, *Argon2* was announced_ as the winner.

.. _Password Hashing Competition: https://www.password-hashing.net/
.. _revelations: https://en.wikipedia.org/wiki/Dual_EC_DRBG
.. _announced: https://groups.google.com/forum/#!topic/crypto-competitions/3QNdmwBS98o
