# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "GridGame"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="GridGame",
    author_email="charlie@cenithinnovations.com",
    url="",
    keywords=["Swagger", "GridGame"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['./openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['GridGame=GridGame.__main__:main']},
    long_description="""\
    API for the Cenith GridGame.
    """
)
