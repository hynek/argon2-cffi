CLI
===

To aid you with finding the parameters, ``argon2_cffi`` offers a CLI interface that can be accessed using ``python -m argon2``.
It will benchmark Argon2’s password *verification* in the current environment.
You can use command line arguments to set hashing parameters:

.. code-block:: text

   $ python -m argon2
   Running Argon2id 100 times with:
   hash_len: 16 bytes
   memory_cost: 102400 KiB
   parallelism: 8 threads
   time_cost: 2 iterations

   Measuring...

   45.3ms per password verification

This should make it much easier to determine the right parameters for your use case and your environment.
