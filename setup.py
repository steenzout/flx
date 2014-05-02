#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.req import parse_requirements

from setuptools import find_packages, setup

exec(open('flx/version.py').read())
setup(name='flx',
      version=__version__,
      description='Yet another Python InfluxDB client.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/flx',
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=[str(pkg.req) for pkg in parse_requirements('requirements.txt')],
      tests_requires=[str(pkg.req) for pkg in parse_requirements('test-requirements.txt')],)
