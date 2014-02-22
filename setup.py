from setuptools import setup, find_packages

setup(
    name='sendgrid',
    version='0.2.7',
    author='Yamil Asusta',
    author_email='yamil@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(),
    license='MIT',
    description='SendGrid library for Python',
    long_description=open('./README.rst').read(),
    install_requires=[
        'smtpapi'
    ],
)
