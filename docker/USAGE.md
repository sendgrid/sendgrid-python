You can use Docker to easily try out or test sendgrid-python.

<a name="Quickstart"></a>
# Quickstart

1. Install Docker on your machine.
2. Run `docker run -it sendgrid/sendgrid-python`.

<a name="Info"></a>
# Info

This Docker image contains
 - `sendgrid-python` and `python-http-client`
 - Stoplight's Prism, which lets you try out the API without actually sending email
 - `tox` and all supported Python versions, set up to test `sendgrid-python` or your own fork

Run it in interactive mode with `-it`.

You can mount repositories in the `/mnt/sendgrid-python` and `/mnt/python-http-client` directories to use them instead of the default SendGrid libraries. Read on for more info.

<a name="Options"></a>
# Options

## Using an old version

The easiest way to use an old version is to use an [old tag](https://github.com/sendgrid/sendgrid-python/releases).

```sh-session
$ docker run -it sendgrid/sendgrid-python:v3.6.1
```

Tags from before this Docker image was created might not exist yet. You may [manually download](#Versions) [old versions](https://github.com/sendgrid/sendgrid-python/releases) in order to use them.

<a name="Versions"></a>
## Specifying specific versions

To use different versions of sendgrid-python or python-http-client - for instance, to replicate your production setup - mount them with the `-v <host_dir>:<container_dir>` option. When you put either repository under `/mnt`, the container will automatically detect it and make the proper symlinks. You can edit these files from the host machine while the container is running.

For instance, to install sendgrid-python 3.6.1 and use the current python-http-client:

```sh-session
$ git clone https://github.com/sendgrid/sendgrid-python.git --branch v3.6.1
$ realpath sendgrid-python
/path/to/sendgrid-python
$ docker run -it -v /path/to/sendgrid-python:/mnt/sendgrid-python sendgrid/sendgrid-python
```

To install sendgrid-python v3.6.1 and use an older version of python-http-client:

```sh-session
$ git clone https://github.com/sendgrid/sendgrid-python.git --branch v3.6.1
$ realpath sendgrid-python
/path/to/sendgrid-python
$ git clone https://github.com/sendgrid/python-http-client.git --branch v1.2.4
$ realpath python-http-client
/path/to/python-http-client
$ docker run -it -v /path/to/sendgrid-python:/mnt/sendgrid-python \
>                -v /path/to/python-http-client:/mnt/python-http-client \
>                sendgrid/sendgrid-python
```

## Specifying your own fork:

```sh-session
$ git clone https://github.com/you/cool-sendgrid-python.git
$ realpath cool-sendgrid-python
/path/to/cool-sendgrid-python
$ docker run -it -v /path/to/cool-sendgrid-python:/mnt/sendgrid-python sendgrid/sendgrid-python
```

Note that the paths you specify in `-v` must be absolute.

# Docker Compose

<a name="Quickstart"></a>
# Quickstart

1. Install docker-compose on your machine.
2. Must copy .env_sample to .env file.
3. Edit .env file for yours versions and paths.
4. Must create env folder for clone yours repo.
5. Have fun! :D

## Using tag's for versions - DockerHub:

### Edit variable TAG on .env/env_sample file

```sh-session
$ sed -ie 's/TAG=latest/TAG=choice_a_version/g'
```
### Run service using tags

```sh-session
$ cd /path/to/sendgrid-python/docker
$ docker-compose up -d sendgrid
```

## Specifying specific versions:

### Edit variable TAG on .env/env_sample file

```sh-session
$ sed -ie 's/SENDGRID_PYTHON_VERSION=vy.x.z/SENDGRID_PYTHON_VERSION=vx.y.z/g'
$ sed -ie 's/HTTP_CLIENT_VERSION=vy.x.z/HTTP_CLIENT_VERSION=vx.y.z/g'
```

### Run service

```sh-session
$ cd /path/to/sendgrid-python/docker
$ docker-compose up -d sendgrid-dev
```

## Specifying your own fork:

### Edit variable TAG on .env/env_sample file

```sh-session
$ sed -ie 's/TAG=latest/TAG=choice_a_version/g'
$ sed -ie 's/SENDGRID_PYTHON_VERSION=vy.x.z/SENDGRID_PYTHON_VERSION=vx.y.z/g'
```

### Run service

```sh-session
$ cd /path/to/sendgrid-python/docker
$ docker-compose up -d sendgrid-beta
```

<a name="Testing"></a>
# Testing
Testing is easy!  Run the container, `cd sendgrid`, and run `tox`.

<a name="about"></a>
# About

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
