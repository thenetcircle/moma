#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.1.0'

setup(
    name='moma',
    version=version,
    description="Model Manager",
    long_description="""Model Management Tool for DataOps""",
    classifiers=[],
    keywords='ml,dataops,models',
    author='Oscar Eriksson',
    author_email='oscar.eriks@gmail.com',
    url='https://github.com/thenetcircle/moma',
    license='LICENSE.txt',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zope.interface',   # interfaces
        'pyyaml',            # configuration files
    ])
