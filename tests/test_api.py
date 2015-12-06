# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import binascii

import pytest

from hypothesis import given
from hypothesis import strategies as st

from argon2 import (
    hash_password, hash_password_raw, verify_password, Type,
    DEFAULT_RANDOM_SALT_LENGTH,
)
from argon2.exceptions import VerificationError, HashingError
from argon2._util import encoded_str_len

# Example data obtained using the official Argon2 CLI client:
#
# $ echo -n "password" | ./argon2 somesalt -t 2 -m 16 -p 4
# Type:       Argon2i
# Iterations: 2
# Memory:     65536 KiB
# Parallelism:    4
# Hash:       4162f32384d8f4790bd994cb73c83a4a29f076165ec18af3cfdcf10a8d1b9066
# Encoded:    $argon2i$m=65536,t=2,p=4$c29tZXNhbHQAAAAAAAAAAA$QWLzI4TY9HkL2ZTLc
#             8g6SinwdhZewYrzz9zxCo0bkGY
# 0.176 seconds
# Verification ok
#
# $ echo -n "password" | ./argon2 somesalt -t 2 -m 16 -p 4 -d
# Type:       Argon2d
# Iterations: 2
# Memory:     65536 KiB
# Parallelism:    4
# Hash:       9ca3b9fc007d09daf489dcf854e9a785ff5a32c62ec50acf26477977add23225
# Encoded:    $argon2d$m=65536,t=2,p=4$c29tZXNhbHQAAAAAAAAAAA$nKO5/AB9Cdr0idz4V
#             Omnhf9aMsYuxQrPJkd5d63SMiU
# 0.189 seconds
# Verification ok

TEST_HASH_I = (
    b"$argon2i$m=65536,t=2,p=4"
    b"$c29tZXNhbHQAAAAAAAAAAA"
    b"$QWLzI4TY9HkL2ZTLc8g6SinwdhZewYrzz9zxCo0bkGY"
)
TEST_HASH_D = (
    b"$argon2d$m=65536,t=2,p=4"
    b"$c29tZXNhbHQAAAAAAAAAAA$"
    b"nKO5/AB9Cdr0idz4VOmnhf9aMsYuxQrPJkd5d63SMiU"
)
TEST_RAW_I = binascii.unhexlify(
    b"4162f32384d8f4790bd994cb73c83a4a29f076165ec18af3cfdcf10a8d1b9066"
)
TEST_RAW_D = binascii.unhexlify(  # N.B. includes NUL byte!
    b"9ca3b9fc007d09daf489dcf854e9a785ff5a32c62ec50acf26477977add23225"
)
TEST_HASH_FAST = (
    b"$argon2i$m=8,t=1,p=1$c29tZXNhbHQAAAAAAAAAAA$owd7NH5aC7mrx3sIc0zMF+R8RkPH"
    b"S23ZuFM0IO3uck8"
)  # same password/salt, but much cheaper.

TEST_PASSWORD = b"password"
TEST_SALT_LEN = 16
TEST_SALT = b"somesalt"
TEST_SALT += b"\x00" * (TEST_SALT_LEN - len(TEST_SALT))
TEST_TIME = 2
TEST_MEMORY = 65536
TEST_PARALLELISM = 4
TEST_HASH_LEN = 32

i_and_d_encoded = pytest.mark.parametrize("type,hash", [
    (Type.I, TEST_HASH_I,),
    (Type.D, TEST_HASH_D,),
])
i_and_d_raw = pytest.mark.parametrize("type,hash", [
    (Type.I, TEST_RAW_I,),
    (Type.D, TEST_RAW_D,),
])


class TestHash(object):
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
            int(encoded_str_len(DEFAULT_RANDOM_SALT_LENGTH)) - 1 == len(salt)
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
    def test_auto_success(self, type, hash):
        """
        Given a valid hash and password, we figure out the type ourself and
        succeed.
        """
        assert True is verify_password(hash, TEST_PASSWORD)

    @i_and_d_encoded
    def test_explicit_success(self, type, hash):
        """
        Given a valid hash and password and correct type, we succeed.
        """
        assert True is verify_password(hash, TEST_PASSWORD, type)

    def test_explicit_fail(self):
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

    def test_auto_fast(self):
        """
        Just a test ensure that test_auto_fail works on correct data.
        """
        assert verify_password(TEST_HASH_FAST, b"password")

    @given(st.binary(max_size=128))
    def test_auto_fail(self, wrong_password):
        """
        Given a valid but wrong hash and password, we figure out the type
        ourself and fail.
        """
        with pytest.raises(VerificationError):
            verify_password(TEST_HASH_FAST, wrong_password)
