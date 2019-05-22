import io
import os
from distutils.file_util import copy_file
from setuptools import setup, find_packages


def getRequires():
    deps = ['python_http_client>=3.0']
    return deps


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()
version = io.open(os.path.join(dir_path, 'sendgrid/VERSION.txt'), encoding='utf-8').read().strip()
copy_file(os.path.join(dir_path, 'sendgrid', 'VERSION.txt'),
          os.path.join(dir_path, 'sendgrid', 'VERSION.txt'),
          verbose=0)

setup(
    name='sendgrid',
    version=version,
    author='Elmer Thomas, Yamil Asusta',
    author_email='dx@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(exclude=["temp*.py", "test"]),
    include_package_data=True,
    license='MIT',
    description='Twilio SendGrid library for Python',
    long_description=readme,
    install_requires=getRequires(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
