=====================================
CFFI-based Argon2 Bindings for Python
=====================================

.. image:: https://img.shields.io/pypi/v/argon2_cffi.svg
  :target: https://pypi.python.org/pypi/argon2_cffi

.. image:: https://readthedocs.org/projects/argon2-cffi/badge/?version=stable
  :target: http://argon2-cffi.readthedocs.io/en/latest/?badge=stable
  :alt: Documentation Status

.. image:: https://travis-ci.org/hynek/argon2_cffi.svg?branch=master
  :target: https://travis-ci.org/hynek/argon2_cffi

.. image:: https://codecov.io/github/hynek/argon2_cffi/branch/master/graph/badge.svg
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
  >>> hash = ph.hash("s3kr3tp4ssw0rd")
  >>> hash  # doctest: +SKIP
  '$argon2i$v=19$m=512,t=2,p=2$5VtWOO3cGWYQHEMaYGbsfQ$AcmqasQgW/wI6wAHAMk4aQ'
  >>> ph.verify(hash, "s3kr3tp4ssw0rd")
  True
  >>> ph.verify(hash, "t0t411ywr0ng")
  Traceback (most recent call last):
    ...
  argon2.exceptions.VerifyMismatchError: The password does not match the supplied hash


``argon2_cffi``\ ’s documentation lives at `Read the Docs <https://argon2-cffi.readthedocs.io/>`_, the code on `GitHub <https://github.com/hynek/argon2_cffi>`_.
It’s rigorously tested on Python 2.7, 3.4+, and PyPy.
