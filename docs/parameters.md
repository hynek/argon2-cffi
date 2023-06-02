# Choosing Parameters

:::{note}
You can probably just use {class}`argon2.PasswordHasher` with its default values and be fine.
But it's good to double check using *argon2-cffi*'s {doc}`cli` client, whether its defaults are too slow or too fast for your use case.
:::

Finding the right parameters for a password hashing algorithm is a daunting task.
As of September 2021, we have the official Internet standard [RFC 9106] to help use with it.

It comes with two recommendations in [section 4](https://www.rfc-editor.org/rfc/rfc9106.html#section-4), that (as of *argon2-cffi* 21.2.0) you can load directly from the {mod}`argon2.profiles` module: {data}`argon2.profiles.RFC_9106_HIGH_MEMORY` (called "FIRST RECOMMENDED") and {data}`argon2.profiles.RFC_9106_LOW_MEMORY` ("SECOND RECOMMENDED") into {meth}`argon2.PasswordHasher.from_parameters()`.

Please use the {doc}`cli` interface together with its `--profile` argument to see if they work for you.

______________________________________________________________________

If you need finer tuning, the current recommended best practice is as follow:

1. Choose whether you want Argon2i, Argon2d, or Argon2id (`type`).
   If you don't know what that means, choose Argon2id ({attr}`argon2.Type.ID`).

2. Figure out how many threads can be used on each call to Argon2 (`parallelism`, called "lanes" in the RFC).
   They recommend 4 threads.

3. Figure out how much memory each call can afford (`memory_cost`).
   The APIs use [Kibibytes] (1024 bytes) as base unit.

4. Select the salt length.
   16 bytes is sufficient for all applications, but can be reduced to 8 bytes in the case of space constraints.

5. Choose a hash length (`hash_len`, called "tag length" in the documentation).
   16 bytes is sufficient for password verification.

6. Figure out how long each call can take.
   One [recommendation](https://web.archive.org/web/20160304024620/https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2015/march/enough-with-the-salts-updates-on-secure-password-schemes/) for concurrent user logins is to keep it under 0.5 ms.
   The RFC used to recommend under 500 ms.
   The truth is somewhere between those two values: more is more secure, less is a better user experience.
   *argon2-cffi*'s current defaults land with ~50ms somewhere in the middle, but the actual time depends on your hardware.

   Please note though, that even a verification time of 1 second won't protect you against bad passwords from the "top 10,000 passwords" lists that you can find online.

7. Measure the time for hashing using your chosen parameters.
   Start with `time_cost=1` and measure the time it takes.
   Raise `time_cost` until it is within your accounted time.
   If `time_cost=1` takes too long, lower `memory_cost`.

*argon2-cffi*'s {doc}`cli` will help you with this process.

:::{note}
Alternatively, you can also refer to the [OWASP cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id).
:::

[kibibytes]: https://en.wikipedia.org/wiki/Kibibyte
[rfc 9106]: https://www.rfc-editor.org/rfc/rfc9106.html
