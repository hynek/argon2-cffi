# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Calendar Versioning](https://calver.org/).

The **first number** of the version is the year.
The **second number** is incremented with each release, starting at 1 for each year.
The **third number** is when we need to start branches for older releases (only for emergencies).

You can find our backwards-compatibility policy [here](https://github.com/hynek/argon2-cffi/blob/main/.github/SECURITY.md).

<!-- changelog follows -->


## [25.1.0](https://github.com/hynek/argon2-cffi/compare/23.1.0...25.1.0) - 2025-06-03

### Added

- Official support for Python 3.13 and 3.14.
  No code changes were necessary.


### Removed

- Python 3.7 is not supported anymore.
  [#186](https://github.com/hynek/argon2-cffi/pull/186)


### Changed

- `argon2.PasswordHasher.check_needs_rehash()` now also accepts bytes like the rest of the API.
  [#174](https://github.com/hynek/argon2-cffi/pull/174)

- Improved parameter compatibility handling for Pyodide / WebAssembly environments.
  [#190](https://github.com/hynek/argon2-cffi/pull/190)


## [23.1.0](https://github.com/hynek/argon2-cffi/compare/21.3.0...23.1.0) - 2023-08-15

### Removed

- Python 3.6 is not supported anymore.


### Deprecated

- The `InvalidHash` exception is deprecated in favor of `InvalidHashError`.
  No plans for removal currently exist and the names can (but shouldn't) be used interchangeably.

- `argon2.hash_password()`, `argon2.hash_password_raw()`, and `argon2.verify_password()` that have been soft-deprecated since 2016 are now hard-deprecated.
  They now raise `DeprecationWarning`s and will be removed in 2024.


### Added

- Official support for Python 3.11 and 3.12.
  No code changes were necessary.

- `argon2.exceptions.InvalidHashError` as a replacement for `InvalidHash`.

- *salt* parameter to `argon2.PasswordHasher.hash()` to allow for custom salts.
  This is only useful for specialized use-cases -- leave it on None unless you know exactly what you are doing.
  [#153](https://github.com/hynek/argon2-cffi/pull/153)


## [21.3.0](https://github.com/hynek/argon2-cffi/compare/21.2.0...21.3.0) - 2021-12-11

### Fixed

- While the last release added type hints, the fact that it's been missing a `py.typed` file made Mypy ignore them.
  [#113](https://github.com/hynek/argon2-cffi/pull/113)


## [21.2.0](https://github.com/hynek/argon2-cffi/compare/21.1.0...21.2.0) - 2021-12-08

### Removed

- Python 3.5 is not supported anymore.

- The CFFI bindings have been extracted into a separate project: [*argon2-cffi-bindings*]
  This makes *argon2-cffi* a Python-only project und should make it easier to contribute to and have more frequent releases with high-level features.

  This change is breaking for users who want to use a system-wide installation of Argon2 instead of our vendored code, because the argument to the ``--no-binary`` argument changed.
  Please refer to the [installation guide](https://argon2-cffi.readthedocs.io/en/stable/installation.html).


### Added

- Thanks to lots of work within [*argon2-cffi-bindings*], there're pre-compiled wheels for many new platforms.
  Including:
    - Apple Silicon via `universal2`
    - Linux on `amd64` and `arm64`
    - [*musl libc*](https://musl.libc.org) ([Alpine Linux!](https://www.alpinelinux.org)) on `i686`, `amd64`, and `arm64`
    - PyPy 3.8

  We hope to provide wheels for Windows on `arm64` soon, but are waiting for GitHub Actions to support that.

- `argon2.Parameters.from_parameters()` together with the `argon2.profiles` module that offers easy access to the RFC-recommended configuration parameters and then some.
  [#101](https://github.com/hynek/argon2-cffi/pull/101)
  [#110](https://github.com/hynek/argon2-cffi/pull/110)

- The CLI interface now has a `--profile` option that takes any name from `argon2.profiles`.

- Types!
  *argon2-cffi* is now fully typed.
  [#112](https://github.com/hynek/argon2-cffi/pull/112)


### Changed

- `argon2.PasswordHasher` now uses the RFC 9106 low-memory profile by default.
  The old defaults are available as `argon2.profiles.PRE_21_2`.


## [21.1.0](https://github.com/hynek/argon2-cffi/compare/20.1.0...21.1.0) - 2021-08-29

Vendoring Argon2 @ [62358ba](https://github.com/P-H-C/phc-winner-argon2/tree/62358ba2123abd17fccf2a108a301d4b52c01a7c) (20190702)

### Removed

- Microsoft stopped providing the necessary SDKs to ship Python 2.7 wheels and currently the downloads amount to 0.09%.
  Therefore we have decided that Python 2.7 is not supported anymore.


### Changed

- There are indeed no changes whatsoever to the code of *argon2-cffi*.
  The Argon2 project also hasn't tagged a new release since July 2019.
  There also don't seem to be any important pending fixes.

  This release is mainly about improving the way binary wheels are built (`abi3` on all platforms).


## [20.1.0](https://github.com/hynek/argon2-cffi/compare/19.2.0...20.1.0) - 2020-05-11

Vendoring Argon2 @ [62358ba](https://github.com/P-H-C/phc-winner-argon2/tree/62358ba2123abd17fccf2a108a301d4b52c01a7c) (20190702)


### Added

- It is now possible to manually override the detection of SSE2 using the `ARGON2_CFFI_USE_SSE2` environment variable.


## [19.2.0](https://github.com/hynek/argon2-cffi/compare/18.3.0...19.1.0) - 2019-10-27

Vendoring Argon2 @ [62358ba](https://github.com/P-H-C/phc-winner-argon2/tree/62358ba2123abd17fccf2a108a301d4b52c01a7c) (20190702)

### Removed

- Python 3.4 is not supported anymore. It has been unsupported by the Python core team for a while now and its PyPI downloads are negligible.

  It's very unlikely that *argon2-cffi* will break under 3.4 anytime soon, but we don't test it and don't ship binary wheels for it anymore.

### Fixed

- The dependency on `enum34` is now protected using a PEP 508 marker.
  This fixes problems when the sdist is handled by a different interpreter version than the one running it.
  [#48](https://github.com/hynek/argon2-cffi/issues/48)


## [19.1.0](https://github.com/hynek/argon2-cffi/compare/18.3.0...19.1.0) - 2019-01-17

Vendoring Argon2 @ [670229c](https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6) (20171227)

### Added

- Added support for Argon2 v1.2 hashes in `argon2.extract_parameters()`.


## [18.3.0](https://github.com/hynek/argon2-cffi/compare/18.2.0...18.3.0) - 2018-08-19

Vendoring Argon2 @ [670229c](https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6) (20171227)

### Added

- `argon2.PasswordHasher`'s hash type is configurable now.


## [18.2.0](https://github.com/hynek/argon2-cffi/compare/18.1.0...18.2.0) - 2018-08-19

Vendoring Argon2 @ [670229c](https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6) (20171227)

### Changed

- The hash type for `argon2.PasswordHasher` is Argon2**id** now.

  This decision has been made based on the recommendations in the latest [Argon2 RFC draft](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-argon2-04#section-4).
  [#33](https://github.com/hynek/argon2-cffi/issues/33)
  [#34](https://github.com/hynek/argon2-cffi/pull/34)

- Some of the hash parameters have been made stricter to be closer to said recommendations.
  The current goal for a hash verification times is around 50ms.
  [#41](https://github.com/hynek/argon2-cffi/pull/41)

### Added

- To make the change of hash type backward compatible, `argon2.PasswordHasher.verify()` now determines the type of the hash and verifies it accordingly.

- To allow for bespoke decisions about upgrading Argon2 parameters, it's now possible to extract them from a hash via the `argon2.extract_parameters()` function.
  [#41](https://github.com/hynek/argon2-cffi/pull/41)

- Additionally `argon2.PasswordHasher` now has a `check_needs_rehash()` method that allows to verify whether a hash has been created with the instance's parameters or whether it should be rehashed.
  [#41](https://github.com/hynek/argon2-cffi/pull/41)


## [18.1.0](https://github.com/hynek/argon2-cffi/compare/16.3.0...18.1.0) - 2018-01-06

Vendoring Argon2 @ [670229c](https://github.com/P-H-C/phc-winner-argon2/tree/670229c849b9fe882583688b74eb7dfdc846f9f6) (20171227)

### Added

- It is now possible to use the *argon2-cffi* bindings against an Argon2 library that is provided by the system.


## [16.3.0](https://github.com/hynek/argon2-cffi/compare/16.2.0...16.3.0) - 2016-11-10

Vendoring Argon2 @ [1c4fc41f81f358283755eea88d4ecd05e43b7fd3](https://github.com/P-H-C/phc-winner-argon2/tree/1c4fc41f81f358283755eea88d4ecd05e43b7fd3) (20161029)

### Added

- Add low-level bindings for Argon2id functions.

### Fixed

- Prevent side-effects like the installation of `cffi` if `setup.py` is called with a command that doesn't require it.
  [#20](https://github.com/hynek/argon2-cffi/pull/20)
- Fix a bunch of warnings with new `cffi` versions and Python 3.6.
  [#14](https://github.com/hynek/argon2-cffi/pull/14)
  [#16](https://github.com/hynek/argon2-cffi/issues/16)


## [16.2.0](https://github.com/hynek/argon2-cffi/compare/16.1.0...16.2.0) - 2016-09-10

Vendoring Argon2 @ [4844d2fee15d44cb19296ddf36029326d17c5aa3](https://github.com/P-H-C/phc-winner-argon2/tree/4844d2fee15d44cb19296ddf36029326d17c5aa3)

### Fixed

- Fixed compilation on Debian 8 (Jessie).
  [#13](https://github.com/hynek/argon2-cffi/pull/13)


## [16.1.0](https://github.com/hynek/argon2-cffi/compare/16.0.0...16.1.0) - 2016-04-19

Vendoring Argon2 @ [00aaa6604501fade85853a4b2f5695611ff6e7c5](https://github.com/P-H-C/phc-winner-argon2/tree/00aaa6604501fade85853a4b2f5695611ff6e7c5).

### Added

  - Add `VerifyMismatchError` that is raised if verification fails only because of a password/hash mismatch.
  It's a subclass of `VerificationError` therefore this change is completely backwards-compatible.

### Changed

- Add support for [Argon2 1.3](https://mailarchive.ietf.org/arch/msg/cfrg/beOzPh41Hz3cjl5QD7MSRNTi3lA/).
  Old hashes remain functional but opportunistic rehashing is strongly recommended.

### Removed

- Python 3.3 and 2.6 aren't supported anymore.
  They may work by chance but any support to them has been ceased.

  The last Python 2.6 release was on October 29, 2013 and isn't supported by the CPython core team anymore.
  Major Python packages like Django and Twisted dropped Python 2.6 a while ago already.

  Python 3.3 never had a significant user base and wasn't part of any distribution's LTS release.


## [16.0.0](https://github.com/hynek/argon2-cffi/compare/15.0.1...16.0.0) - 2016-01-02

Vendoring Argon2 @ [421dafd2a8af5cbb215e16da5953663eb101d139](https://github.com/P-H-C/phc-winner-argon2/tree/421dafd2a8af5cbb215e16da5953663eb101d139).

### Deprecated

- `hash_password()`, `hash_password_raw()`, and `verify_password()` should not be used anymore.
  For hashing passwords, use the new `argon2.PasswordHasher`.
  If you want to implement your own higher-level abstractions, use the new low-level APIs `hash_secret()`, `hash_secret_raw()`, and `verify_secret()` from the `argon2.low_level` module.
  If you want to go *really* low-level, `core()` is for you.
  The old functions will *not* raise any warnings though and there are *no* immediate plans to remove them.

### Added

- Added `argon2.PasswordHasher`.
  A higher-level class specifically for hashing passwords that also works on Unicode strings.
- Added `argon2.low_level` module with low-level API bindings for building own high-level abstractions.


## [15.0.1](https://github.com/hynek/argon2-cffi/compare/15.0.0...15.0.1) - 2015-12-18

Vendoring Argon2 @ [4fe0d8cda37691228dd5a96a310be57369403a4b](https://github.com/P-H-C/phc-winner-argon2/tree/4fe0d8cda37691228dd5a96a310be57369403a4b).

### Fixed

- Fix `long_description` on PyPI.


## [15.0.0](https://github.com/hynek/argon2-cffi/compare/15.0.0b5...15.0.0) - 2015-12-18

Vendoring Argon2 @ [4fe0d8cda37691228dd5a96a310be57369403a4b](https://github.com/P-H-C/phc-winner-argon2/tree/4fe0d8cda37691228dd5a96a310be57369403a4b).

### Added

- Conditionally use the [SSE2](https://en.wikipedia.org/wiki/SSE2)-optimized version of `argon2` on x86 architectures.

### Changed

- `verify_password()` doesn't guess the hash type if passed `None` anymore.
  Supporting this resulted in measurable overhead (~0.6ms vs 0.8ms on my notebook) since it had to happen in Python.
  That means that naïve usage of the API would give attackers an edge.
  The new behavior is that it has the same default value as `hash_password()` such that `verify_password(hash_password(b"password"), b"password")` still works.
- Tweaked default parameters to more reasonable values.
  Verification should take between 0.5ms and 1ms on recent-ish hardware.

### Fixed

- More packaging fixes.
  Most notably compilation on Visual Studio 2010 for Python 3.3 and 3.4.


## [15.0.0b5](https://github.com/hynek/argon2-cffi/tree/15.0.0b5) - 2015-12-10

Vendoring Argon2 @ [4fe0d8cda37691228dd5a96a310be57369403a4b](https://github.com/P-H-C/phc-winner-argon2/tree/4fe0d8cda37691228dd5a96a310be57369403a4b).

### Added

- Initial work.
  Previous betas were only for fixing Windows packaging.
  The authors of Argon2 were kind enough to [help me](https://github.com/P-H-C/phc-winner-argon2/issues/44) to get it building under Visual Studio 2008 that we’re forced to use for Python 2.7 on Windows.


[*argon2-cffi-bindings*]: https://github.com/hynek/argon2-cffi-bindings
