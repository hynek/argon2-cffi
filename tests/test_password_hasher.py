# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest
import six

from argon2 import PasswordHasher
from argon2._password_hasher import _ensure_bytes
from argon2.exceptions import InvalidHash


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
        ph = PasswordHasher(1, 8, 1, 16, 16, "latin1")

        h = ph.hash(password)

        prefix = u"$argon2id$v=19$m=8,t=1,p=1$"

        assert isinstance(h, six.text_type)
        assert h[:len(prefix)] == prefix

    @bytes_and_unicode_password
    def test_verify_agility(self, password):
        """
        Verification works with unicode and bytes and variant is correctly
        detected.
        """
        ph = PasswordHasher(1, 8, 1, 16, 16, "latin1")
        hash = (  # handrolled artisanal test vector
            u"$argon2i$m=8,t=1,p=1$"
            u"bL/lLsegFKTuR+5vVyA8tA$VKz5CHavCtFOL1N5TIXWSA"
        )

        assert ph.verify(hash, password)

    @bytes_and_unicode_password
    def test_hash_verify(self, password):
        """
        Hashes are valid and can be verified.
        """
        ph = PasswordHasher()

        assert ph.verify(ph.hash(password), password) is True

    def test_check(self):
        """
        Raises a helpful TypeError on wrong arguments.
        """
        with pytest.raises(TypeError) as e:
            PasswordHasher("1")

        assert "'time_cost' must be a int (got str)." == e.value.args[0]

    def test_verify_invalid_hash(self):
        """
        If the hash can't be parsed, InvalidHash is raised.
        """
        with pytest.raises(InvalidHash):
            PasswordHasher().verify("tiger", "does not matter")
