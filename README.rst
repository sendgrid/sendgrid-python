.. image:: https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png
   :target: https://www.sendgrid.com

|Travis Badge| |codecov| |Python Versions| |PyPI Version| |Docker Badge| |Email Notifications Badge| |MIT licensed| |Twitter Follow| |GitHub contributors| |Open Source Helpers|

**NEW:**

-  Subscribe to email `notifications`_ for releases and breaking changes.
-  Quickly get started with `Docker`_.

**This library allows you to quickly and easily use the SendGrid Web API v3 via Python.**

Version 3.X.X+ of this library provides full support for all SendGrid `Web API v3`_ endpoints, including the new `v3 /mail/send`_.

This library represents the beginning of a new path for SendGrid.
We want this library to be community driven and SendGrid led.
We need your help to realize this goal.
To help make sure we are building the right things in the right order,
we ask that you create `issues`_ and `pull requests`_ or simply upvote or comment on existing issues or pull requests.

Please browse the rest of this README for further detail.

We appreciate your continued support, thank you!

Table of Contents
=================

-  `Installation <#installation>`__
-  `Quick Start <#quick-start>`__
-  `Processing Inbound Email <#processing-inbound-email>`__
-  `Usage <#usage>`__
-  `Use Cases <#use-cases>`__
-  `Announcements <#announcements>`__
-  `Roadmap <#roadmap>`__
-  `How to Contribute <#how-to-contribute>`__
-  `Troubleshooting <#troubleshooting>`__
-  `About <#about>`__
-  `License <#license>`__

Installation
============

Prerequisites
-------------

-  Python version 2.7 and 3.4+
-  The SendGrid service, starting at the `free level`_

Setup Environment Variables
---------------------------

Mac
~~~

Update the development environment with your `SENDGRID_API_KEY`_ (more info `here <https://sendgrid.com/docs/User_Guide/Settings/api_keys.html>`__), for example:

.. code:: bash

    echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
    echo "sendgrid.env" >> .gitignore
    source ./sendgrid.env

SendGrid also supports local environment file ``.env``.
Copy or rename ``.env_sample`` into ``.env`` and update `SENDGRID_API_KEY`_ with your key.

Windows
~~~~~~~

Temporarily set the environment variable (accessible only during the current CLI session):

.. code:: bash

    set SENDGRID_API_KEY=YOUR_API_KEY

Permanently set the environment variable (accessible in all subsequent CLI sessions):

.. code:: bash

    setx SENDGRID_API_KEY "YOUR_API_KEY"

Install Package
---------------

.. code:: bash

    pip install sendgrid

Dependencies
------------

-  `Python-HTTP-Client`_

Quick Start
===========

Hello Email
-----------

The following is the minimum needed code to send an email with the `/mail/send Helper`_
(`here <https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail_example.py#L192>`__ is a full example):

With Mail Helper Class
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import sendgrid
    import os
    from sendgrid.helpers.mail import *

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("test@example.com")
    to_email = Email("test@example.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

The ``Mail`` constructor creates a `personalization object`_ for you.
`Here <https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail_example.py#L16>`__ is an example of how to add it.

Without Mail Helper Class
~~~~~~~~~~~~~~~~~~~~~~~~~

The following is the minimum needed code to send an email without the /mail/send Helper
(`here <https://github.com/sendgrid/sendgrid-python/blob/master/examples/mail/mail.py#L27>`__ is a full example):

.. code:: python

    import sendgrid
    import os

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    data = {
      "personalizations": [
        {
          "to": [
            {
              "email": "test@example.com"
            }
          ],
          "subject": "Sending with SendGrid is Fun"
        }
      ],
      "from": {
        "email": "test@example.com"
      },
      "content": [
        {
          "type": "text/plain",
          "value": "and easy to do anywhere, even with Python"
        }
      ]
    }
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.body)
    print(response.headers)

General v3 Web API Usage (With `Fluent Interface`_)
---------------------------------------------------

.. code:: python

    import sendgrid
    import os

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    response = sg.client.suppression.bounces.get()
    print(response.status_code)
    print(response.body)
    print(response.headers)

General v3 Web API Usage (Without `Fluent Interface`_)
------------------------------------------------------

.. code:: python

    import sendgrid
    import os

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    response = sg.client._("suppression/bounces").get()
    print(response.status_code)
    print(response.body)
    print(response.headers)

Processing Inbound Email
========================

Please see `our helper`_ for utilizing our Inbound Parse webhook.

Usage
=====

-  `SendGrid Documentation`_
-  `Library Usage Documentation`_
-  `Example Code`_
-  `How-to: Migration from v2 to v3`_
-  `v3 Web API Mail Send Helper`_ - build a request object payload for a v3 /mail/send API call.
-  `Processing Inbound Email`_

Use Cases
=========

`Examples of common API use cases`_, such as how to send an email with a transactional template.

Announcements
=============

Join an experienced and passionate team that focuses on making an impact.
`Opportunities abound`_ to grow the product - and grow your career!

Please see our announcement regarding `breaking changes`_.
Your support is appreciated!

All updates to this library are documented in our `CHANGELOG`_ and `releases`_.
You may also subscribe to email `release notifications`_ for releases and breaking changes.

Roadmap
=======

If you are interested in the future direction of this project,
please take a look at our open `issues`_ and `pull requests <https://github.com/sendgrid/sendgrid-python/pulls>`__.
We would love to hear your feedback.

How to Contribute
=================

We encourage contribution to our libraries (you might even score some nifty swag), please see our `CONTRIBUTING`_ guide for details.

Quick links:

-  `Feature Request`_
-  `Bug Reports`_
-  `Improvements to the Codebase`_
-  `Review Pull Requests`_
-  `Sign the CLA to Create a Pull Request`_

Troubleshooting
===============

Please see our `troubleshooting guide`_ for common library issues.

About
=====

**sendgrid-python** is guided and supported by the SendGrid Developer Experience Team.

Email the Developer Experience Team `here <mailto:dx@sendgrid.com>`__ in case of any queries.

**sendgrid-python** is maintained and funded by SendGrid, Inc.
The names and logos for **sendgrid-python** are trademarks of SendGrid, Inc.

License
=======

`The MIT License (MIT)`_

.. _notifications: https://dx.sendgrid.com/newsletter/python
.. _Docker: https://github.com/sendgrid/sendgrid-python/tree/master/docker
.. _Web API v3: https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html
.. _v3 /mail/send: https://sendgrid.com/blog/introducing-v3mailsend-sendgrids-new-mail-endpoint
.. _issues: https://github.com/sendgrid/sendgrid-python/issues
.. _pull requests: https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md
.. _free level: https://sendgrid.com/free?source=sendgrid-python
.. _SENDGRID_API_KEY: https://app.sendgrid.com/settings/api_keys
.. _Python-HTTP-Client: https://github.com/sendgrid/python-http-client
.. _/mail/send Helper: https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail
.. _personalization object: https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/personalizations.html
.. _Fluent Interface: https://sendgrid.com/blog/using-python-to-implement-a-fluent-interface-to-any-rest-api/
.. _our helper: https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/inbound
.. _SendGrid Documentation: https://sendgrid.com/docs/API_Reference/index.html
.. _Library Usage Documentation: https://github.com/sendgrid/sendgrid-python/tree/master/USAGE.md
.. _Example Code: https://github.com/sendgrid/sendgrid-python/tree/master/examples
.. _`How-to: Migration from v2 to v3`: https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/how_to_migrate_from_v2_to_v3_mail_send.html
.. _v3 Web API Mail Send Helper: https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/mail
.. _Processing Inbound Email: https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid/helpers/inbound
.. _Examples of common API use cases: https://github.com/sendgrid/sendgrid-python/blob/master/use_cases/README.md
.. _Opportunities abound: https://sendgrid.com/careers
.. _breaking changes: https://github.com/sendgrid/sendgrid-python/issues/217
.. _CHANGELOG: https://github.com/sendgrid/sendgrid-python/blob/master/CHANGELOG.md
.. _releases: https://github.com/sendgrid/sendgrid-python/releases
.. _release notifications: https://dx.sendgrid.com/newsletter/python
.. _CONTRIBUTING: https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md
.. _Feature Request: https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#feature-request
.. _Bug Reports: https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#submit-a-bug-report
.. _Improvements to the Codebase: https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#improvements-to-the-codebase
.. _Review Pull Requests: https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#code-reviews
.. _Sign the CLA to Create a Pull Request: https://cla.sendgrid.com/sendgrid/sendgrid-python
.. _troubleshooting guide: https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md
.. _Developer Experience Team: mailto:dx@sendgrid.com
.. _The MIT License (MIT): https://github.com/sendgrid/sendgrid-python/blob/master/LICENSE.txt

.. |Travis Badge| image:: https://travis-ci.org/sendgrid/sendgrid-python.svg?branch=master
   :target: https://travis-ci.org/sendgrid/sendgrid-python
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/sendgrid.svg
   :target: https://pypi.org/project/sendgrid/
.. |PyPI Version| image:: https://img.shields.io/pypi/v/sendgrid.svg
   :target: https://pypi.org/project/sendgrid/
.. |codecov| image:: https://img.shields.io/codecov/c/github/sendgrid/sendgrid-python/master.svg?style=flat-square&label=Codecov+Coverage
   :target: https://codecov.io/gh/sendgrid/sendgrid-python
.. |Docker Badge| image:: https://img.shields.io/docker/automated/sendgrid/sendgrid-python.svg
   :target: https://hub.docker.com/r/sendgrid/sendgrid-python/
.. |Email Notifications Badge| image:: https://dx.sendgrid.com/badge/python
   :target: https://dx.sendgrid.com/newsletter/python
.. |MIT licensed| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: ./LICENSE.txt
.. |Twitter Follow| image:: https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow
   :target: https://twitter.com/sendgrid
.. |GitHub contributors| image:: https://img.shields.io/github/contributors/sendgrid/sendgrid-python.svg
   :target: https://github.com/sendgrid/sendgrid-python/graphs/contributors
.. |Open Source Helpers| image:: https://www.codetriage.com/sendgrid/sendgrid-python/badges/users.svg
   :target: https://www.codetriage.com/sendgrid/sendgrid-python
