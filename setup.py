from setuptools import find_packages, setup
from tech_talk_demo import __version__

setup(
    name='tech_talk_demo',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='Databricks Labs CICD Templates Sample Project',
    author='ME'
)
