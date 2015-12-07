# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import ctypes.util

from enum import Enum
from six import iteritems, PY3


from ._ffi import ffi
from .exceptions import InvalidHash


lib = ffi.dlopen(ctypes.util.find_library("argon2"))


class Type(Enum):
    D = lib.Argon2_d
    I = lib.Argon2_i


NoneType = type(None)


def check_types(**kw):
    """
    Check each ``name: (value, types)`` in *kw*.

    Returns a human-readable string of all violations or `None``.
    """
    errors = []
    for name, (value, types) in iteritems(kw):
        if not isinstance(value, types):
            if isinstance(types, tuple):
                types = ", or ".join(t.__name__ for t in types)
            else:
                types = types.__name__
            errors.append("'{name}' must be a {type} (got {actual})".format(
                name=name,
                type=types,
                actual=type(value).__name__,
            ))

    if errors != []:
        return ", ".join(errors) + "."


def error_to_str(error):
    """
    Convert an Argon2 error code into a native string.
    """
    msg = ffi.string(lib.error_message(error))
    if PY3:
        msg = msg.decode("ascii")
    return msg


def encoded_str_len(l):
    """
    Compute how long a byte string of length *l* becomes if encoded to hex.
    """
    return (l << 2) / 3 + 2


def get_encoded_len(hash_len, salt_len):
    """
    Compute the size of the required buffer for an encoded hash with *hash_len*
    and *salt_len*.
    """
    # From https://github.com/P-H-C/phc-winner-argon2/blob/master/src/run.c:
    #
    # Sample encode: $argon2i$m=65536,t=2,p=4$c29tZXNhbHQAAAAAAAAAAA$QWLzI4TY9H
    # kL2ZTLc8g6SinwdhZewYrzz9zxCo0bkGY
    # Maximumum lengths are defined as:
    # strlen $argon2i$ = 9
    # m=65536 with strlen (uint32_t)-1 = 10, so this total is 12
    # ,t=2,p=4 If we consider each number to potentially reach four digits
    # in future, this = 14
    # $c29tZXNhbHQAAAAAAAAAAA Formula for this is
    # (SALT_LEN * 4 + 3) / 3 + 1 = 23
    # $QWLzI4TY9HkL2ZTLc8g6SinwdhZewYrzz9zxCo0bkGY per above formula, = 44
    # + NULL byte
    # 9 + 12 + 14 + 23 + 44 + 1 = 103
    # Rounded to 4 byte boundary: 104
    return (
        39 + int(encoded_str_len(hash_len) + encoded_str_len(salt_len))
    ) & ~3


def guess_type(s):
    """
    Guesses what type of encoded Argon2 hash *s* is or raises InvalidHash.
    """
    prefix = s[:8]
    if prefix == b"$argon2i":
        return Type.I
    elif prefix == b"$argon2d":
        return Type.D
    else:
        raise InvalidHash(s)
