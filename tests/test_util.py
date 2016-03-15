# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from six import PY3

from argon2._util import _check_types, NoneType


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
            bytes=(u"not bytes", bytes),
            str_or_None=(42, (str, NoneType))
        )

        assert "." == rv[-1]  # proper grammar FTW
        assert "'str_or_None' must be a str, or NoneType (got int)" in rv

        if PY3:
            assert "'bytes' must be a bytes (got str)" in rv
        else:
            assert "'bytes' must be a str (got unicode)" in rv
