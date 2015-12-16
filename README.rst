=====================================
CFFI-based Argon2 Bindings for Python
=====================================

.. image:: https://readthedocs.org/projects/argon2-cffi/badge/?version=latest
  :target: http://argon2-cffi.readthedocs.org/en/latest/?badge=latest
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

  >>> import argon2
  >>> encoded_hash = argon2.hash_password(b"secret", b"somesalt")
  >>> encoded_hash
  b'$argon2i$m=512,t=2,p=2$c29tZXNhbHQ$2IdoNVglVTxb9w4YVJqW8w'
  >>> argon2.verify_password(encoded_hash, b"secret")
  True
  >>> argon2.verify_password(encoded_hash, b"wrong")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerificationError: Decoding failed

You can omit the ``salt`` argument for a secure random `salt <https://en.wikipedia.org/wiki/Salt_(cryptography)>`_ of length ``argon2.DEFAULT_RANDOM_SALT_LENGTH``:

.. code-block:: pycon

  >>> argon2.DEFAULT_RANDOM_SALT_LENGTH
  16
  >>> argon2.hash_password(b"secret")  # doctest: +SKIP
  b'$argon2i$m=512,t=2,p=2$c29tZXNhbHQ$2IdoNVglVTxb9w4YVJqW8w'

``argon2_cffi``\ ’s documentation lives at `Read the Docs <https://argon2-cffi.readthedocs.org/>`_, the code on `GitHub <https://github.com/hynek/argon2_cffi>`_.
It’s rigorously tested on Python 2.6, 2.7, 3.3+, and PyPy.
