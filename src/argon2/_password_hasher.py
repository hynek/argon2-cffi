from __future__ import absolute_import, division, print_function

import os

from .low_level import (
    Type,
    hash_secret,
    verify_secret,
)
from ._utils import _check_types


DEFAULT_RANDOM_SALT_LENGTH = 16
DEFAULT_HASH_LENGTH = 16
DEFAULT_TIME_COST = 2
DEFAULT_MEMORY_COST = 512
DEFAULT_PARALLELISM = 2


def _ensure_bytes(s, encoding):
    """
    Ensure *s* is a bytes string.  Encode using *encoding* if it isn't.
    """
    if isinstance(s, bytes):
        return s
    return s.encode(encoding)


class PasswordHasher(object):
    """
    High level class to hash passwords with sensible defaults.

    Uses *always* Argon2\ **i** and a random salt_.

    The reason for this being a class is both for convenience to carry
    parameters and to verify the parameters only *once*.   Any unnecessary
    slowdown when hashing is a tangible advantage for a brute force attacker.

    :param int time_cost: Defines the amount of computation realized and
        therefore the execution time, given in number of iterations.
    :param int memory_cost: Defines the memory usage, given in kibibytes_.
    :param int parallelism: Defines the number of parallel threads (*changes*
        the resulting hash value).
    :param int hash_len: Length of the hash in bytes.
    :param int salt_len: Length of random salt to be generated for each
        password.
    :param str encoding: The Argon2 C library expects bytes.  So if
        :meth:`hash` or :meth:`verify` are passed an unicode string, it will be
        encoded using this encoding.

    .. versionadded:: 16.0.0

    .. _salt: https://en.wikipedia.org/wiki/Salt_(cryptography)
    .. _kibibytes: https://en.wikipedia.org/wiki/Binary_prefix#kibi
    """
    __slots__ = [
        "time_cost", "memory_cost", "parallelism", "hash_len", "salt_len",
        "encoding",
    ]

    def __init__(
        self,
        time_cost=DEFAULT_TIME_COST,
        memory_cost=DEFAULT_MEMORY_COST,
        parallelism=DEFAULT_PARALLELISM,
        hash_len=DEFAULT_HASH_LENGTH,
        salt_len=DEFAULT_RANDOM_SALT_LENGTH,
        encoding="utf-8",
    ):
        e = _check_types(
            time_cost=(time_cost, int),
            memory_cost=(memory_cost, int),
            parallelism=(parallelism, int),
            hash_len=(hash_len, int),
            salt_len=(salt_len, int),
            encoding=(encoding, str),
        )
        if e:
            raise TypeError(e)
        self.time_cost = time_cost
        self.memory_cost = memory_cost
        self.parallelism = parallelism
        self.hash_len = hash_len
        self.salt_len = salt_len
        self.encoding = encoding

    def hash(self, password):
        """
        Hash *password* and return an encoded hash.

        :param password: Password to hash.
        :type password: ``bytes`` or ``unicode``

        :raises argon2.exceptions.HashingError: If hashing fails.

        :rtype: unicode
        """
        return hash_secret(
            secret=_ensure_bytes(password, self.encoding),
            salt=os.urandom(self.salt_len),
            time_cost=self.time_cost,
            memory_cost=self.memory_cost,
            parallelism=self.parallelism,
            hash_len=self.hash_len,
            type=Type.I,
        ).decode("ascii")

    def verify(self, hash, password):
        """
        Verify that *password* matches *hash*.

        :param unicode hash: An encoded hash as returned from
            :meth:`PasswordHasher.hash`.
        :param password: The password to verify.
        :type password: ``bytes`` or ``unicode``

        :raises argon2.exceptions.VerifyMismatchError: If verification fails
            because *hash* is not valid for *secret* of *type*.
        :raises argon2.exceptions.VerificationError: If verification fails for
            other reasons.

        :return: ``True`` on success, raise
            :exc:`~argon2.exceptions.VerificationError` otherwise.
        :rtype: bool

        .. versionchanged:: 16.1.0
            Raise :exc:`~argon2.exceptions.VerifyMismatchError` on mismatches
            instead of its more generic superclass.
        """
        return verify_secret(
            _ensure_bytes(hash, "ascii"),
            _ensure_bytes(password, self.encoding),
            Type.I,
        )
