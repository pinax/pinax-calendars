import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="Django utilities for publishing events as a calendar",
    name="pinax-calendars",
    long_description=read("README.rst"),
    version="1.0.0",
    url="http://github.com/pinax/pinax-calendars/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.calendars": [
            "templates/pinax/calendars/*"
        ]
    },
    install_requires=[
        "pytz"
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
