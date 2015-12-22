# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from ._util import (
    _error_to_str, ffi, lib, _get_encoded_len, Type
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
    "core",
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
    :param int time_cost: Amount of computation realized and therefore the
        execution time, given in number of iterations.
    :param int memory_cost: Memory usage, given in kibibytes_.
    :param int parallelism: Number of parallel threads (*changes* the resulting
        hash value).
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
    if salt is None:
        salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)

    raw_buf = encoded_buf = ffi.NULL
    raw_len = encoded_len = 0
    if encoded:
        encoded_len = _get_encoded_len(hash_len, len(salt))
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
        raise HashingError(_error_to_str(rv))

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

    :return: ``True`` on success, raise
            :exc:`~argon2.exceptions.VerificationError` otherwise.
    :rtype: bool
    """
    rv = lib.argon2_verify(
        ffi.new("char[]", hash),
        ffi.new("char[]", password),
        len(password),
        type.value,
    )
    if rv == lib.ARGON2_OK:
        return True
    else:
        raise VerificationError(_error_to_str(rv))


def core(password,
         salt=None,
         secret=None,
         associated_data=None,
         time_cost=DEFAULT_TIME_COST,
         memory_cost=DEFAULT_MEMORY_COST,
         parallelism=DEFAULT_PARALLELISM,
         threads=None,
         hash_len=DEFAULT_HASH_LENGTH,
         type=Type.I):
    """
    Performs the core argon2 key-derivation.

        This function takes the same parameters as :func:`hash_password`
            and additionally the optional arguments

        :param bytes secret:
        :param bytes associated_data:
        :param int threads: actual maximum number of threads to spawn
        :rtype: bool
    """
    # Check parameters
    if salt is None:
        salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)
    if threads is None:
        threads = parallelism

    out_buf = ffi.new('char[]', hash_len)
    salt_buf = ffi.new('char[]', salt)

    # Set up context
    context = ffi.new('argon2_context *')
    context.out = out_buf
    context.outlen = hash_len
    context.pwd = ffi.new('char[]', password)
    context.pwdlen = len(password)
    context.salt = salt_buf
    context.saltlen = len(salt)
    context.t_cost = time_cost
    context.m_cost = memory_cost
    context.lanes = parallelism
    context.threads = threads
    context.allocate_cbk = ffi.NULL
    context.free_cbk = ffi.NULL
    context.flags = 4  # XXX

    if secret is None:
        context.secret = ffi.NULL
        context.secretlen = 0
    else:
        secretbuf = ffi.new('char[]', secret)
        context.secret = secretbuf
        context.secretlen = len(secret)

    if associated_data is None:
        context.ad = ffi.NULL
        context.adlen = 0
    else:
        adbuf = ffi.new('char[]', associated_data)
        context.ad = adbuf
        context.adlen = len(associated_data)

    # Run!
    rv = lib.argon2_core(context, type.value)
    if rv != lib.ARGON2_OK:
        raise HashingError(_error_to_str(rv))

    return bytes(ffi.buffer(out_buf))
