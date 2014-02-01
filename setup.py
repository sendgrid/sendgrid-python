from setuptools import setup, find_packages

setup(
    name='sendgrid',
    version='0.2.1',
    author='Yamil Asusta',
    author_email='yamil@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(),
    license='MIT',
    description='SendGrid library for Python',
    long_description='SendGrid library for Python',
    install_requires=[
        'requests',
        'smtpapi'
    ],
)
