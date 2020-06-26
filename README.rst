=====================================
CFFI-based Argon2 Bindings for Python
=====================================

.. image:: https://readthedocs.org/projects/argon2-cffi/badge/?version=stable
   :target: http://argon2-cffi.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://github.com/hynek/argon2-cffi/workflows/CI/badge.svg?branch=master
   :target: https://github.com/hynek/argon2-cffi/actions?workflow=CI
   :alt: CI Status

.. image:: https://codecov.io/github/hynek/argon2-cffi/branch/master/graph/badge.svg
   :target: https://codecov.io/github/hynek/argon2-cffi
   :alt: Test Coverage

.. image:: https://www.irccloud.com/invite-svg?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1
   :target: https://www.irccloud.com/invite?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1
   :alt: IRC

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black

.. teaser-begin

`Argon2 <https://github.com/p-h-c/phc-winner-argon2>`_ won the `Password Hashing Competition <https://password-hashing.net/>`_ and ``argon2-cffi`` is the simplest way to use it in Python and PyPy:

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


``argon2-cffi``\ ’s documentation lives at `Read the Docs <https://argon2-cffi.readthedocs.io/>`_, the code on `GitHub <https://github.com/hynek/argon2-cffi>`_.
It’s rigorously tested on Python 2.7, 3.5+, and PyPy.

It implements Argon2 version 1.3, as described in
`Argon2: the memory-hard function for password hashing and other applications <https://www.cryptolux.org/images/0/0d/Argon2.pdf>`_.
