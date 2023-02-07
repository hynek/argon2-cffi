# How To Contribute

First off, thank you for considering contributing to *argon2-cffi*!
It's people like *you* who make it such a great tool for everyone.

This document intends to make contribution more accessible by codifying tribal knowledge and expectations.
Don't be afraid to open half-finished PRs, and ask questions if something is unclear!

Please note that this project is released with a Contributor [Code of Conduct](https://github.com/hynek/argon2-cffi/blob/main/.github/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.
Please report any harm to [Hynek Schlawack] in any way you find appropriate.


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


## Local Development Environment

You can (and should) run our test suite using [*tox*].
However, you’ll probably want a more traditional environment as well.
We highly recommend to develop using the version specified in the `.python-version` file in the project root.
That's the version used in CI by default.

First create a [virtual environment](https://virtualenv.pypa.io/) so you don't break your system-wide Python installation.
It’s out of scope for this document to list all the ways to manage virtual environments in Python, but if you don’t already have a pet way, take some time to look at tools like [*direnv*](https://hynek.me/til/python-project-local-venvs/), [*virtualfish*](https://virtualfish.readthedocs.io/), and [*virtualenvwrapper*](https://virtualenvwrapper.readthedocs.io/).

Next, get an up-to-date checkout of the *argon2-cffi* repository:

```console
$ git clone git@github.com:hynek/argon2-cffi.git
```

or if you prefer to use *Git* via `https`:

```console
$ git clone https://github.com/hynek/argon2-cffi.git
```

Change into the newly created directory and **after activating your virtual environment** install an editable version of *argon2-cffi* along with its tests and docs requirements:

```console
$ cd argon2-cffi
$ python -m pip install --upgrade pip wheel  # PLEASE don't skip this step
$ python -m pip install -e '.[dev]'
```

At this point,

```console
$ python -m pytest
```

should work and pass, as should:

```console
$ cd docs
$ make html
```

The built documentation can then be found in `docs/_build/html/`.

To avoid committing code that violates our style guide, we strongly advise you to install [*pre-commit*] and its hooks:

```console
$ pre-commit install
```

This is not strictly necessary, because our [*tox*] file contains an environment that runs:

```console
$ pre-commit run --all-files
```

and our CI has integration with `pre-commit.ci <https://pre-commit.ci>`_.
But it's way more comfortable to run it locally and *git* catching avoidable errors.


## Code

- Obey [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/).
  We use the `"""`-on-separate-lines style for docstrings:

  ```python
  def func(x):
      """
      Do something.

      :param str x: A very important parameter.

      :rtype: str
      """
  ```
- If you add or change public APIs, tag the docstring using `..  versionadded:: 16.0.0 WHAT` or `..  versionchanged:: 16.2.0 WHAT`.
- We use [*isort*](https://github.com/PyCQA/isort) to sort our imports, and we use [*Black*](https://github.com/psf/black) with line length of 79 characters to format our code.
  As long as you run our full [*tox*] suite before committing, or install our [*pre-commit*] hooks (ideally you'll do both – see [*Local Development Environment*](#local-development-environment) above), you won't have to spend any time on formatting your code at all.
  If you don't, [CI] will catch it for you – but that seems like a waste of your time!


## Tests

- Write your asserts as `expected == actual` to line them up nicely:

  ```python
  x = f()

  assert 42 == x.some_attribute
  assert "foo" == x._a_private_attribute
  ```

- To run the test suite, all you need is a recent [*tox*].
  It will ensure the test suite runs with all dependencies against all Python versions just as it will in our [CI].
  If you lack some Python versions, you can can always limit the environments like `tox -e py38,py39`, or make it a non-failure using `tox --skip-missing-interpreters`.

  In that case you should look into [*asdf*](https://asdf-vm.com) or [*pyenv*](https://github.com/pyenv/pyenv), which make it very easy to install many different Python versions in parallel.
- Write [good test docstrings](https://jml.io/pages/test-docstrings.html).


## Documentation

- Use [semantic newlines] in [*reStructuredText*] and [*Markdown*](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) files (files ending in `.rst` and `.md`):

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


[CI]: https://github.com/hynek/argon2-cffi/actions
[Hynek Schlawack]: https://hynek.me/about/
[*pre-commit*]: https://pre-commit.com/
[*tox*]: https://https://tox.wiki/
[semantic newlines]: https://rhodesmill.org/brandon/2012/one-sentence-per-line/
