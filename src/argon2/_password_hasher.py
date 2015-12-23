from __future__ import absolute_import, division, print_function

from ._api import (
    DEFAULT_HASH_LENGTH,
    DEFAULT_MEMORY_COST,
    DEFAULT_PARALLELISM,
    DEFAULT_TIME_COST,
    hash_password,
    verify_password,
)
from ._util import Type, _check_types


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

    Uses *always* Argon2\ **i** and a random salt.

    The reason for this being a class is both for convenience to carry
    parameters and to verify the parameters only *once*.   Any unnecessary
    slowdown when hashing is a tangible advantage for a brute force attacker.

    :param int time_cost: Defines the amount of computation realized and
        therefore the execution time, given in number of iterations.
    :param int memory_cost: Defines the memory usage, given in kibibytes_.
    :param int parallelism: Defines the number of parallel threads (*changes*
        the resulting hash value).
    :param int hash_len: Length of the hash in bytes.
    :param str encoding: The Argon2 C library expects bytes.  So if
        :meth:`hash` or :meth:`verify` are passed an unicode string, it will be
        encoded using this encoding.

    .. versionadded:: 16.0.0
    """
    __slots__ = [
        "time_cost", "memory_cost", "parallelism", "hash_len", "encoding",
    ]

    def __init__(
        self,
        time_cost=DEFAULT_TIME_COST,
        memory_cost=DEFAULT_MEMORY_COST,
        parallelism=DEFAULT_PARALLELISM,
        hash_len=DEFAULT_HASH_LENGTH,
        encoding="utf-8",
    ):
        e = _check_types(
            time_cost=(time_cost, int),
            memory_cost=(memory_cost, int),
            parallelism=(parallelism, int),
            hash_len=(hash_len, int),
            encoding=(encoding, str),
        )
        if e:
            raise TypeError(e)
        self.time_cost = time_cost
        self.memory_cost = memory_cost
        self.parallelism = parallelism
        self.hash_len = hash_len
        self.encoding = encoding

    def hash(self, password):
        """
        Hash *password* and return an encoded hash.

        :param password: Password to hash.
        :type password: ``bytes`` or ``unicode``

        :raises argon2.exceptions.HashingError: If hashing fails.

        :rtype: unicode
        """
        return hash_password(
            _ensure_bytes(password, self.encoding), None,
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

        :raises argon2.exceptions.VerificationError: If verification fails.

        :return: ``True`` on success, raise
            :exc:`~argon2.exceptions.VerificationError` otherwise.
        :rtype: bool
        """
        return verify_password(
            _ensure_bytes(hash, "ascii"),
            _ensure_bytes(password, self.encoding),
            Type.I,
        )
