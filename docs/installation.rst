Installation
============

Generally speaking,

.. code-block:: bash

  pip install argon2_cffi

should be all it takes.

But since Argon2 isn't packaged on any major distribution yet, ``argon2_cffi`` vendors its C code which depending on the platform leads to complications.


Linux
-----

A working C compiler is required.
If you've been able to compile Python CFFI extensions before, ``argon2_cffi`` should install without any problems.

If something goes wrong, please try to update your ``pip`` and ``setuptools`` first:

.. code-block:: bash

  pip install -U pip setuptools


Also please note CFFI's dependencies_.


OS X & Windows
--------------

Binary `wheels <http://pythonwheels.com>`_ are provided on PyPI_.
With a recent-enough ``pip`` and ``setuptools``, they should be used automatically.

.. _PyPI: https://pypi.python.org/pypi/argon2_cffi/
.. _dependencies: https://cffi.readthedocs.org/en/latest/installation.html#platform-specific-instructions
