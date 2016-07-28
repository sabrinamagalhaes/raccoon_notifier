from setuptools import find_packages
from setuptools import setup

setup(
    name='raccoon_email',
    version='1.0.0',
    description="Configure email sender to set a model for all projects.",
    author="Raccoon",
    author_email="ti@raccoon.ag",
    url="https://www.raccoon.ag",
    packages=find_packages(),
    install_requires=[
        'plivo',
        'urllib3[secure]',
    ]
)
