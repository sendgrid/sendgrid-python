import sys
from setuptools import setup, find_packages


def getRequires():
    deps = ['smtpapi==0.1.2']
    if sys.version_info < (3, 0):
        deps.append('unittest2')
    else:
        deps.append('unittest2py3k')
    return deps


setup(
    name='sendgrid',
    version='0.5.1',
    author='Yamil Asusta',
    author_email='yamil@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(),
    license='MIT',
    description='SendGrid library for Python',
    long_description=open('./README.rst').read(),
    install_requires=getRequires(),
)
