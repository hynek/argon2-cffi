Credits
=======

``argon2_cffi`` is written and maintained by Hynek Schlawack.

The development is kindly supported by `Variomedia AG <https://www.variomedia.de/>`_.

A full list of contributors can be found on `GitHub <https://github.com/hynek/argon2_cffi/graphs/contributors>`_.


Vendored Code
-------------

Argon2
^^^^^^

The original Argon2 repo can be found at https://github.com/P-H-C/phc-winner-argon2/.

Except for the components listed below, the Argon2 code in this repository is copyright (c) 2015 Daniel Dinu, Dmitry Khovratovich (main authors), Jean-Philippe Aumasson and Samuel Neves, and under CC0 license.

The string encoding routines in src/encoding.c are copyright (c) 2015 Thomas Pornin, and under CC0 license.

The BLAKE2 code in src/blake2/ is copyright (c) Samuel Neves, 2013-2015, and under CC0 license.


msinttypes
^^^^^^^^^^

In order to be able to compile on Visual Studio 2008 which is required for Python 2.7, we also ship two headers with integer types.
They are from the `msinttypes project <https://code.google.com/p/msinttypes/>`_ (`auto-import on GitHub <https://github.com/chemeris/msinttypes>`_) and licensed under New BSD:

Copyright (c) 2006-2013 Alexander Chemeris

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  3. Neither the name of the product nor the names of its contributors may
     be used to endorse or promote products derived from this software
     without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
