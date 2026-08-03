# How To Contribute

First off, thank you for considering contributing!
It's people like *you* who make it is such a great tool for everyone.

This document is mainly to help you to get started by codifying tribal knowledge and expectations and make it more accessible to everyone.
But don't be afraid to open half-finished PRs and ask questions if something is unclear!


## Workflow

- No contribution is too small!
  Please submit as many fixes for typos and grammar bloopers as you can!
- Try to limit each pull request to *one* change only.
- Since we squash on merge, it's up to you how you handle updates to the main branch.
  Whether you prefer to rebase on main or merge main into your branch, do whatever is more comfortable for you.
- *Always* add tests and docs for your code.
  This is a hard rule; patches with missing tests or documentation can't be merged.
- Make sure your changes pass our [CI].
  You won't get any feedback until it's green unless you ask for it.
- For the CI to pass, the coverage must be 100%.
  If you have problems to test something, open anyway and ask for advice.
  In some situations, we may agree to add an `# pragma: no cover`.
- Once you've addressed review feedback, make sure to bump the pull request with a short note, so we know you're done.
- Don’t break backwards-compatibility.


## Local development environment

First, **fork** the repository on GitHub and **clone** it using one of the alternatives that you can copy-paste by pressing the big green button labeled `<> Code`.

We use a fully locked development environment based on [*uv*](https://docs.astral.sh/uv/), so the easiest way to get started is to [install *uv*](https://docs.astral.sh/uv/getting-started/installation/) and run:

```console
$ uv sync --python $(cat .python-version-default)
```

This creates a virtual environment in `.venv` using the Python version from the `.python-version-default` file, because that's the one that is used in the CI by default, too.
It also installs everything that's pinned in `uv.lock`.
After that, `uv run pytest` runs the test suite without you having to activate anything; if you activate `.venv` you can also run `pytest` directly.

If you're using [*direnv*](https://direnv.net), you can automate the creation and activation of that environment by adding the following `.envrc` to the project root:

```bash
uv sync --python $(cat .python-version-default)
. .venv/bin/activate
```

You can also link `.python-version-default` to `.python-version` so you don't have to remember to use `$(cat .python-version-default)` every time.

> [!WARNING]
> - **Before** you start working on a new pull request, use the "*Sync fork*" button in GitHub's web UI to ensure your fork is up to date.
> - **Always create a new branch off `main` for each new pull request.**
>   Yes, you can work on `main` in your fork and submit pull requests.
>   But this will *inevitably* lead to you not being able to synchronize your fork with upstream and having to start over.

You can (and should) run our full test suite using [*tox*].
It's part of our development environment, so `uv run tox` works out of the box.

When working on the documentation, use:

```console
$ uv run tox run -e docs-watch
```

This will build the documentation, and then watch for changes and rebuild it whenever you save a file.

To just build the documentation, use `uv run tox run -e docs-build`, and to run the doctests, use `uv run tox run -e docs-doctests`.

You will find the built documentation in `docs/_build/html`.

Our linters run in *tox*, too:

```console
$ uv run tox run -f lint
```

This formats and lints the code base using [Ruff](https://ruff.rs/) and runs all [*pre-commit*] hooks.
To have *git* catch avoidable errors before you commit, install the hooks locally using [*prek*](https://prek.j178.dev/) (or *pre-commit*, if you prefer):

```console
$ uv run prek install -f
```


## Code

- Obey [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/).
  We use the `"""`-on-separate-lines style for docstrings and [Napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) for parsing them:

  ```python
  def func(x: str, y: bool) -> int:
      """
      Do something.

      Args:
          x: A very important parameter.

          y:
              Another important parameter whose description is too long for one
              line, therefore it starts on the next line.

      Returns:
          Something!
      """
  ```
- If you add or change public APIs, tag the docstring using `..  versionadded:: 16.0.0 WHAT` or `..  versionchanged:: 16.2.0 WHAT`.

- We use [Ruff](https://ruff.rs/) to sort our imports and format our code with a line length of 79 characters.
  As long as you run `uv run tox run -f lint` before committing (see [*Local Development Environment*](#local-development-environment) above) you won't have to spend any time on formatting your code at all.
  If you don't, [CI] will catch it for you, but that seems like a waste of your time!


## Tests

- Write your asserts as `expected == actual` to line them up nicely:

  ```python
  x = f()

  assert 42 == x.some_attribute
  assert "foo" == x._a_private_attribute
  ```

- To run the test suite, all you need is a recent [*tox*].
  It will ensure the test suite runs with all dependencies against all Python versions just as it will in our [CI].

- Write [good test docstrings](https://jml.io/pages/test-docstrings.html).


## Documentation

- Use [semantic newlines] in [*reStructuredText*](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) and [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) files (files ending in `.rst` and `.md`):

  ```rst
  This is a sentence.
  This is another sentence.
  ```


### Changelog

If your change is noteworthy, there needs to be a changelog entry in `CHANGELOG.md`.

- The changelog follows the [*Keep a Changelog*](https://keepachangelog.com/en/1.0.0/) standard.
  Please add the best-fitting section if it's missing for the current release.
  We use the following order: `Security`, `Removed`, `Deprecated`, `Added`, `Changed`, `Fixed`.
- As with other docs, please use [semantic newlines] in the changelog.
- Make the last line a link to your pull request.
  You probably have to open it first to know the number.
- Wrap symbols like modules, functions, or classes into backticks so they are rendered in a `monospace font`.
- Wrap arguments into asterisks like in docstrings:
  `Added new argument *an_argument*.`
- If you mention functions or other callables, add parentheses at the end of their names:
  `argon2_cffi.func()` or `argon2_cffi.Class.method()`.
  This makes the changelog a lot more readable.
- Prefer simple past tense or constructions with "now".
  For example:

  * Added `argon2_cffi.func()`.
  * `argon2_cffi.func()` now doesn't crash the Large Hadron Collider anymore when passed the *foobar* argument.


#### Example entries

```markdown
Added `argon2_cffi.func()`.
The feature really *is* awesome.
```

or:

```markdown
`argon2_cffi.func()` now doesn't crash the Large Hadron Collider anymore when passed the *foobar* argument.
The bug really *was* nasty.
```

---

Again, this list is mainly to help you to get started by codifying tribal knowledge and expectations.
If something is unclear, feel free to ask for help!

Please note that this project is released with a Contributor [Code of Conduct](https://github.com/hynek/argon2-cffi/blob/main/.github/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.
Please report any harm to [Hynek Schlawack] in any way you find appropriate.


[CI]: https://github.com/hynek/argon2-cffi/actions
[Hynek Schlawack]: https://hynek.me/about/
[*pre-commit*]: https://pre-commit.com/
[*tox*]: https://tox.wiki/
[semantic newlines]: https://rhodesmill.org/brandon/2012/one-sentence-per-line/
