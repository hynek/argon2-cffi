Choosing Parameters
===================

.. note::

  You can probably just use :class:`argon2.PasswordHasher` with its default values and be fine.
  But it's good to double check using ``argon2_cffi``'s :doc:`cli` client, whether its defaults are too slow or too fast for your use case.

Finding the right parameters for a password hashing algorithm is a daunting task.
The authors of Argon2 specified a method in their `paper <https://github.com/P-H-C/phc-winner-argon2/blob/master/argon2-specs.pdf>`_, however some parts of it have been revised in the `RFC draft`_ for Argon2 that is currently being written.

The current recommended best practice is as follow:

#. Choose whether you want Argon2i, Argon2d, or Argon2id (``type``).
   If you don't know what that means, choose Argon2id (:attr:`argon2.Type.ID`).
#. Figure out how many threads can be used on each call to Argon2 (``parallelism``, called "lanes" in the RFC).
   They recommend twice as many as the number of cores dedicated to hashing passwords.
   :class:`~argon2.PasswordHasher` will *not* determine this for you and use a default value that you can find in the linked API docs.
#. Figure out how much memory each call can afford (``memory_cost``).
   The RFC recommends 4 GB for backend authentication and 1 GB for frontend authentication.
#. Select the salt length.
   16 bytes is sufficient for all applications, but can be reduced to 8 bytes in the case of space constraints.
#. Choose a hash length (``hash_len``, called "tag length" in the documentation).
   16 bytes is sufficient for password verification.
#. Figure out how long each call can take.
   One `recommendation <https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2015/march/enough-with-the-salts-updates-on-secure-password-schemes/>`_ for concurent user logins is to keep it under 0.5 ms.
   The RFC recommends under 500 ms.
#. Measure the time for hashing using your chosen parameters.
   Find a ``time_cost`` that is within your accounted time.
   If ``time_cost=1`` takes too long, lower ``memory_cost``.

``argon2_cffi``'s :doc:`cli` will help you with this process.


.. _`RFC draft`: https://tools.ietf.org/html/draft-irtf-cfrg-argon2-03#section-4
