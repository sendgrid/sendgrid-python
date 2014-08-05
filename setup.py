import sys
from setuptools import setup, find_packages

execfile('sendgrid/version.py')


def getRequires():
    deps = ['smtpapi==0.1.2']
    if sys.version_info < (3, 0):
        deps.append('unittest2')
    else:
        deps.append('unittest2py3k')
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
)
