# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from . import exceptions
from ._util import Type
from ._api import (
    DEFAULT_HASH_LENGTH,
    DEFAULT_MEMORY_COST,
    DEFAULT_PARALLELISM,
    DEFAULT_RANDOM_SALT_LENGTH,
    DEFAULT_TIME_COST,
    hash_password,
    hash_password_raw,
    verify_password,
    core,
)
from ._password_hasher import PasswordHasher


__version__ = "16.0.0.dev0"

__title__ = "argon2_cffi"
__description__ = "The secure Argon2 password hashing algorithm."
__uri__ = "https://argon2-cffi.readthedocs.org"

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
    "verify_password",
    "core",
]
