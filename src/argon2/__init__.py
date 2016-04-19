# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from . import exceptions, low_level
from ._legacy import (
    hash_password,
    hash_password_raw,
    verify_password,
)
from ._password_hasher import (
    DEFAULT_HASH_LENGTH,
    DEFAULT_MEMORY_COST,
    DEFAULT_PARALLELISM,
    DEFAULT_RANDOM_SALT_LENGTH,
    DEFAULT_TIME_COST,
    PasswordHasher,
)
from .low_level import Type


__version__ = "16.1.0.dev0"

__title__ = "argon2_cffi"
__description__ = "The secure Argon2 password hashing algorithm."
__uri__ = "https://argon2-cffi.readthedocs.org/"

__author__ = "Hynek Schlawack"
__email__ = "hs@ox.cx"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2015 {author}".format(author=__author__)


__all__ = [
    "DEFAULT_HASH_LENGTH",
    "DEFAULT_MEMORY_COST",
    "DEFAULT_PARALLELISM",
    "DEFAULT_RANDOM_SALT_LENGTH",
    "DEFAULT_TIME_COST",
    "PasswordHasher",
    "Type",
    "exceptions",
    "hash_password",
    "hash_password_raw",
    "hash_secret",
    "hash_secret_raw",
    "low_level",
    "verify_password",
    "verify_secret",
]
