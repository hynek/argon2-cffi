# Installation

## Using a Vendored Argon2

```console
$ python -Im pip install argon2-cffi
```

should be all it takes.

But since *argon2-cffi* depends on [argon2-cffi-bindings] that vendors Argon2's C code by default, it can lead to complications depending on the platform.

The C code is known to compile and work on all common platforms (including x86, ARM, and PPC).
On x86, an [SSE2]-optimized version is used.

If something goes wrong, please try to update your *cffi*, *pip* and *setuptools* packages first:

```console
$ python -Im pip install -U cffi pip setuptools
```

Overall this should be the safest bet because *argon2-cffi* has been specifically tested against the vendored version.


### Wheels

Binary [wheels](https://pythonwheels.com) for macOS, Windows, and Linux are provided on [PyPI] by [argon2-cffi-bindings].
With a recent-enough *pip* and *setuptools*, they should be used automatically.


### Source Distribution

A working C compiler and [CFFI environment] are required to build the [argon2-cffi-bindings] dependency.
If you've been able to compile Python CFFI extensions before, *argon2-cffi* should install without any problems.


## Using a System-wide Installation of Argon2

If you set `ARGON2_CFFI_USE_SYSTEM` to `1` (and *only* `1`), *argon2-cffi-bindings* will not build its bindings.
However binary wheels are preferred by *pip* and Argon2 gets installed along with *argon2-cffi* anyway.

Therefore you also have to instruct *pip* to use a source distribution of [argon2-cffi-bindings]:

```console
$ env ARGON2_CFFI_USE_SYSTEM=1 \
    python -m pip install --no-binary=argon2-cffi-bindings argon2-cffi
```

This approach can lead to problems around your build chain and you can run into incompatibilities between Argon2 and *argon2-cffi* if the latter has been tested against a different version.

**It is your own responsibility to deal with these risks if you choose this path.**

Available since version 18.1.0.
The `--no-binary` option value changed in 21.2.0 due to the outsourcing of the binary bindings.


## Override Automatic SSE2 Detection

Usually the build process tries to guess whether or not it should use [SSE2]-optimized code.
Despite our best efforts, this can go wrong.

Therefore you can use the `ARGON2_CFFI_USE_SSE2` environment variable to control the process:

- If you set it to `1`, *argon2-cffi* will build **with** SSE2 support.
- If you set it to `0`, *argon2-cffi* will build **without** SSE2 support.
- If you set it to anything else, it will be ignored and *argon2-cffi* will try to guess.

Available since version 20.1.0.

[argon2-cffi-bindings]: https://github.com/hynek/argon2-cffi-bindings
[cffi environment]: https://cffi.readthedocs.io/en/latest/installation.html
[pypi]: https://pypi.org/project/argon2-cffi-bindings/
[sse2]: https://en.wikipedia.org/wiki/SSE2
