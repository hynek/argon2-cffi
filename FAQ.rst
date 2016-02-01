Frequently Asked Questions
==========================

I'm using ``bcrypt``/``scrypt``/``PBKDF2``, do I need to migrate?
  Using password hashes that aren't memory hard carries a certain risk but there's **no immediate danger or need for action**.
  If however you are deciding how to hash password *today*, pick Argon2 because it's a superior, future-proof choice.

  But if you already use one of the hashes mentioned in the question, you should be fine for the foreseeable future.

Why do the ``verify()`` methods raise an Exception instead of returning ``False``?
   #. The Argon2 library has no concept of a "wrong password" error.
      Therefore an exception with the full error is raised so you can inspect what went actually wrong.
   #. In my opinion, a wrong password should raise an exception such that it can't pass unnoticed by accident.
      See also The Zen of Python: "Errors should never pass silently."
   #. It's more `Pythonic <https://docs.python.org/3/glossary.html#term-eafp>`_.
