How To Contribute
=================

Every open source project lives from the generous help by contributors that sacrifice their time and ``argon2_cffi`` is no different.

Here are a few guidelines to get you started:

- If you want to install a *development version* of ``argon2_cffi`` into your current ``virtualenv``, you have to remember to:

  #. ``git submodule init`` (to initialize git submodule mechanics)
  #. ``git submodule update`` (to update the vendored Argon2 C library to the version ``argon2_cffi`` is currently packaging)
  #. ``python setup.py build`` (to build the CFFI module)
  #. ``pip install -e .[dev]``  (to [re-]install it along with the Python code and test dependencies)

  You have to perform steps 2, 3, and 4 whenever something changes in the Argon2 C code (e.g. if the vendored code has been updated).

- Try to limit each pull request to one change only.
- To run the test suite, all you need is a recent tox_.
  It will ensure the test suite runs with all dependencies against all Python versions just as it will on `Travis CI`_.
  If you lack some Python versions, you can can make it a non-failure using ``tox --skip-missing-interpreters`` (in that case you may want to look into pyenv_ that makes it very easy to install many different Python versions in parallel).

  One of the environments requires a system-wide installation of Argon2.
  On macOS, it's available in Homebrew and recent Ubuntus (zesty and later) ship it too.
- Make sure your changes pass our CI.
  You won't get any feedback until it's green unless you ask for it.
- Once you've addressed review feedback, make sure to bump the pull request with a short note, so we know you're done.
- If your change is noteworthy, add an entry to the changelog_.
  Use semantic newlines and add a link to your pull request.
- No contribution is too small; please submit as many fixes for typos and grammar bloopers as you can!
- Don’t break backward compatibility.
- *Always* add tests and docs for your code.
  This is a hard rule; patches with missing tests or documentation won’t be merged.
- Write `good test docstrings`_.
- Obey `PEP 8`_ and `PEP 257`_.

Please note that this project is released with a Contributor `Code of Conduct`_.
By participating in this project you agree to abide by its terms.
Please report any harm to `Hynek Schlawack`_ in any way you find appropriate.

Thank you for considering to contribute!


.. _Hynek Schlawack: https://hynek.me/about/
.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/
.. _`PEP 257`: https://www.python.org/dev/peps/pep-0257/
.. _`good test docstrings`: https://jml.io/pages/test-docstrings.html
.. _`Code of Conduct`: https://github.com/hynek/argon2_cffi/blob/master/.github/CODE_OF_CONDUCT.rst
.. _changelog: https://github.com/hynek/argon2_cffi/blob/master/CHANGELOG.rst
.. _`tox`: https://tox.readthedocs.io/
.. _`Travis CI`: https://travis-ci.org/
.. _pyenv: https://github.com/pyenv/pyenv
