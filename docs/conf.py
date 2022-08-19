# SPDX-License-Identifier: MIT

from importlib import metadata


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "argon2-cffi"
copyright = "2015, Hynek Schlawack"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = metadata.version("argon2-cffi")
# The short X.Y version.
version = release.rsplit(".", 1)[0]

rst_epilog = f"""
.. |changelog| replace:: What’s new?
.. _changelog: https://github.com/hynek/argon2-cffi/blob/{release}/CHANGELOG.md
"""

# In dev mode, always point to main branch. There's no tags yet.
if release.endswith(".dev0"):
    rst_epilog = rst_epilog.replace(release, "main")

# Move type hints into the description block, instead of the func definition.
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True


# -- Options for HTML output ----------------------------------------------

html_theme = "furo"

# Output file base name for HTML help builder.
htmlhelp_basename = "argon2-cffidoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "argon2-cffi.tex",
        "argon2-cffi Documentation",
        "Hynek Schlawack",
        "manual",
    )
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        "argon2-cffi",
        "argon2-cffi Documentation",
        ["Hynek Schlawack"],
        1,
    )
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "argon2-cffi",
        "argon2-cffi Documentation",
        "Hynek Schlawack",
        "argon2-cffi",
        "The secure Argon2 password hashing algorithm.",
        "Miscellaneous",
    )
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/3": None}
