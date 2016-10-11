import sys
import os
from setuptools import setup, find_packages

__version__ = None
with open('sendgrid/version.py') as f:
    exec(f.read())

long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

def getRequires():
    deps = ['python_http_client>=2.1.1']
    if sys.version_info < (2, 7):
        deps.append('unittest2')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('unittest2py3k')
    return deps

setup(
    name='sendgrid',
    version=str(__version__),
    author='Elmer Thomas, Yamil Asusta',
    author_email='dx@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(exclude=["temp*.py"]),
    include_package_data=True,
    license='MIT',
    description='SendGrid library for Python',
    long_description=long_description,
    install_requires=getRequires(),
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
