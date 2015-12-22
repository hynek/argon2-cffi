Frequently Asked Questions
==========================

I'm using ``bcrypt``/``scrypt``/``PBKDF2``, do I need to migrate?
  Using password hashes that aren't memory hard carries a certain risk but there's **no immediate danger or need for action**.
  If however you are deciding how to hash password *today*, pick Argon2 because it's a superior, future-proof choice.

  But if you already use one of the hashes mentioned in the question, you should be fine for the foreseeable future.
