# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from ._util import (
    check_types, error_to_str, guess_type, ffi, lib, get_encoded_len, Type,
    NoneType,
)
from .exceptions import VerificationError, HashingError


__all__ = [
    "DEFAULT_RANDOM_SALT_LENGTH",
    "hash_password",
    "hash_password_raw",
    "verify_password",
]

DEFAULT_RANDOM_SALT_LENGTH = 16
DEFAULT_HASH_LENGTH = 16
DEFAULT_TIME_COST = 3
DEFAULT_MEMORY_COST = 2**12
DEFAULT_PARALLELISM = 2


def hash_password(password, salt=None,
                  time_cost=DEFAULT_TIME_COST,
                  memory_cost=DEFAULT_MEMORY_COST,
                  parallelism=DEFAULT_PARALLELISM,
                  hash_len=DEFAULT_HASH_LENGTH,
                  type=Type.I):
    return _hash(password, salt, time_cost, memory_cost, parallelism, hash_len,
                 type, True)


def hash_password_raw(password, salt=None,
                      time_cost=DEFAULT_TIME_COST,
                      memory_cost=DEFAULT_MEMORY_COST,
                      parallelism=DEFAULT_PARALLELISM,
                      hash_len=DEFAULT_HASH_LENGTH,
                      type=Type.I):
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


def verify_password(hash, password, type=None):
    """
    Verify whether *password* is correct for *hash* of *type*.

    :return: ``True`` on success, throw exception otherwise.
    :rtype: bool
    """
    e = check_types(
        password=(password, bytes),
        hash=(hash, bytes),
        type=(type, (Type, NoneType)),
    )
    if e:
        raise TypeError(e)

    if type is None:
        type = guess_type(hash)

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
