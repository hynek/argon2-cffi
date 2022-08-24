# Frequently Asked Questions

## I'm using *bcrypt* / *PBKDF2* / *scrypt* / *yescrypt*, do I need to migrate?

Using password hashes that aren't memory hard carries a certain risk but there's **no immediate danger or need for action**.
If however you are deciding how to hash password *today*, *Argon2* is the superior, future-proof choice.

But if you already use one of the hashes mentioned in the question, you should be fine for the foreseeable future.
If you're using *scrypt* or *yescrypt*, you will be probably fine for good.


## Why do the `verify()` methods raise an Exception instead of returning `False`?

1.  The *Argon2* library had no concept of a "wrong password" error in the beginning.
    Therefore when writing these bindings, an exception with the full error had to be raised so you could inspect what went actually wrong.

    Changing that now would be a very dangerous break of backwards-compatibility.

2.  In my opinion, a wrong password should raise an exception such that it can't pass unnoticed by accident.
    See also The Zen of Python: "Errors should never pass silently."

3.  It's more [Pythonic](https://docs.python.org/3/glossary.html#term-EAFP).
