# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest
import six

from argon2 import PasswordHasher
from argon2._password_hasher import _ensure_bytes


class TestEnsureBytes(object):
    def test_is_bytes(self):
        """
        Bytes are just returned.
        """
        s = u"föö".encode("utf-8")

        rv = _ensure_bytes(s, "doesntmatter")

        assert isinstance(rv, bytes)
        assert s == rv

    def test_is_unicode(self):
        """
        Unicode is encoded using the specified encoding.
        """
        s = u"föö"

        rv = _ensure_bytes(s, "latin1")

        assert isinstance(rv, bytes)
        assert s.encode("latin1") == rv


bytes_and_unicode_password = pytest.mark.parametrize("password", [
    u"pässword".encode("latin1"),
    u"pässword",
])


class TestPasswordHasher(object):
    @bytes_and_unicode_password
    def test_hash(self, password):
        """
        Hashing works with unicode and bytes.  Uses correct parameters.
        """
        ph = PasswordHasher(1, 8, 1, 16, "latin1")

        h = ph.hash(password)

        assert isinstance(h, six.text_type)
        assert h[:21] == u"$argon2i$m=8,t=1,p=1$"

    @bytes_and_unicode_password
    def test_verify(self, password):
        """
        Verification works with unicode and bytes.
        """
        ph = PasswordHasher(1, 8, 1, 16, "latin1")
        hash = (  # handrolled artisanal test vector
            u"$argon2i$m=8,t=1,p=1$"
            u"bL/lLsegFKTuR+5vVyA8tA$VKz5CHavCtFOL1N5TIXWSA"
        )

        assert ph.verify(hash, password)

    def test_check(self):
        """
        Raises a helpful TypeError on wrong arguments.
        """
        with pytest.raises(TypeError) as e:
            PasswordHasher("1")

        assert "'time_cost' must be a int (got str)." == e.value.args[0]
