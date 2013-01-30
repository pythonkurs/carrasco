from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='carrasco',
      version=version,
      description="Package for the python course",
      long_description="""\
Just a Set of scripts/assignments for the python course in Science For Life Laboratory""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='science bioinformatics',
      author='Guillermo Carrasco',
      author_email='guillermo.carrasco@scilifelab.se',
      url='https://github.com/guillermo-carrasco',
      license='GPL V3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
