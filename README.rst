=====================================
CFFI-based Argon2 Bindings for Python
=====================================

.. image:: https://readthedocs.org/projects/argon2-cffi/badge/?version=stable
  :target: http://argon2-cffi.readthedocs.org/en/latest/?badge=stable
  :alt: Documentation Status

.. image:: https://travis-ci.org/hynek/argon2_cffi.svg?branch=master
  :target: https://travis-ci.org/hynek/argon2_cffi

.. image:: https://codecov.io/github/hynek/argon2_cffi/coverage.svg?branch=master
  :target: https://codecov.io/github/hynek/argon2_cffi

.. image:: https://ci.appveyor.com/api/projects/status/3faufu7qgwc8nv2v/branch/master?svg=true
  :target: https://ci.appveyor.com/project/hynek/argon2-cffi

.. image:: https://www.irccloud.com/invite-svg?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1
  :target: https://www.irccloud.com/invite?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1

.. teaser-begin

`Argon2 <https://github.com/p-h-c/phc-winner-argon2>`_ won the `Password Hashing Competition <https://password-hashing.net/>`_ and ``argon2_cffi`` is the simplest way to use it in Python and PyPy:

.. code-block:: pycon

  >>> from argon2 import PasswordHasher
  >>> ph = PasswordHasher()
  >>> hash = ph.hash("secret")
  >>> hash   # doctest: +SKIP
  '$argon2i$m=512,t=2,p=2$c29tZXNhbHQ$2IdoNVglVTxb9w4YVJqW8w'
  >>> ph.verify(hash, "secret")
  True
  >>> ph.verify(hash, "wrong")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerificationError: Decoding failed


``argon2_cffi``\ ’s documentation lives at `Read the Docs <https://argon2-cffi.readthedocs.org/>`_, the code on `GitHub <https://github.com/hynek/argon2_cffi>`_.
It’s rigorously tested on Python 2.7, 3.4+, and PyPy.
