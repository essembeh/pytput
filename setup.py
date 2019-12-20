#!/usr/bin/env python3

from setuptools import find_packages, setup


def readfile(file):
    with open(file) as f:
        return f.read()


def readlines(file):
    return [
        line
        for line in map(str.strip, readfile(file).splitlines())
        if not line.startswith("#")
    ]


setup(
    name="pytput",
    description="Python3 API to format messages using colors and styles",
    url="https://github.com/essembeh/pytput",
    long_description=readfile("README.md"),
    long_description_content_type="text/markdown",
    license="Mozilla Public License Version 2.0",
    author="Sébastien MB",
    author_email="seb@essembeh.org",
    python_requires=">=3.6.0",
    setup_requires=["setuptools_scm"],
    use_scm_version={"version_scheme": "post-release"},
    install_requires=readlines("requirements.txt"),
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*_tests"]),
    entry_points={"console_scripts": ["pytput = pytput.__main__:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "Topic :: Utilities",
    ],
)
