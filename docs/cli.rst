CLI
===

To aid you with finding the parameters, ``argon2_cffi`` offers a CLI interface that can be accessed using ``python -m argon2``.
It will benchmark Argon2’s password *verification* in the current environment.
You can use command line arguments to set hashing parameters:

.. code-block:: text

  $ python -m argon2 -t 1 -m 512 -p 2
   Running Argon2id 100 times with:
   hash_len: 16
   memory_cost: 512
   parallelism: 2
   time_cost: 1

   Measuring...

   0.432ms per password verification

This should make it much easier to determine the right parameters for your use case and your environment.
