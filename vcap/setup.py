#!/usr/bin/env python3
import os

from setuptools import setup, find_namespace_packages

about = {}
with open("vcap/version.py") as fp:
    exec(fp.read(), about)

test_packages = ["pytest", "mock"]

PRE_RELEASE_SUFFIX = os.environ.get("PRE_RELEASE_SUFFIX", "")

setup(
    name='vcap',
    description="A library for creating OpenVisionCapsules in Python",
    author="Aotu",
    packages=find_namespace_packages(include=["vcap*"]),
    version=about["__version__"] + PRE_RELEASE_SUFFIX,

    install_requires=[
        "pycryptodomex==3.9.7",
        "scipy==1.4.1",
        "scikit-learn==0.22.2",
        "numpy>=1.16,<2",
        "tensorflow-gpu==1.15.4",
    ],
    extras_require={
        "tests": test_packages,
        "easy": ["opencv-python-headless~=4.1.2"],
    },
    tests_require=test_packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
