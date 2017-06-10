#!/usr/bin/env python

from setuptools import setup
from os.path import exists

import versioneer


setup(name='xarray-sim',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='xarray extension for computer model simulations',
      url='http://github.com/benbovy/xarray-sim',
      maintainer='Benoit Bovy',
      maintainer_email='benbovy@gmail.com',
      license='BSD-Clause3',
      keywords='python xarray modelling simulation-framework',
      packages=['xrsim'],
      long_description=(open('README.md').read() if exists('README.md')
                        else ''),
      python_requires='>=3.4',
      install_requires=['numpy', 'xarray >= 0.8.0'],
      zip_safe=False)
