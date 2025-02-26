from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    jgo_long_description = f.read()

setup(
    name="jgo",
    version="1.0.4.dev0",
    author="SciJava team",
    author_email="ctrueden@wisc.edu",
    description="Launch Java code from Python and the CLI, installation-free.",
    long_description=jgo_long_description,
    long_description_content_type="text/markdown",
    license="Public domain",
    url="https://github.com/scijava/jgo",
    packages=["jgo"],
    test_suite="nose.collector",
    entry_points={"console_scripts": ["jgo=jgo:main"]},
    python_requires='>=3.6',
    install_requires=["psutil"],
    tests_require=["nose>=1.0"],
)
