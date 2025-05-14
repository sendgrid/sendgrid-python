import io
import os
from setuptools import setup, find_packages


__version__ = None
with open('sendgrid/version.py') as f:
    exec(f.read())

def getRequires():
    deps = [
        'python_http_client>=3.2.1',
        'ecdsa>=0.19.1,<1',
        "werkzeug>=0.11.15,<1.0.0 ; python_version < '3.0'",
        "werkzeug>=0.15.0,<2.0.0 ; python_version >= '3.0' and python_version < '3.7'",
        "werkzeug>=0.15.0,<2.3.0 ; python_version >= '3.0' and python_version < '3.8'", # version 2.3.0 dropped support for Python 3.7
        "werkzeug>=0.16.0,<3.1.0 ; python_version >= '3.0' and python_version < '3.9'", # version 3.1.0 dropped support for Python 3.8
        "werkzeug>=1.0.0 ; python_version >= '3.9'",
        "werkzeug>=2.2.0 ; python_version >= '3.11'",
        "werkzeug>=2.3.5 ; python_version >= '3.12'"
    ]
    return deps


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()

setup(
    name='sendgrid',
    version=str(__version__),
    author='Elmer Thomas, Yamil Asusta',
    author_email='help@twilio.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(exclude=["temp*.py", "test"]),
    include_package_data=True,
    license='MIT',
    description='Twilio SendGrid library for Python',
    long_description=readme,
    install_requires=getRequires(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ]
)
