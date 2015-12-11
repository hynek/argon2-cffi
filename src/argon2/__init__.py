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
)


__version__ = "15.0.0b6"

__title__ = "argon2_cffi"
__description__ = "argon2 password hashing algorithm."
__uri__ = ""

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
    "Type",
    "exceptions",
    "hash_password",
    "hash_password_raw",
    "verify_password",
]
