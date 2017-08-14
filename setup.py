from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='py_yaml_util',
    version='0.1.0',
    description='Python module (py_yaml_util) that reads and parses an YAML file from the given url',
    long_description=readme,
    author='Quadyster_dev_team',
    author_email='nvallepalli@quadyster.com',
    url='https://github.com/nvallepalli/cloud_creator.git',
    packages=find_packages(exclude=('tests', 'docs'))
)
