# -*- coding: utf-8 -*-

import os
import sys
import subprocess

try:
    from setuptools import find_packages, setup, Command
except ImportError:
    from distutils.core import find_packages, setup, Command


here = os.path.abspath(os.path.dirname(__file__))

DESCRIPTION = "Minimal database Model management for MongoDB"

try:
    LONG_DESCRIPTION = open(os.path.join(here, "README.rst")).read()
except IOError:
    print("Warning: IOError raised: cannot open README.rst.")
    LONG_DESCRIPTION = DESCRIPTION


CLASSIFIERS = (
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: BSD License"
    "Intended Audience :: Developers",
    "Topic :: Database",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
)


class PyTest(Command):
    """Unfortunately :mod:`setuptools` support only :mod:`unittest`
    based tests, thus, we have to overider build-in ``test`` command
    to run :mod:`pytest`."""
    user_options = []
    initialize_options = finalize_options = lambda self: None

    def run(self):
        errno = subprocess.call([sys.executable, "runtests.py"])
        raise SystemExit(errno)


requires = ["pymongo"]

setup(name="minimongo",
      version="0.2.9",
      packages=find_packages(),
      cmdclass={"test": PyTest},
      platforms=["any"],

      install_requires = ["pymongo<=2.8", "six"],
      zip_safe=False,
      include_package_data=True,

      author="Steve Lacy",
      author_email="slacy@slacy.com",
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      classifiers=CLASSIFIERS,
      keywords=["mongo", "mongodb", "pymongo", "orm"],
      url="https://github.com/slacy/minimongo",
)
