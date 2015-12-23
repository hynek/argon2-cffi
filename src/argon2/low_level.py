"""
Low-level functions if you want to build your own higher level abstractions.
"""

from __future__ import absolute_import, division, print_function

from ._util import (
    _error_to_str, ffi, lib, _get_encoded_len
)
from .exceptions import VerificationError, HashingError


__all__ = [
    "hash_secret",
    "hash_secret_raw",
    "verify_secret",
]


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
    buf = ffi.new("char[]", size)
    rv = lib.argon2_hash(
        time_cost, memory_cost, parallelism,
        ffi.new("char[]", secret), len(secret),
        ffi.new("char[]", salt), len(salt),
        ffi.NULL, hash_len,
        buf, size,
        type.value,
    )
    if rv != lib.ARGON2_OK:
        raise HashingError(_error_to_str(rv))

    return ffi.string(buf)


def hash_secret_raw(secret, salt, time_cost, memory_cost, parallelism,
                    hash_len, type):
    """
    Hash *password* and return a **raw** hash.

    This function takes the same parameters as :func:`hash_secret`.
    """
    buf = ffi.new("char[]", hash_len)

    rv = lib.argon2_hash(
        time_cost, memory_cost, parallelism,
        ffi.new("char[]", secret), len(secret),
        ffi.new("char[]", salt), len(salt),
        buf, hash_len,
        ffi.NULL, 0,
        type.value,
    )
    if rv != lib.ARGON2_OK:
        raise HashingError(_error_to_str(rv))

    return bytes(ffi.buffer(buf))


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
        ffi.new("char[]", hash),
        ffi.new("char[]", secret),
        len(secret),
        type.value,
    )
    if rv == lib.ARGON2_OK:
        return True
    else:
        raise VerificationError(_error_to_str(rv))
