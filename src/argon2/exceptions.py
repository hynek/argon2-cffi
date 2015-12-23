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

    You can find the original error message from Argon2 in ``args[0]``.
    """


class HashingError(Argon2Error):
    """
    Raised if hashing failed.

    You can find the original error message from Argon2 in ``args[0]``.
    """
