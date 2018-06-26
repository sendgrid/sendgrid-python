# Supported tags and respective `Dockerfile` links
 - `v5.4.1`, `latest` [(Dockerfile)](https://github.com/sendgrid/sendgrid-python/blob/master/docker/Dockerfile)
 - `v5.4.0`
 - `v5.3.0`
 - `v5.2.1`
 - `v5.2.0`
 - `v5.1.0`
 - `v5.0.1`
 - `v5.0.0`
 - `v4.2.1`
 - `v4.2.0`
 - `v4.1.0`
 - `v4.0.0`
 - `v3.6.5`
 - `v3.6.4`
 - `v3.6.3`
 - `v3.6.2`
 - `v3.3.0`
 - `v3.2.3`
 - `v3.2.2`
 - `v3.2.1`
 - `v3.2.0`
# Quick reference
 - **Where to get help:**
   [Contact SendGrid Support](https://support.sendgrid.com/hc/en-us)

 - **Where to file issues:**
   https://github.com/sendgrid/sendgrid-python/issues

 - **Where to get more info:**
   [USAGE.md](https://github.com/sendgrid/sendgrid-python/blob/master/docker/USAGE.md)

 - **Maintained by:**
   [SendGrid Inc.](https://sendgrid.com)

# Usage examples
 - Most recent version: `docker run -it sendgrid/sendgrid-python`.
 - Old version: `docker run -it sendgrid/sendgrid-python:v4.2.0`
 - Old version predating this Docker image:
   ```sh-session
   $ git clone https://github.com/sendgrid/sendgrid-python.git --branch v3.6.1
   $ realpath sendgrid-python
   /path/to/sendgrid-python
   $ docker run -it -v /path/to/sendgrid-python:/mnt/sendgrid-python sendgrid/sendgrid-python
   ```
 - Your own fork:
   ```sh-session
   $ git clone https://github.com/you/cool-sendgrid-python.git
   $ realpath cool-sendgrid-python
   /path/to/cool-sendgrid-python
   $ docker run -it -v /path/to/cool-sendgrid-python:/mnt/sendgrid-python sendgrid/sendgrid-python
   ```

For more detailed information, see [USAGE.md](https://github.com/sendgrid/sendgrid-python/blob/master/docker/USAGE.md).

# About

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
