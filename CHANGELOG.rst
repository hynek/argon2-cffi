Changelog
=========

Versions are year-based with a strict backward compatibility policy.

*argon2-cffi* has a very strong backward compatibility policy.
Generally speaking, you shouldn't ever be afraid of updating.

Whenever breaking changes are needed, they are:

#. …announced here in the changelog.
#. …the old behavior raises a ``DeprecationWarning`` for a year (if possible).
#. …are done with another announcement in the changelog.

What explicitly *may* change over time are the default hashing parameters and the behavior of the :doc:`cli`.


21.2.0 (UNRELEASED)
-------------------

Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Python 3.5 is not supported anymore.
- The CFFI bindings have been extracted to a separated project: `argon2-cffi-bindings`_
  This makes *argon2-cffi* a Python-only project und should make it easier to contribute to and have more frequent releases with high-level features.

  This change is only breaking for users who want to use a system-wide installation of *Argon2* instead of our vendored code.
  Please refer to the `installation guide <https://argon2-cffi.readthedocs.io/en/stable/installation.html>`_.


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

*none*


----


21.1.0 (2021-08-29)
-------------------

Vendoring Argon2 @ `62358ba <https://github.com/P-H-C/phc-winner-argon2/tree/62358ba2123abd17fccf2a108a301d4b52c01a7c>`_ (20190702)


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Microsoft stopped providing the necessary SDKs to ship Python 2.7 wheels and currenly the downloads amount to 0.09%.
Therefore we have decided that Python 2.7 is not supported anymore.


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

There are indeed no changes whatsoever to the code of *argon2-cffi*.
The *Argon2* project also hasn't tagged a new release since July 2019.
There also don't seem to be any important pending fixes.

This release is mainly about improving the way binary wheels are built (abi3 on all platforms).


----


20.1.0 (2020-05-11)
-------------------

Vendoring Argon2 @ `62358ba <https://github.com/P-H-C/phc-winner-argon2/tree/62358ba2123abd17fccf2a108a301d4b52c01a7c>`_ (20190702)


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*none*


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

- It is now possible to manually override the detection of SSE2 using the ``ARGON2_CFFI_USE_SSE2`` environment variable.


----


19.2.0 (2019-10-27)
-------------------

Vendoring Argon2 @ `62358ba <https://github.com/P-H-C/phc-winner-argon2/tree/62358ba2123abd17fccf2a108a301d4b52c01a7c>`_ (20190702)


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Python 3.4 is not supported anymore.
  It has been unsupported by the Python core team for a while now and its PyPI downloads are negligible.

  It's very unlikely that *argon2-cffi* will break under 3.4 anytime soon, but we don't test it and don't ship binary wheels for it anymore.


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

- The dependency on ``enum34`` is now protected using a PEP 508 marker.
  This fixes problems when the sdist is handled by a different interpreter version than the one running it.
  `#48 <https://github.com/hynek/argon2-cffi/issues/48>`_


----


19.1.0 (2019-01-17)
-------------------

Vendoring Argon2 @ `670229c <https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6>`_ (20171227)


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*none*


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

- Added support for Argon2 v1.2 hashes in ``argon2.extract_parameters()``.


----


18.3.0 (2018-08-19)
-------------------

Vendoring Argon2 @ `670229c <https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6>`_ (20171227)


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*none*


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

- ``argon2.PasswordHasher``'s hash type is configurable now.


----


18.2.0 (2018-08-19)
-------------------

Vendoring Argon2 @ `670229c <https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6>`_ (20171227)


Changes:
^^^^^^^^

- The hash type for ``argon2.PasswordHasher`` is Argon2\ **id** now.

  This decision has been made based on the recommendations in the latest `Argon2 RFC draft <https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-argon2-04#section-4>`_.
  `#33 <https://github.com/hynek/argon2-cffi/issues/33>`_
  `#34 <https://github.com/hynek/argon2-cffi/pull/34>`_
- To make the change of hash type backward compatible, ``argon2.PasswordHasher.verify()`` now determines the type of the hash and verifies it accordingly.
- Some of the hash parameters have been made stricter to be closer to said recommendations.
  The current goal for a hash verification times is around 50ms.
  `#41 <https://github.com/hynek/argon2-cffi/pull/41>`_
- To allow for bespoke decisions about upgrading Argon2 parameters, it's now possible to extract them from a hash via the ``argon2.extract_parameters()`` function.
  `#41 <https://github.com/hynek/argon2-cffi/pull/41>`_
- Additionally ``argon2.PasswordHasher`` now has a ``check_needs_rehash()`` method that allows to verify whether a hash has been created with the instance's parameters or whether it should be rehashed.
  `#41 <https://github.com/hynek/argon2-cffi/pull/41>`_


----


18.1.0 (2018-01-06)
-------------------

Vendoring Argon2 @ `670229c <https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6>`_ (20171227)


Changes:
^^^^^^^^

- It is now possible to use the *argon2-cffi* bindings against an Argon2 library that is provided by the system.


----


16.3.0 (2016-11-10)
-------------------

Vendoring Argon2 @ `1c4fc41f81f358283755eea88d4ecd05e43b7fd3 <https://github.com/P-H-C/phc-winner-argon2/tree/1c4fc41f81f358283755eea88d4ecd05e43b7fd3>`_ (20161029)

Changes:
^^^^^^^^

- Prevent side-effects like the installation of ``cffi`` if ``setup.py`` is called with a command that doesn't require it.
  `#20 <https://github.com/hynek/argon2-cffi/pull/20>`_
- Fix a bunch of warnings with new ``cffi`` versions and Python 3.6.
  `#14 <https://github.com/hynek/argon2-cffi/pull/14>`_
  `#16 <https://github.com/hynek/argon2-cffi/issues/16>`_
- Add low-level bindings for Argon2id functions.


----


16.2.0 (2016-09-10)
-------------------

Vendoring Argon2 @ `4844d2fee15d44cb19296ddf36029326d17c5aa3 <https://github.com/P-H-C/phc-winner-argon2/tree/4844d2fee15d44cb19296ddf36029326d17c5aa3>`_

Changes:
^^^^^^^^

- Fix compilation on debian jessie.
  `#13 <https://github.com/hynek/argon2-cffi/pull/13>`_


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
- Add support for `Argon2 1.3 <https://mailarchive.ietf.org/arch/msg/cfrg/beOzPh41Hz3cjl5QD7MSRNTi3lA/>`_.
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
.. _argon2-cffi-bindings: https://github.com/hynek/argon2-cffi-bindings
