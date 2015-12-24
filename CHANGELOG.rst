Changelog
=========

Versions are year-based with a strict backward compatibility policy.
The third digit is only for regressions.


16.0.0 (UNRELEASED)
-------------------

Vendoring ``argon2`` @ 69cb15836e31c65edb515f94da0ee31e88705189_.

Deprecations:
^^^^^^^^^^^^^

- ``hash_password()``, ``hash_password_raw()``, and ``verify_password()`` should not be used anymore.
  For hashing passwords, use the new ``argon2.PasswordHasher``.
  If you want to implement your own higher-level abstractions, use the new low-level APIs ``hash_secret()``, ``hash_secret_raw()``, and ``verify_secret()`` from the ``argon2.low_level`` module.
  The old functions will *not* raise any warnings though and there are *no* immediate plans to remove them.

Changes:
^^^^^^^^

- Add ``argon2.PasswordHasher``.
  A higher-level class specifically for hashing passwords that also works on unicode.


15.0.1 (2015-12-18)
-------------------

Vendoring ``argon2`` @ 4fe0d8cda37691228dd5a96a310be57369403a4b_.

Changes:
^^^^^^^^

- Fix ``long_description`` on PyPI.


15.0.0 (2015-12-18)
-------------------

Vendoring ``argon2`` @ 4fe0d8cda37691228dd5a96a310be57369403a4b_.

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


15.0.0b5 (2015-12-10)
---------------------

Vendoring ``argon2`` @ 4fe0d8cda37691228dd5a96a310be57369403a4b_.

Initial work.
Previous betas were only for fixing Windows packaging.
The authors of ``argon2`` were kind enough to `help me <https://github.com/P-H-C/phc-winner-argon2/issues/44>`_ to get it building under Visual Studio 2008 that we’re forced to use for Python 2.7 on Windows.


.. _69cb15836e31c65edb515f94da0ee31e88705189: https://github.com/P-H-C/phc-winner-argon2/tree/69cb15836e31c65edb515f94da0ee31e88705189
.. _4fe0d8cda37691228dd5a96a310be57369403a4b: https://github.com/P-H-C/phc-winner-argon2/tree/4fe0d8cda37691228dd5a96a310be57369403a4b
