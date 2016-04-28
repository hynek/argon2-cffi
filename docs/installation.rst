Installation
============

Generally speaking,

.. code-block:: bash

  pip install argon2_cffi

should be all it takes.

But since Argon2 (the C library) isn't packaged on any major distribution yet, ``argon2_cffi`` vendors its C code which depending on the platform can lead to complications.

The C code is known to compile and work on all common platforms (including x86, ARM, and PPC).
On x86, an SSE2_-optimized version is used.

If something goes wrong, please try to update your ``cffi``, ``pip`` and ``setuptools`` first:

.. code-block:: bash

  pip install -U cffi pip setuptools


OS X & Windows
--------------

Binary `wheels <http://pythonwheels.com>`_ are provided on PyPI_.
With a recent-enough ``pip`` and ``setuptools``, they should be used automatically.


Linux
-----

A working C compiler and `CFFI environment`_ is required.
If you've been able to compile Python CFFI extensions before, ``argon2_cffi`` should install without any problems.


.. _SSE2: https://en.wikipedia.org/wiki/SSE2
.. _PyPI: https://pypi.python.org/pypi/argon2_cffi/
.. _CFFI environment: https://cffi.readthedocs.io/en/latest/installation.html
