from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = find_packages(exclude=['contrib', 'docs', 'tests'])

setup(name='pylockscreen',
      version='0.0.0',
      description='Simple yet modern Python i3lock alternative',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Arinnrron',
      packages=packages,
      scripts=[''],
      author_email='',
      url='https://github.com/Arinerron/pylockscreen/e',
      install_requires=[
      ],
      classifiers=[
        "Programming Language :: Python :: 3"
      ]
     )
