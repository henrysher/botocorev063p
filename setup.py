#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import sys
import botocorev063p

from setuptools import setup, find_packages


requires = ['six>=1.1.0',
            'jmespathv041p==0.4.1',
            'python-dateutil>=2.1']


if sys.version_info[:2] == (2, 6):
    # For python2.6 we have a few other dependencies.
    # First we need an ordered dictionary so we use the
    # 2.6 backport.
    requires.append('ordereddict==1.1')
    # Then we need simplejson.  This is because we need
    # a json version that allows us to specify we want to
    # use an ordereddict instead of a normal dict for the
    # JSON objects.  The 2.7 json module has this.  For 2.6
    # we need simplejson.
    requires.append('simplejson==3.3.0')


setup(
    name='botocorev063p',
    version=botocorev063p.__version__,
    description='Low-level, data-driven core of boto 3.',
    long_description=open('README.rst').read(),
    author='Mitch Garnaat',
    author_email='garnaat@amazon.com',
    url='https://github.com/boto/botocorev063p',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={'botocorev063p': ['data/*.json', 'data/aws/*.json'],
                  'botocorev063p.vendored.requests': ['*.pem']},
    package_dir={'botocorev063p': 'botocorev063p'},
    include_package_data=True,
    install_requires=requires,
    license=open("LICENSE.txt").read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)
