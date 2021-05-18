from __future__ import absolute_import, division, print_function

import codecs
import os
import platform
import re
import sys

from distutils.command.build import build
from distutils.command.build_clib import build_clib
from distutils.errors import DistutilsSetupError

from setuptools import find_packages, setup
from setuptools.command.install import install


###############################################################################

NAME = "argon2-cffi"
PACKAGES = find_packages(where="src")

use_sse2 = os.environ.get("ARGON2_CFFI_USE_SSE2", None)
if use_sse2 == "1":
    optimized = True
elif use_sse2 == "0":
    optimized = False
else:
    # Optimized version requires SSE2 extensions.  They have been around since
    # 2001 so we try to compile it on every recent-ish x86.
    optimized = platform.machine() in ("i686", "x86", "x86_64", "AMD64")

CFFI_MODULES = ["src/argon2/_ffi_build.py:ffi"]
lib_base = os.path.join("extras", "libargon2", "src")
include_dirs = [
    os.path.join(lib_base, "..", "include"),
    os.path.join(lib_base, "blake2"),
]
sources = [
    os.path.join(lib_base, path)
    for path in [
        "argon2.c",
        os.path.join("blake2", "blake2b.c"),
        "core.c",
        "encoding.c",
        "opt.c" if optimized else "ref.c",
        "thread.c",
    ]
]

# Add vendored integer types headers if necessary.
windows = "win32" in str(sys.platform).lower()
if windows:
    int_base = "extras/msinttypes/"
    inttypes = int_base + "inttypes"
    stdint = int_base + "stdint"
    vi = sys.version_info[0:2]
    if vi in [(2, 6), (2, 7)]:
        # VS 2008 needs both.
        include_dirs += [inttypes, stdint]
    elif vi in [(3, 3), (3, 4)]:
        # VS 2010 needs inttypes.h and fails with both.
        include_dirs += [inttypes]

LIBRARIES = [("argon2", {"include_dirs": include_dirs, "sources": sources})]
META_PATH = os.path.join("src", "argon2", "__init__.py")
KEYWORDS = ["password", "hash", "hashing", "security"]
PROJECT_URLS = {
    "Documentation": "https://argon2-cffi.readthedocs.io/",
    "Bug Tracker": "https://github.com/hynek/argon2-cffi/issues",
    "Source Code": "https://github.com/hynek/argon2-cffi",
    "Funding": "https://github.com/sponsors/hynek",
    "Tidelift": "https://tidelift.com/subscription/pkg/pypi-argon2-cffi?"
    "utm_source=pypi-argon2-cffi&utm_medium=pypi",
    "Ko-fi": "https://ko-fi.com/the_hynek",
}
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python",
    "Topic :: Security :: Cryptography",
    "Topic :: Security",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

SETUP_REQUIRES = ["cffi"]
if windows and sys.version_info[0] == 2:
    # required for "Microsoft Visual C++ Compiler for Python 2.7"
    # https://www.microsoft.com/en-us/download/details.aspx?id=44266
    SETUP_REQUIRES.append("setuptools>=6.0")

INSTALL_REQUIRES = ["cffi>=1.0.0", "six", "enum34; python_version<'3.4'"]
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "furo"],
    "tests": ["coverage[toml]>=5.0.2", "hypothesis", "pytest"],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["wheel", "pre-commit"]
)

###############################################################################


def keywords_with_side_effects(argv):
    """
    Get a dictionary with setup keywords that (can) have side effects.

    :param argv: A list of strings with command line arguments.

    :returns: A dictionary with keyword arguments for the ``setup()`` function.
        This setup.py script uses the setuptools 'setup_requires' feature
        because this is required by the cffi package to compile extension
        modules. The purpose of ``keywords_with_side_effects()`` is to avoid
        triggering the cffi build process as a result of setup.py invocations
        that don't need the cffi module to be built (setup.py serves the dual
        purpose of exposing package metadata).

    Stolen from pyca/cryptography.
    """
    no_setup_requires_arguments = (
        "-h",
        "--help",
        "-n",
        "--dry-run",
        "-q",
        "--quiet",
        "-v",
        "--verbose",
        "-V",
        "--version",
        "--author",
        "--author-email",
        "--classifiers",
        "--contact",
        "--contact-email",
        "--description",
        "--egg-base",
        "--fullname",
        "--help-commands",
        "--keywords",
        "--licence",
        "--license",
        "--long-description",
        "--maintainer",
        "--maintainer-email",
        "--name",
        "--no-user-cfg",
        "--obsoletes",
        "--platforms",
        "--provides",
        "--requires",
        "--url",
        "clean",
        "egg_info",
        "register",
        "sdist",
        "upload",
    )

    def is_short_option(argument):
        """Check whether a command line argument is a short option."""
        return len(argument) >= 2 and argument[0] == "-" and argument[1] != "-"

    def expand_short_options(argument):
        """Expand combined short options into canonical short options."""
        return ("-" + char for char in argument[1:])

    def argument_without_setup_requirements(argv, i):
        """Check whether a command line argument needs setup requirements."""
        if argv[i] in no_setup_requires_arguments:
            # Simple case: An argument which is either an option or a command
            # which doesn't need setup requirements.
            return True
        elif is_short_option(argv[i]) and all(
            option in no_setup_requires_arguments
            for option in expand_short_options(argv[i])
        ):
            # Not so simple case: Combined short options none of which need
            # setup requirements.
            return True
        elif argv[i - 1 : i] == ["--egg-base"]:
            # Tricky case: --egg-info takes an argument which should not make
            # us use setup_requires (defeating the purpose of this code).
            return True
        else:
            return False

    if all(
        argument_without_setup_requirements(argv, i)
        for i in range(1, len(argv))
    ):
        return {"cmdclass": {"build": DummyBuild, "install": DummyInstall}}
    else:
        use_system_argon2 = (
            os.environ.get("ARGON2_CFFI_USE_SYSTEM", "0") == "1"
        )
        if use_system_argon2:
            disable_subcommand(build, "build_clib")
        cmdclass = {"build_clib": BuildCLibWithCompilerFlags}
        if BDistWheel is not None:
            cmdclass["bdist_wheel"] = BDistWheel
        return {
            "setup_requires": SETUP_REQUIRES,
            "cffi_modules": CFFI_MODULES,
            "libraries": LIBRARIES,
            "cmdclass": cmdclass,
        }


def disable_subcommand(command, subcommand_name):
    for name, method in command.sub_commands:
        if name == subcommand_name:
            command.sub_commands.remove((subcommand_name, method))
            break


setup_requires_error = (
    "Requested setup command that needs 'setup_requires' while command line "
    "arguments implied a side effect free command or option."
)


class DummyBuild(build):
    """
    This class makes it very obvious when ``keywords_with_side_effects()`` has
    incorrectly interpreted the command line arguments to ``setup.py build`` as
    one of the 'side effect free' commands or options.
    """

    def run(self):
        raise RuntimeError(setup_requires_error)


class DummyInstall(install):
    """
    This class makes it very obvious when ``keywords_with_side_effects()`` has
    incorrectly interpreted the command line arguments to ``setup.py install``
    as one of the 'side effect free' commands or options.
    """

    def run(self):
        raise RuntimeError(setup_requires_error)


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


VERSION = find_meta("version")
URL = find_meta("url")
LONG = (
    read("README.rst")
    + "\n\n"
    + "Release Information\n"
    + "===================\n\n"
    + re.search(
        r"(\d+.\d.\d \(.*?\)\r?\n.*?)\r?\n\r?\n\r?\n----\r?\n\r?\n\r?\n",
        read("CHANGELOG.rst"),
        re.S,
    ).group(1)
    + "\n\n`Full changelog "
    + "<{url}en/stable/changelog.html>`_.\n\n".format(url=URL)
    + read("AUTHORS.rst")
)


class BuildCLibWithCompilerFlags(build_clib):
    """
    We need to pass ``-msse2`` for the optimized build.
    """

    def build_libraries(self, libraries):
        """
        Mostly copy pasta from ``distutils.command.build_clib``.
        """
        for (lib_name, build_info) in libraries:
            sources = build_info.get("sources")
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError(
                    "in 'libraries' option (library '%s'), "
                    "'sources' must be present and must be "
                    "a list of source filenames" % lib_name
                )
            sources = list(sources)

            print("building '%s' library" % (lib_name,))

            # First, compile the source code to object files in the library
            # directory.  (This should probably change to putting object
            # files in a temporary build directory.)
            macros = build_info.get("macros")
            include_dirs = build_info.get("include_dirs")
            objects = self.compiler.compile(
                sources,
                extra_preargs=["-msse2"] if optimized and not windows else [],
                output_dir=self.build_temp,
                macros=macros,
                include_dirs=include_dirs,
                debug=self.debug,
            )

            # Now "link" the object files together into a static library.
            # (On Unix at least, this isn't really linking -- it just
            # builds an archive.  Whatever.)
            self.compiler.create_static_lib(
                objects, lib_name, output_dir=self.build_clib, debug=self.debug
            )


if sys.version_info > (3,) and platform.python_implementation() == "CPython":
    try:
        import wheel.bdist_wheel
    except ImportError:
        BDistWheel = None
    else:

        class BDistWheel(wheel.bdist_wheel.bdist_wheel):
            def finalize_options(self):
                self.py_limited_api = "cp3{}".format(sys.version_info[1])
                wheel.bdist_wheel.bdist_wheel.finalize_options(self)


else:
    BDistWheel = None


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=URL,
        project_urls=PROJECT_URLS,
        version=VERSION,
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        long_description=LONG,
        long_description_content_type="text/x-rst",
        keywords=KEYWORDS,
        packages=PACKAGES,
        package_dir={"": "src"},
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        # CFFI
        zip_safe=False,
        ext_package="argon2",
        **keywords_with_side_effects(sys.argv)
    )
