# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from ._util import (
    check_types, error_to_str, ffi, lib, get_encoded_len, Type, NoneType,
)
from .exceptions import VerificationError, HashingError


__all__ = [
    "DEFAULT_HASH_LENGTH",
    "DEFAULT_MEMORY_COST",
    "DEFAULT_PARALLELISM",
    "DEFAULT_RANDOM_SALT_LENGTH",
    "DEFAULT_TIME_COST",
    "hash_password",
    "hash_password_raw",
    "verify_password",
]

DEFAULT_RANDOM_SALT_LENGTH = 16
DEFAULT_HASH_LENGTH = 16
DEFAULT_TIME_COST = 2
DEFAULT_MEMORY_COST = 512
DEFAULT_PARALLELISM = 2


def hash_password(password, salt=None,
                  time_cost=DEFAULT_TIME_COST,
                  memory_cost=DEFAULT_MEMORY_COST,
                  parallelism=DEFAULT_PARALLELISM,
                  hash_len=DEFAULT_HASH_LENGTH,
                  type=Type.I):
    """
    Hash *password* and return an **encoded** hash.

    An encoded hash can be directly passed into :func:`verify_password` as it
    contains all parameters and the salt.

    :param bytes password: Password to hash.
    :param bytes salt: A salt_.  Should be random and different for each
        password.  Will generate a random salt for you if left ``None``
        (recommended).
    :param int time_cost: Defines the amount of computation realized and
        therefore the execution time, given in number of iterations.
    :param int memory_cost: Defines the memory usage, given in kibibytes_.
    :param int parallelism: Defines the number of parallel threads (*changes*
        the resulting hash value).
    :param int hash_len: Length of the hash in bytes.
    :param Type type: Which Argon2 variant to use.  In doubt use the default
        :attr:`Type.I` which is better suited for passwords.

    :rtype: bytes

    .. _salt: https://en.wikipedia.org/wiki/Salt_(cryptography)
    .. _kibibytes: https://en.wikipedia.org/wiki/Binary_prefix#kibi
    """
    return _hash(password, salt, time_cost, memory_cost, parallelism, hash_len,
                 type, True)


def hash_password_raw(password, salt=None,
                      time_cost=DEFAULT_TIME_COST,
                      memory_cost=DEFAULT_MEMORY_COST,
                      parallelism=DEFAULT_PARALLELISM,
                      hash_len=DEFAULT_HASH_LENGTH,
                      type=Type.I):
    """
    Hash *password* and return a **raw** hash.

    This function takes the same parameters as :func:`hash_password`.
    """
    return _hash(password, salt, time_cost, memory_cost, parallelism, hash_len,
                 type, False)


def _hash(password, salt, time_cost, memory_cost, parallelism, hash_len, type,
          encoded):
    e = check_types(
        password=(password, bytes),
        salt=(salt, (bytes, NoneType)),
        time_cost=(time_cost, int),
        memory_cost=(memory_cost, int),
        parallelism=(parallelism, int),
        hash_len=(hash_len, int),
        type=(type, Type),
        encoded=(encoded, bool),
    )
    if e:
        raise TypeError(e)
    if salt is None:
        salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)

    raw_buf = encoded_buf = ffi.NULL
    raw_len = encoded_len = 0
    if encoded:
        encoded_len = get_encoded_len(hash_len, len(salt))
        encoded_buf = ffi.new("char[]", encoded_len)
    else:
        raw_len = hash_len
        raw_buf = ffi.new("char[]", raw_len)

    rv = lib.argon2_hash(
        time_cost, memory_cost, parallelism,
        ffi.new("char[]", password), len(password),
        ffi.new("char[]", salt), len(salt),
        raw_buf, hash_len,
        encoded_buf, encoded_len,
        type.value,
    )
    if rv != lib.ARGON2_OK:
        raise HashingError(error_to_str(rv))

    return (
        ffi.string(encoded_buf) if encoded_len != 0
        else bytes(ffi.buffer(raw_buf))
    )


def verify_password(hash, password, type=Type.I):
    """
    Verify whether *password* is correct for *hash* of *type*.

    :param bytes hash: An encoded Argon2 password hash as returned by
        :func:`hash_password`.
    :param bytes password: The password to verify whether it matches the one
        in *hash*.
    :param Type type: Type for *hash*.

    :return: ``True`` on success, throw exception otherwise.
    :rtype: bool
    """
    e = check_types(
        password=(password, bytes),
        hash=(hash, bytes),
        type=(type, Type),
    )
    if e:
        raise TypeError(e)

    rv = lib.argon2_verify(
        ffi.new("char[]", hash),
        ffi.new("char[]", password),
        len(password),
        type.value,
    )
    if rv == lib.ARGON2_OK:
        return True
    else:
        raise VerificationError(error_to_str(rv))
