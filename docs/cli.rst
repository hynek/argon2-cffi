CLI
===

To aid you with finding the parameters, *argon2-cffi* offers a CLI interface that can be accessed using ``python -m argon2``.
It will benchmark *Argon2*’s password *verification* in the current environment:

.. code-block:: console

   $ python -m argon2
   Running Argon2id 100 times with:
   hash_len: 32 bytes
   memory_cost: 65536 KiB
   parallelism: 4 threads
   time_cost: 3 iterations

   Measuring...

   45.7ms per password verification

You can use command line arguments to set hashing parameters.
Either by setting them one by one (``-t`` for time, ``-m`` for memory, ``-p`` for parallelism, ``-l`` for hash length), or by passing ``--profile`` followed by one of the names from :mod:`argon2.profiles`.
In that case, the other parameters are ignored.
If you don't pass any arguments as above, it runs with :class:`argon2.PasswordHasher`'s default values.

This should make it much easier to determine the right parameters for your use case and your environment.
