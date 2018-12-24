import sys
import os
from io import open
from setuptools import setup, find_packages

__version__ = None
with open('sendgrid/version.py') as f:
    exec(f.read())

long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt', 'r', encoding='utf-8').read()

setup(
    name='sendgrid',
    version=str(__version__),
    author='Elmer Thomas, Yamil Asusta',
    author_email='dx@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(exclude=["temp*.py", "register.py", "test"]),
    include_package_data=True,
    license='MIT',
    description='SendGrid library for Python',
    long_description=long_description,
    install_requires=['python_http_client>=3.0'],
    python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
