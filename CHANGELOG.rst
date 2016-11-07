Changelog
=========

Versions are year-based with a strict backward compatibility policy.
The third digit is only for regressions.


16.3.0 (UNRELEASED)
-------------------

Changes:
^^^^^^^^

- Prevent side-effects like the installation of ``cffi`` if ``setup.py`` is called with a command that doesn't require it.
  `#20 <https://github.com/hynek/argon2_cffi/pull/20>`_
- Fix a bunch of warnings with new ``cffi`` versions and Python 3.6.
  `#14 <https://github.com/hynek/argon2_cffi/pull/14>`_
  `#16 <https://github.com/hynek/argon2_cffi/pull/16>`_


----


16.2.0 (2016-09-10)
-------------------

Vendoring Argon2 @ `4844d2fee15d44cb19296ddf36029326d17c5aa3 <https://github.com/P-H-C/phc-winner-argon2/tree/4844d2fee15d44cb19296ddf36029326d17c5aa3>`_

Changes:
^^^^^^^^

- Fix compilation on debian jessie.
  `#13 <https://github.com/hynek/argon2_cffi/pull/13>`_


----


16.1.0 (2016-04-19)
-------------------

Vendoring Argon2 @ 00aaa6604501fade85853a4b2f5695611ff6e7c5_.

Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Python 3.3 and 2.6 aren't supported anymore.
  They may work by chance but any support to them has been ceased.

  The last Python 2.6 release was on October 29, 2013 and isn't supported by the CPython core team anymore.
  Major Python packages like Django and Twisted dropped Python 2.6 a while ago already.

  Python 3.3 never had a significant user base and wasn't part of any distribution's LTS release.

Changes:
^^^^^^^^

- Add ``VerifyMismatchError`` that is raised if verification fails only because of a password/hash mismatch.
  It's a subclass of ``VerificationError`` therefore this change is completely backward compatible.
- Add support for `Argon2 1.3 <https://www.ietf.org/mail-archive/web/cfrg/current/msg07948.html>`_.
  Old hashes remain functional but opportunistic rehashing is strongly recommended.


----


16.0.0 (2016-01-02)
-------------------

Vendoring Argon2 @ 421dafd2a8af5cbb215e16da5953663eb101d139_.

Deprecations:
^^^^^^^^^^^^^

- ``hash_password()``, ``hash_password_raw()``, and ``verify_password()`` should not be used anymore.
  For hashing passwords, use the new ``argon2.PasswordHasher``.
  If you want to implement your own higher-level abstractions, use the new low-level APIs ``hash_secret()``, ``hash_secret_raw()``, and ``verify_secret()`` from the ``argon2.low_level`` module.
  If you want to go *really* low-level, ``core()`` is for you.
  The old functions will *not* raise any warnings though and there are *no* immediate plans to remove them.

Changes:
^^^^^^^^

- Add ``argon2.PasswordHasher``.
  A higher-level class specifically for hashing passwords that also works on Unicode strings.
- Add ``argon2.low_level`` module with low-level API bindings for building own high-level abstractions.


----


15.0.1 (2015-12-18)
-------------------

Vendoring Argon2 @ 4fe0d8cda37691228dd5a96a310be57369403a4b_.

Changes:
^^^^^^^^

- Fix ``long_description`` on PyPI.


----


15.0.0 (2015-12-18)
-------------------

Vendoring Argon2 @ 4fe0d8cda37691228dd5a96a310be57369403a4b_.

Changes:
^^^^^^^^

- ``verify_password()`` doesn't guess the hash type if passed ``None`` anymore.
  Supporting this resulted in measurable overhead (~ 0.6ms vs 0.8ms on my notebook) since it had to happen in Python.
  That means that naïve usage of the API would give attackers an edge.
  The new behavior is that it has the same default value as ``hash_password()`` such that ``verify_password(hash_password(b"password"), b"password")`` still works.
- Conditionally use the `SSE2 <https://en.wikipedia.org/wiki/SSE2>`_-optimized version of ``argon2`` on x86 architectures.
- More packaging fixes.
  Most notably compilation on Visual Studio 2010 for Python 3.3 and 3.4.
- Tweaked default parameters to more reasonable values.
  Verification should take between 0.5ms and 1ms on recent-ish hardware.


----


15.0.0b5 (2015-12-10)
---------------------

Vendoring Argon2 @ 4fe0d8cda37691228dd5a96a310be57369403a4b_.

Initial work.
Previous betas were only for fixing Windows packaging.
The authors of Argon2 were kind enough to `help me <https://github.com/P-H-C/phc-winner-argon2/issues/44>`_ to get it building under Visual Studio 2008 that we’re forced to use for Python 2.7 on Windows.


.. _421dafd2a8af5cbb215e16da5953663eb101d139: https://github.com/P-H-C/phc-winner-argon2/tree/421dafd2a8af5cbb215e16da5953663eb101d139
.. _4fe0d8cda37691228dd5a96a310be57369403a4b: https://github.com/P-H-C/phc-winner-argon2/tree/4fe0d8cda37691228dd5a96a310be57369403a4b
.. _00aaa6604501fade85853a4b2f5695611ff6e7c5: https://github.com/P-H-C/phc-winner-argon2/tree/00aaa6604501fade85853a4b2f5695611ff6e7c5
