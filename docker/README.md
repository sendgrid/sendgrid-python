To easily install sendgrid-python, you can use Docker.

# Installation

1. Install Docker on your machine
2. Pull the latest Docker image with `docker code here`
3. Run it with `docker code here`.

# Info

This Docker image contains
 - `sendgrid-python` and `python-http-client`
 - Stoplight's Prism, which lets you try out the API without actually sending email
 - A complete setup for testing the repository or your own fork

# Options

To use a different version of sendgrid-python or python-http-client, mount it with the `-v <host_dir>:<container_dir>` option.  If you put it under `/mnt`, the container will automatically detect it and make the proper symlinks under root.

For instance, to install v3.6.1:
    $ DOCKER PULL CODE HERE
    $ git clone https://github.com/sendgrid/sendgrid-python.git --branch v3.6.1
    $ realpath sendgrid-python
      /foo/sendgrid-python
    $ DOCKER RUN CODE HERE
To install your own version:
    $ DOCKER PULL CODE HERE
    $ git clone https://github.com/foo/cool-sendgrid-python.git
    $ realpath sendgrid-python
      /foo/cool-sendgrid-python
    $ DOCKER RUN CODE HERE

# Testing
Testing is easy!  Just `cd sendgrid` and run `tox`.
