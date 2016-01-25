# -*- coding: utf-8 -*-
"""
Low-level functions if you want to build your own higher level abstractions.

.. warning::
    This is a "Hazardous Materials" module.  You should **ONLY** use it if
    you're 100% absolutely sure that you know what you’re doing because this
    module is full of land mines, dragons, and dinosaurs with laser guns.
"""

from __future__ import absolute_import, division, print_function

from enum import Enum

from six import PY3

from ._ffi import ffi, lib
from ._util import _get_encoded_len
from .exceptions import VerificationError, HashingError


__all__ = [
    "Type",
    "ffi",
    "hash_secret",
    "hash_secret_raw",
    "verify_secret",
]


class Type(Enum):
    """
    Enum of Argon2 variants.
    """
    D = lib.Argon2_d
    """
    Argon2\ **d** is faster and uses data-depending memory access, which makes
    it less suitable for hashing secrets and more suitable for cryptocurrencies
    and applications with no threats from side-channel timing attacks.
    """
    I = lib.Argon2_i
    """
    Argon2\ **i** uses data-independent memory access, which is preferred for
    password hashing and password-based key derivation.  Argon2i is slower as
    it makes more passes over the memory to protect from tradeoff attacks.
    """


def hash_secret(secret, salt, time_cost, memory_cost, parallelism, hash_len,
                type):
    """
    Hash *secret* and return an **encoded** hash.

    An encoded hash can be directly passed into :func:`verify_secret` as it
    contains all parameters and the salt.

    :param bytes secret: Secret to hash.
    :param bytes salt: A salt_.  Should be random and different for each
        secret.
    :param Type type: Which Argon2 variant to use.

    For an explanation of the Argon2 parameters see :class:`PasswordHasher`.

    :rtype: bytes

    :raises argon2.exceptions.HashingError: If hashing fails.

    .. versionadded:: 16.0.0

    .. _salt: https://en.wikipedia.org/wiki/Salt_(cryptography)
    .. _kibibytes: https://en.wikipedia.org/wiki/Binary_prefix#kibi
    """
    size = _get_encoded_len(hash_len, len(salt))
    buf = ffi.new("uint8_t[]", size)
    rv = lib.argon2_hash(
        time_cost, memory_cost, parallelism,
        ffi.new("uint8_t[]", secret), len(secret),
        ffi.new("uint8_t[]", salt), len(salt),
        ffi.NULL, hash_len,
        buf, size,
        type.value,
    )
    if rv != lib.ARGON2_OK:
        raise HashingError(error_to_str(rv))

    return ffi.string(buf)


def hash_secret_raw(secret, salt, time_cost, memory_cost, parallelism,
                    hash_len, type):
    """
    Hash *password* and return a **raw** hash.

    This function takes the same parameters as :func:`hash_secret`.
    """
    buf = ffi.new("uint8_t[]", hash_len)

    rv = lib.argon2_hash(
        time_cost, memory_cost, parallelism,
        ffi.new("uint8_t[]", secret), len(secret),
        ffi.new("uint8_t[]", salt), len(salt),
        buf, hash_len,
        ffi.NULL, 0,
        type.value,
    )
    if rv != lib.ARGON2_OK:
        raise HashingError(error_to_str(rv))

    return bytes(ffi.buffer(buf, hash_len))


def verify_secret(hash, secret, type):
    """
    Verify whether *secret* is correct for *hash* of *type*.

    :param bytes hash: An encoded Argon2 hash as returned by
        :func:`hash_secret`.
    :param bytes secret: The secret to verify whether it matches the one
        in *hash*.
    :param Type type: Type for *hash*.

    :raises argon2.exceptions.VerificationError: If verification fails.

    :return: ``True`` on success, raise
            :exc:`~argon2.exceptions.VerificationError` otherwise.
    :rtype: bool
    """
    rv = lib.argon2_verify(
        ffi.new("uint8_t[]", hash),
        ffi.new("uint8_t[]", secret),
        len(secret),
        type.value,
    )
    if rv == lib.ARGON2_OK:
        return True
    else:
        raise VerificationError(error_to_str(rv))


def core(context, type):
    """
    Direct binding to the ``argon2_ctx`` function.

    .. warning::
        This is a strictly advanced function working on raw C data structures.
        Both Argon2's and ``argon2_cffi``'s' higher-level bindings do a lot of
        sanity checks and housekeeping work that *you* are now responsible for
        (e.g. clearing buffers).

        Use at your own peril; ``argon2_cffi`` does *not* use this binding
        itself.

    :param context: A CFFI Argon2 context object (i.e. an ``struct
        Argon2_Context``/``argon2_context``).
    :param int type: Which Argon2 variant to use.  You can use the ``value``
        field of :class:`Type`'s fields.

    :rtype: int
    :return: An Argon2 error code.  Can be transformed into a string using
        :func:`error_to_str`.

    .. versionadded:: 16.0.0
    """
    return lib.argon2_ctx(context, type)


def error_to_str(error):
    """
    Convert an Argon2 error code into a native string.

    :param int error: An Argon2 error code as returned by :func:`core`.

    :rtype: str

    .. versionadded:: 16.0.0
    """
    msg = ffi.string(lib.argon2_error_message(error))
    if PY3:
        msg = msg.decode("ascii")
    return msg
