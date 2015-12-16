Choosing Parameters
===================

Finding the right parameters for a password hashing algorithm is a daunting task.
The authors of Argon2 specified a method in their `paper <https://github.com/P-H-C/phc-winner-argon2/blob/master/argon2-specs.pdf>`_ but it should be noted that they also  mention that no value for ``time_cost`` or ``memory_cost`` is actually insecure (cf. section 6.4).

#. Choose whether you want Argon2i or Argon2d (``type``).
   If you don't know what that means, choose Argon2i (:attr:`argon2.Type.I`).
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

``argon2_cffi``'s :doc:`cli` will help you with this process.
