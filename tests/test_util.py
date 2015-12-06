# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from six import PY3

import pytest

from hypothesis import given
from hypothesis import strategies as st

from argon2.exceptions import InvalidHash
from argon2._util import get_encoded_len, check_types, NoneType, guess_type

from .test_api import i_and_d_encoded


def test_get_encoded_len():
    """
    Verify we get the same result as the official example.
    """
    assert 104 == get_encoded_len(32, 16)


class TestCheckTypes(object):
    def test_success(self):
        """
        Returns None if all types are okay.
        """
        assert None is check_types(
            bytes=(b"bytes", bytes),
            tuple=((1, 2), tuple),
            str_or_None=(None, (str, NoneType)),
        )

    def test_fail(self):
        """
        Returns summary of failures.
        """
        rv = check_types(
            bytes=(u"not bytes", bytes),
            str_or_None=(42, (str, NoneType))
        )

        assert "." == rv[-1]  # proper grammar FTW
        assert "'str_or_None' must be a str, or NoneType (got int)" in rv

        if PY3:
            assert "'bytes' must be a bytes (got str)" in rv
        else:
            assert "'bytes' must be a str (got unicode)" in rv


class TestGuessType(object):
    @i_and_d_encoded
    def test_success(self, type, hash):
        """
        Returns Type.I on likely Argon2i hashes.
        """
        assert type is guess_type(hash)

    @given(st.binary(max_size=128))
    def test_fail(self, wrong_hash):
        """
        If the hash can't be neither i nor d, raise InvalidHash.
        """
        with pytest.raises(InvalidHash):
            guess_type(wrong_hash)
