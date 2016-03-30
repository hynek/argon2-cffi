# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


from six import iteritems


NoneType = type(None)


def _check_types(**kw):
    """
    Check each ``name: (value, types)`` in *kw*.

    Returns a human-readable string of all violations or `None``.
    """
    errors = []
    for name, (value, types) in iteritems(kw):
        if not isinstance(value, types):
            if isinstance(types, tuple):
                types = ", or ".join(t.__name__ for t in types)
            else:
                types = types.__name__
            errors.append("'{name}' must be a {type} (got {actual})".format(
                name=name,
                type=types,
                actual=type(value).__name__,
            ))

    if errors != []:
        return ", ".join(errors) + "."


def _encoded_str_len(l):
    """
    Compute how long a byte string of length *l* becomes if encoded to hex.
    """
    return (l << 2) / 3 + 2
