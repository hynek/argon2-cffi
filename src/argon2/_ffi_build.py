# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os
import sys

from cffi import FFI


include_dirs = [os.path.join("extras", "libargon2", "src")]

# Add vendored integer types headers.
if "win32" in str(sys.platform).lower():
    int_base = os.path.join("extras", "msinttypes")
    inttypes = os.path.join(int_base, "inttypes")
    stdint = os.path.join(int_base, "stdint")
    vi = sys.version_info[0:2]
    if vi in [(2, 6), (2, 7)]:
        # VS 2008 needs both.
        include_dirs += [inttypes, stdint]
    elif vi in [(3, 3), (3, 4)]:
        # VS 2010 needs only inttypes.h
        include_dirs += [inttypes]


ffi = FFI()
ffi.set_source(
    "_ffi", "#include <argon2.h>",
    include_dirs=include_dirs,
    libraries=["libargon2"],
)

ffi.cdef("""\
typedef enum Argon2_type { Argon2_d = 0, Argon2_i = 1 } argon2_type;

int argon2_hash(const uint32_t t_cost, const uint32_t m_cost,
                const uint32_t parallelism, const void *pwd,
                const size_t pwdlen, const void *salt, const size_t saltlen,
                void *hash, const size_t hashlen, char *encoded,
                const size_t encodedlen, argon2_type type);

int argon2_verify(const char *encoded, const void *pwd, const size_t pwdlen,
                  argon2_type type);

const char *error_message(int error_code);

/* Error codes */
typedef enum Argon2_ErrorCodes {
    ARGON2_OK = 0,

    ARGON2_OUTPUT_PTR_NULL = 1,

    ARGON2_OUTPUT_TOO_SHORT = 2,
    ARGON2_OUTPUT_TOO_LONG = 3,

    ARGON2_PWD_TOO_SHORT = 4,
    ARGON2_PWD_TOO_LONG = 5,

    ARGON2_SALT_TOO_SHORT = 6,
    ARGON2_SALT_TOO_LONG = 7,

    ARGON2_AD_TOO_SHORT = 8,
    ARGON2_AD_TOO_LONG = 9,

    ARGON2_SECRET_TOO_SHORT = 10,
    ARGON2_SECRET_TOO_LONG = 11,

    ARGON2_TIME_TOO_SMALL = 12,
    ARGON2_TIME_TOO_LARGE = 13,

    ARGON2_MEMORY_TOO_LITTLE = 14,
    ARGON2_MEMORY_TOO_MUCH = 15,

    ARGON2_LANES_TOO_FEW = 16,
    ARGON2_LANES_TOO_MANY = 17,

    ARGON2_PWD_PTR_MISMATCH = 18,    /* NULL ptr with non-zero length */
    ARGON2_SALT_PTR_MISMATCH = 19,   /* NULL ptr with non-zero length */
    ARGON2_SECRET_PTR_MISMATCH = 20, /* NULL ptr with non-zero length */
    ARGON2_AD_PTR_MISMATCH = 21,     /* NULL ptr with non-zero length */

    ARGON2_MEMORY_ALLOCATION_ERROR = 22,

    ARGON2_FREE_MEMORY_CBK_NULL = 23,
    ARGON2_ALLOCATE_MEMORY_CBK_NULL = 24,

    ARGON2_INCORRECT_PARAMETER = 25,
    ARGON2_INCORRECT_TYPE = 26,

    ARGON2_OUT_PTR_MISMATCH = 27,

    ARGON2_THREADS_TOO_FEW = 28,
    ARGON2_THREADS_TOO_MANY = 29,

    ARGON2_MISSING_ARGS = 30,

    ARGON2_ENCODING_FAIL = 31,

    ARGON2_DECODING_FAIL = 32,

    ARGON2_ERROR_CODES_LENGTH /* Do NOT remove; Do NOT add error codes after
                                 this
                                 error code */
} argon2_error_codes;
""")

if __name__ == '__main__':
    ffi.compile()
