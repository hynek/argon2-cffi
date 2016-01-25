# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest

from hypothesis import given
from hypothesis import strategies as st

from argon2 import (
    hash_password, hash_password_raw, verify_password, Type,
    DEFAULT_RANDOM_SALT_LENGTH,
)
from argon2.exceptions import VerificationError, HashingError
from argon2._util import _encoded_str_len

from .test_low_level import (
    TEST_PASSWORD,
    TEST_SALT,
    TEST_TIME,
    TEST_MEMORY,
    TEST_PARALLELISM,
    TEST_HASH_LEN,
    TEST_HASH_I,
    i_and_d_encoded,
    i_and_d_raw,
)


class TestHash(object):
    def test_hash_defaults(self):
        """
        Calling without arguments works.
        """
        hash_password(b"secret")

    def test_raw_defaults(self):
        """
        Calling without arguments works.
        """
        hash_password_raw(b"secret")

    @i_and_d_encoded
    def test_hash_password(self, type, hash):
        """
        Creates the same encoded hash as the Argon2 CLI client.
        """
        rv = hash_password(
            TEST_PASSWORD,
            TEST_SALT,
            TEST_TIME,
            TEST_MEMORY,
            TEST_PARALLELISM,
            TEST_HASH_LEN,
            type,
        )

        assert hash == rv
        assert isinstance(rv, bytes)

    @i_and_d_raw
    def test_hash_password_raw(self, type, hash):
        """
        Creates the same raw hash as the Argon2 CLI client.
        """
        rv = hash_password_raw(
            TEST_PASSWORD,
            TEST_SALT,
            TEST_TIME,
            TEST_MEMORY,
            TEST_PARALLELISM,
            TEST_HASH_LEN,
            type,
        )

        assert hash == rv
        assert isinstance(rv, bytes)

    def test_hash_nul_bytes(self):
        """
        Hashing passwords with NUL bytes works as expected.
        """
        rv = hash_password_raw(b"abc\x00", TEST_SALT)

        assert rv != hash_password_raw(b"abc", TEST_SALT)

    def test_random_salt(self):
        """
        Omitting a salt, creates a random one.
        """
        rv = hash_password(b"secret")
        salt = rv.split(b",")[-1].split(b"$")[1]
        assert (
            # -1 for not NUL byte
            int(_encoded_str_len(DEFAULT_RANDOM_SALT_LENGTH)) - 1 == len(salt)
        )

    def test_hash_wrong_arg_type(self):
        """
        Passing an argument of wrong type raises TypeError.
        """
        with pytest.raises(TypeError):
            hash_password(u"oh no, unicode!")

    def test_illegal_argon2_parameter(self):
        """
        Raises HashingError if hashing fails.
        """
        with pytest.raises(HashingError):
            hash_password(TEST_PASSWORD, memory_cost=1)

    @given(st.binary(max_size=128))
    def test_hash_fast(self, password):
        """
        Hash various passwords as cheaply as possible.
        """
        hash_password(
            password,
            salt=b"12345678",
            time_cost=1,
            memory_cost=8,
            parallelism=1,
            hash_len=8,
        )


class TestVerify(object):
    @i_and_d_encoded
    def test_success(self, type, hash):
        """
        Given a valid hash and password and correct type, we succeed.
        """
        assert True is verify_password(hash, TEST_PASSWORD, type)

    def test_fail_wrong_argon2_type(self):
        """
        Given a valid hash and password and wrong type, we fail.
        """
        with pytest.raises(VerificationError):
            verify_password(TEST_HASH_I, TEST_PASSWORD, Type.D)

    def test_wrong_arg_type(self):
        """
        Passing an argument of wrong type raises TypeError.
        """
        with pytest.raises(TypeError):
            verify_password(TEST_HASH_I, TEST_PASSWORD.decode("ascii"))
