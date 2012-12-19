#!/usr/bin/env python

from setuptools import setup, find_packages

import fancyunittest

try:
    description = open('README').read()
except:
    description = __doc__

scripts = {
    'console_scripts': ['fancyunittest = fancyunittest.main:main']
}

setup(name='fancyunittest',
      version=fancyunittest.__version__,
      description="Python's unittest extension to colorize its output.",
      long_description=description,
      license='New BSD License',
      author='Anler',
      author_email='anler86@gmail.com',
      url='',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'Operating System :: Unix',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Software Development :: Testing',
      ],
      keywords="unittest colorize visualize output",
      packages=find_packages(),
      entry_points=scripts)
