# How to Hash a Password

*argon2-cffi* comes with an high-level API and uses the officially recommended low-memory Argon2 parameters that result in a verification time of 40--50ms on recent-ish hardware.

:::{warning}
The current memory requirement is set to rather conservative 64 MB.
However, in memory constrained environments such as Docker containers that can lead to problems.
One possible non-obvious symptom are apparent freezes that are caused by swapping.

Please check {doc}`parameters` for more details.
:::

Unless you have any special requirements, all you need to know is:

```python
>>> from argon2 import PasswordHasher
>>> ph = PasswordHasher()
>>> hash = ph.hash("correct horse battery staple")
>>> hash  # doctest: +SKIP
'$argon2id$v=19$m=65536,t=3,p=4$MIIRqgvgQbgj220jfp0MPA$YfwJSVjtjSU0zzV/P3S9nnQ/USre2wvJMjfCIjrTQbg'
>>> ph.verify(hash, "correct horse battery staple")
True
>>> ph.check_needs_rehash(hash)
False
>>> ph.verify(hash, "Tr0ub4dor&3")
Traceback (most recent call last):
...
argon2.exceptions.VerifyMismatchError: The password does not match the supplied hash
```

A login function could thus look like this:

```{literalinclude} login_example.py
```

---

While the {class}`argon2.PasswordHasher` class has the aspiration to be good to use out of the box, it has all the parametrization you'll need.
