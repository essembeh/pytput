#!/usr/bin/env python3

from setuptools import setup


def readfile(file):
    with open(file) as f:
        return f.read()


setup(
    name="pytput",
    description="Python3 API to format messages using colors and styles",
    url="https://github.com/essembeh/pytput",
    license="Mozilla Public License Version 2.0",
    author="Sébastien MB",
    author_email="seb@essembeh.org",
    long_description=readfile("README.md"),
    long_description_content_type="text/markdown",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    package_dir={"": "src"},
    packages=["pytput"],
    entry_points={"console_scripts": ["pytput = pytput.__main__:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "Topic :: Utilities",
    ],
)
