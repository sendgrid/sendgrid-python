import io
import os

from setuptools import find_packages, setup

__version__ = None
with open("sendgrid/version.py") as f:
    exec(f.read())


def getRequires():
    deps = [
        "python_http_client>=3.2.1",
        "cryptography>=44.0.1",
        "werkzeug==3.0.6 ; python_version == '3.8'",  # version 3.1.0 dropped support for Python 3.8
        "werkzeug>=3.0.6 ; python_version >= '3.9'",
    ]
    return deps


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, "README.rst"), encoding="utf-8").read()

setup(
    name="sendgrid",
    version=str(__version__),
    author="Elmer Thomas, Yamil Asusta",
    author_email="help@twilio.com",
    url="https://github.com/sendgrid/sendgrid-python/",
    packages=find_packages(exclude=["temp*.py", "test"]),
    include_package_data=True,
    license="MIT",
    description="Twilio SendGrid library for Python",
    long_description=readme,
    install_requires=getRequires(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
