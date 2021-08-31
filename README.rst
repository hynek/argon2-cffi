===================
*Argon2* for Python
===================

.. image:: https://img.shields.io/badge/Docs-Read%20The%20Docs-black
   :target: https://argon2-cffi.readthedocs.io/
   :alt: Documentation

.. image:: https://img.shields.io/badge/license-MIT-C06524
   :target: https://github.com/hynek/argon2-cffi/blob/main/LICENSE
   :alt: License: MIT

.. image:: https://img.shields.io/pypi/v/argon2-cffi
   :target: https://pypi.org/project/argon2-cffi/
   :alt: PyPI version

.. image:: https://static.pepy.tech/personalized-badge/argon2-cffi?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads%20/%20Month
   :target: https://pepy.tech/project/argon2-cffi
   :alt: Downloads / Month


.. -begin-short-

`Argon2 <https://github.com/p-h-c/phc-winner-argon2>`_ won the `Password Hashing Competition <https://www.password-hashing.net/>`_ and *argon2-cffi* is the simplest way to use it in Python and PyPy:

.. code-block:: pycon

  >>> from argon2 import PasswordHasher
  >>> ph = PasswordHasher()
  >>> hash = ph.hash("s3kr3tp4ssw0rd")
  >>> hash  # doctest: +SKIP
  '$argon2id$v=19$m=102400,t=2,p=8$tSm+JOWigOgPZx/g44K5fQ$WDyus6py50bVFIPkjA28lQ'
  >>> ph.verify(hash, "s3kr3tp4ssw0rd")
  True
  >>> ph.check_needs_rehash(hash)
  False
  >>> ph.verify(hash, "t0t411ywr0ng")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerifyMismatchError: The password does not match the supplied hash

.. -end-short-


.. -begin-meta-

Project Information
===================


*argon2-cffi*'s documentation lives at `Read the Docs <https://argon2-cffi.readthedocs.io/>`_, the code on `GitHub <https://github.com/hynek/argon2-cffi>`_.

It targets Python 3.6 and newer, and PyPy3.
The last version that works with Python 2.7 is 20.1.0, and the last version that works with Python 3.5 is 21.1.0.

*argon2-cffi* implements *Argon2* version 1.3, as described in
`Argon2: the memory-hard function for password hashing and other applications <https://www.cryptolux.org/images/0/0d/Argon2.pdf>`_.


*argon2-cffi* for Enterprise
----------------------------

Available as part of the Tidelift Subscription.

The maintainers of *argon2-cffi* and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source packages you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact packages you use. `Learn more. <https://tidelift.com/subscription/pkg/pypi-argon2-cffi?utm_source=undefined&utm_medium=referral&utm_campaign=enterprise&utm_term=repo>`_

.. -end-meta-
