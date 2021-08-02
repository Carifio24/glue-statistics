from __future__ import print_function
from setuptools import setup, find_packages

entry_points = """
[glue.plugins]
glue_statistics=glue_statistics:setup
"""

with open('README.rst') as infile:
    LONG_DESCRIPTION = infile.read()

with open('glue_statistics/version.py') as infile:
    exec(infile.read())

setup(name='glue_statistics',
      version=__version__,
      description='Statistics Plugin for Glue',
      long_description=LONG_DESCRIPTION,
      url="https://github.com/jk31768/glue-statistics",
      author='',
      author_email='',
      packages = find_packages(),
      package_data={},
      entry_points=entry_points
    )
