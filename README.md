# Argon2 for Python

[![Documentation](https://img.shields.io/badge/Docs-Read%20The%20Docs-black)](https://argon2-cffi.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/license-MIT-C06524)](https://github.com/hynek/argon2-cffi/blob/main/LICENSE)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6671/badge)](https://bestpractices.coreinfrastructure.org/projects/6671)
[![PyPI version](https://img.shields.io/pypi/v/argon2-cffi)](https://pypi.org/project/argon2-cffi/)
[![Downloads / Month](https://static.pepy.tech/personalized-badge/argon2-cffi?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads%20/%20Month)](https://pepy.tech/project/argon2-cffi)

<!-- begin-short -->

[Argon2](https://github.com/p-h-c/phc-winner-argon2) won the [Password Hashing Competition](https://www.password-hashing.net/) and *argon2-cffi* is the simplest way to use it in Python:

```pycon
>>> from argon2 import PasswordHasher
>>> ph = PasswordHasher()
>>> hash = ph.hash("correct horse battery staple")
>>> hash  # doctest: +SKIP
'$argon2id$v=19$m=65536,t=3,p=4$MIIRqgvgQbgj220jfp0MPA$YfwJSVjtjSU0zzV/P3S9nnQ/USre2wvJMjfCIjrTQbg'
>>> ph.verify(hash, "correct horse battery staple")
True
>>> ph.check_needs_rehash(hash)
False
>>> ph.verify(hash, "Tr0ub4dor&3")
Traceback (most recent call last):
  ...
argon2.exceptions.VerifyMismatchError: The password does not match the supplied hash

```
<!-- end-short -->

## Project Links

- [**PyPI**](https://pypi.org/project/argon2-cffi/)
- [**GitHub**](https://github.com/hynek/argon2-cffi)
- [**Documentation**](https://argon2-cffi.readthedocs.io/)
- [**Changelog**](https://github.com/hynek/argon2-cffi/blob/main/CHANGELOG.md)
- The low-level Argon2 CFFI bindings are maintained in the separate [*argon2-cffi-bindings*](https://github.com/hynek/argon2-cffi-bindings) project.


## Credits

*argon2-cffi* is maintained by [Hynek Schlawack](https://hynek.me/).

The development is kindly supported by my employer [Variomedia AG](https://www.variomedia.de/), *argon2-cffi* [Tidelift subscribers](https://tidelift.com/subscription/pkg/pypi-argon2-cffi?utm_source=pypi-argon2-cffi&utm_medium=referral&utm_campaign=enterprise&utm_term=repo), and my amazing [GitHub Sponsors](https://github.com/sponsors/hynek).

A full list of contributors can be found in GitHub's [overview](https://github.com/hynek/argon2-cffi/graphs/contributors).


## *argon2-cffi* for Enterprise

Available as part of the Tidelift Subscription.

The maintainers of *argon2-cffi* and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open-source packages you use to build your applications.
Save time, reduce risk, and improve code health, while paying the maintainers of the exact packages you use.
[Learn more.](https://tidelift.com/subscription/pkg/pypi-argon2-cffi?utm_source=undefined&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)
