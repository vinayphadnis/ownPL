from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

setup(
name='ownpl',
version='0.1.0',
description='Design your own Programming Language',
long_description=readme,
long_description_content_type='text/markdown',
author='Vinay Phadnis',
author_email='phadnisv3010@gmail.com',
url='https://github.com/vinayphadnis/ownPL',
license=license,
packages=find_packages(exclude=('tests', 'docs'))
)
