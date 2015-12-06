# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import argparse
import os
import sys
import timeit

import six

from . import (
    hash_password,
    DEFAULT_RANDOM_SALT_LENGTH,
    DEFAULT_TIME_COST,
    DEFAULT_MEMORY_COST,
    DEFAULT_PARALLELISM,
    DEFAULT_HASH_LENGTH,
    Type,
)


def main(argv):
    parser = argparse.ArgumentParser(description="Benchmark Argon2.")
    parser.add_argument("-n", type=int, default=100,
                        help="Number of iterations to measure.")
    parser.add_argument("-d", action="store_const",
                        const=Type.D, default=Type.I,
                        help="Use Argon2d instead of the default Argon2i.")
    parser.add_argument("-t", type=int, help="`time_cost`",
                        default=DEFAULT_TIME_COST)
    parser.add_argument("-m", type=int, help="`memory_cost`",
                        default=DEFAULT_MEMORY_COST)
    parser.add_argument("-p", type=int, help="`parallellism`",
                        default=DEFAULT_PARALLELISM)
    parser.add_argument("-l", type=int, help="`hash_length`",
                        default=DEFAULT_HASH_LENGTH)

    args = parser.parse_args(argv[1:])

    password = b"secret"
    salt = os.urandom(DEFAULT_RANDOM_SALT_LENGTH)

    hash = hash_password(
        password, salt,
        time_cost=args.t,
        memory_cost=args.m,
        parallelism=args.p,
        type=args.d,
        hash_len=args.l,
    )

    params = {
        "time_cost": args.t,
        "memory_cost": args.m,
        "parallelism": args.p,
        "hash_len": args.l,
    }

    print("Running Argon2{0} {1} times with:".format(
        Type(args.d).name.lower(),
        args.n,
    ))

    for k, v in sorted(six.iteritems(params)):
        print("{0}: {1}".format(k, v))

    print("\nMeasuring...")
    duration = timeit.timeit(
        "verify_password({hash!r}, {password!r})".format(
            hash=hash, password=password
        ),
        setup="from argon2 import verify_password; gc.enable()",
        number=args.n,
    )
    print("\n{0:.3}ms per password".format(duration / args.n * 1000))


if __name__ == "__main__":
    main(sys.argv)
