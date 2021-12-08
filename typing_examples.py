import argon2


ph = argon2.PasswordHasher()

ph.hash("pw")
ph.hash(b"pw")
ph.verify("hash", "pw")
ph.verify(b"hash", "pw")
ph.verify(b"hash", b"pw")
ph.verify("hash", b"pw")

if ph.check_needs_rehash("hash") is True:
    ...
