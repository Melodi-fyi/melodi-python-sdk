# setup.py
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='melodi',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'autoevals',
        'braintrust',
        'requests',
    ],
    author='Kevin Walsh',
    author_email='kevin@melodi.fyi',
    description='Helper functions for Melodi',
    keywords='melodi',
    long_description=long_description,
    long_description_content_type='text/markdown',  # or 'text/x-rst', 'text/plain'
)
