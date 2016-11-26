#!/usr/bin/env python

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="DAQFE",
    version="0.0",
    author="Aman Abhishek Tiwari",
    author_email="amanabt@iitk.ac.in",
    description="Front End for a Data Acquisition System",
    license="MIT",
    keywords="DAQ",
    url="https://github.com/amanabt/DAQFE",
    packages=['DAQFE'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT Licence",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Environment :: Console"
    ],
    install_requires=[
        'pyqt5'
    ],
    extras_require={
        'docs': ['sphinx', 'sphinx-argparse']
    },
    platforms='any',
    entry_points={
        'console_scripts': ['DAQFE=py_lib.fourier:main'],
    }
)
