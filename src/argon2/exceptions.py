# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Argon2Error(Exception):
    """
    Superclass of all argon2 exceptions.

    Never thrown directly.
    """


class VerificationError(Argon2Error):
    """
    Raised if verification failed.
    """


class InvalidHash(VerificationError):
    """
    Raised if :func:`argon2.verify_password` should guess the type of a hash
    but the hash is invalid.
    """


class HashingError(Argon2Error):
    """
    Raised if hasing failed.
    """
