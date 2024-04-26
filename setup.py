# create setup.py for this package 

from setuptools import setup, find_packages

setup(
    name='morph1D',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pygem>=2.0.0',
    ],
)