# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from base64 import b64encode

import pytest

from hypothesis import given
from hypothesis import strategies as st
from six import PY3

from argon2 import Parameters, Type, extract_parameters
from argon2._utils import NoneType, _check_types, _decoded_str_len
from argon2.exceptions import InvalidHash


class TestCheckTypes(object):
    def test_success(self):
        """
        Returns None if all types are okay.
        """
        assert None is _check_types(
            bytes=(b"bytes", bytes),
            tuple=((1, 2), tuple),
            str_or_None=(None, (str, NoneType)),
        )

    def test_fail(self):
        """
        Returns summary of failures.
        """
        rv = _check_types(
            bytes=(u"not bytes", bytes), str_or_None=(42, (str, NoneType))
        )

        assert "." == rv[-1]  # proper grammar FTW
        assert "'str_or_None' must be a str, or NoneType (got int)" in rv

        if PY3:
            assert "'bytes' must be a bytes (got str)" in rv
        else:
            assert "'bytes' must be a str (got unicode)" in rv


@given(st.binary())
def test_decoded_str_len(bs):
    """
    _decoded_str_len computes the resulting length.
    """
    assert len(bs) == _decoded_str_len(len(b64encode(bs).rstrip(b"=")))


VALID_HASH = (
    "$argon2id$v=19$m=65536,t=2,p=4$"
    "c29tZXNhbHQ$GpZ3sK/oH9p7VIiV56G/64Zo/8GaUw434IimaPqxwCo"
)
VALID_PARAMETERS = Parameters(
    type=Type.ID,
    salt_len=8,
    hash_len=32,
    version=19,
    memory_cost=65536,
    time_cost=2,
    parallelism=4,
)


class TestExtractParameters(object):
    def test_valid_hash(self):
        """
        A valid hash is parsed.
        """
        parsed = extract_parameters(VALID_HASH)

        assert VALID_PARAMETERS == parsed

    @pytest.mark.parametrize(
        "hash",
        [
            "",
            "abc" + VALID_HASH,
            VALID_HASH.replace("p=4", "p=four"),
            VALID_HASH.replace(",p=4", ""),
        ],
    )
    def test_invalid_hash(self, hash):
        """
        Invalid hashes of various types raise an InvalidHash error.
        """
        with pytest.raises(InvalidHash):
            extract_parameters(hash)


class TestParameters(object):
    def test_eq(self):
        """
        Parameters are iff every attribute is equal.
        """
        assert VALID_PARAMETERS == VALID_PARAMETERS
        assert not VALID_PARAMETERS != VALID_PARAMETERS

    def test_eq_wrong_type(self):
        """
        Parameters are only compared if they have the same type.
        """
        assert VALID_PARAMETERS != "foo"
        assert not VALID_PARAMETERS == object()

    def test_repr(self):
        """
        __repr__ returns s ensible string.
        """
        assert (
            "<Parameters(type=<Type.ID: 2>, version=19, hash_len=32, "
            "salt_len=8, time_cost=2, memory_cost=65536, parallelelism=4)>"
            == repr(
                Parameters(
                    type=Type.ID,
                    salt_len=8,
                    hash_len=32,
                    version=19,
                    memory_cost=65536,
                    time_cost=2,
                    parallelism=4,
                )
            )
        )
