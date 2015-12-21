Frequently Asked Questions
==========================

I'm using ``bcrypt``/``scrypt``/``PBKDF2``, do I need to migrate?
  Using password hashes that aren't memory hard carries a certain risk but there's **no immediate danger or need for action**.
  If however you are deciding how to hash password today, pick Argon2 because it's a superior, future-proof choice.

  But if you already use one of the hashes mentioned in the question, you should be fine for the foreseeable future.


Why does ``argon2_cffi`` work on bytes and not on Unicode strings?
  Argon2 (as virtually any C library) works on bytes.
  Trying to guess what encoding your password should be hashed as, is a road to security problems:
  It's not unthinkable that someone hashes their password in Python using UTF-8 and checks it in C using latin-9.

  The *encoded* hash *is* always ASCII bytes though.
  So we *could* encode/decode it on demand.

  We've decided against it for two reasons:

  #. **Simplicity/symmetry**: In ``argon2_cffi`` *every* string is bytes.
     No need to think about it.
  #. **Performance**: The C functions of Argon2 *always* take bytes.
     If the user *wants* to use bytes, accepting Unicode would lead to overhead: either to check types or they would have to do an superfluous encode/decode dance.

     This is a problem, because when you're choosing your parameters, your hashing times shouldn't be significantly slower than those of your potential attackers.
     And since ``argon2_cffi`` is mainly a low-level library, we want to give you the best performance possible.

  All that said, it's possible that some kind of higher-level helper functions will make it into ``argon2_cffi`` eventually.
  For now, we encourage you to write your own that perfectly fit your use-case though.
