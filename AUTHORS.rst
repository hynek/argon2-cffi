Credits & License
=================

``argon2-cffi`` is maintained by Hynek Schlawack and released under the `MIT license <https://github.com/hynek/argon2-cffi/blob/main/LICENSE>`_.

The development is kindly supported by `Variomedia AG <https://www.variomedia.de/>`_.

A full list of contributors can be found in GitHub's `overview <https://github.com/hynek/argon2-cffi/graphs/contributors>`_.


Vendored Code
-------------

Argon2
^^^^^^

The original Argon2 repo can be found at https://github.com/P-H-C/phc-winner-argon2/.

Except for the components listed below, the Argon2 code in this repository is copyright (c) 2015 Daniel Dinu, Dmitry Khovratovich (main authors), Jean-Philippe Aumasson and Samuel Neves, and under CC0_ license.

The string encoding routines in src/encoding.c are copyright (c) 2015 Thomas Pornin, and under CC0_ license.

The `BLAKE2 <https://blake2.net>`_ code in ``src/blake2/`` is copyright (c) Samuel Neves, 2013-2015, and under CC0_ license.

The authors of Argon2 also were very helpful to get the library to compile on ancient versions of Visual Studio for ancient versions of Python.

The documentation also quotes frequently from the Argon2 paper_ to avoid mistakes by rephrasing.

.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _paper: https://password-hashing.net/argon2-specs.pdf
