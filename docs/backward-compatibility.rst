Backward Compatibility
======================

*argon2-cffi* has a very strong backward compatibility policy.
Generally speaking, you shouldn't ever be afraid of updating.

If breaking changes are needed do be done, they are:

#. …announced in the changelog_.
#. …the old behavior raises a :exc:`DeprecationWarning` for a year.
#. …are done with another announcement in the changelog_.

What explicitly *may* change over time are the default hashing parameters and the behavior of the :doc:`cli`.

.. _changelog: https://argon2-cffi.readthedocs.io/en/stable/changelog.html
