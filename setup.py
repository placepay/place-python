import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

pkg_name = 'rentshare'

install_requires = ['requests']

directory = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(directory, pkg_name))
from __about__ import __version__

setup(
    name=pkg_name,
    version=__version__,
    description='RentShare python library',
    author='RentShare',
    author_email='help@rentshare.com',
    url='https://github.com/rentshare/python-rentshare',
    packages=[pkg_name],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
