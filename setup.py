import sys
from setuptools import setup, find_packages

__version__ = None
with open('sendgrid/version.py') as f:
    exec(f.read())


def getRequires():
    deps = ['smtpapi==0.3.1']
    if sys.version_info < (2, 7):
        deps.append('unittest2')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('unittest2py3k')
    if (3, 0) <= sys.version_info:
        deps.append('aiohttp')
    return deps

setup(
    name='sendgrid',
    version=str(__version__),
    author='Yamil Asusta',
    author_email='yamil@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(),
    license='MIT',
    description='SendGrid library for Python',
    long_description=open('./README.rst').read(),
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
