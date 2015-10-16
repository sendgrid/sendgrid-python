SendGrid-Python
===============

This library allows you to quickly and easily send emails through
SendGrid using Python.

.. image:: https://travis-ci.org/sendgrid/sendgrid-python.svg?branch=master
    :target: https://travis-ci.org/sendgrid/sendgrid-python

Warning
-------

If you upgrade to version ``1.2.x``, the ``add_to`` method behaves differently. In the past this method defaulted to using the ``SMTPAPI`` header. Now you must explicitly call the ``smtpapi.add_to`` method. More on the ``SMTPAPI`` section.

Announcements
-------------

For users of our `Web API v3 endpoints`_, we have begun integrating v3 endpoints into this library. As part of this process we have implemented a test automation tool, TOX_. We are also updating and enhancing the core library code.

In no particular order, we have implemented a `few of the v3`_ endpoints already and would appreciate your feedback.

Thank you for your continued support! 

Install
-------

.. code:: python

    pip install sendgrid
    # or
    easy_install sendgrid

Example
-------

.. code:: python

    import sendgrid

    sg = sendgrid.SendGridClient('YOUR_SENDGRID_USERNAME', 'YOUR_SENDGRID_PASSWORD')

    message = sendgrid.Mail()
    message.add_to('John Doe <john@email.com>')
    message.set_subject('Example')
    message.set_html('Body')
    message.set_text('Body')
    message.set_from('Doe John <doe@email.com>')
    status, msg = sg.send(message)

    #or

    message = sendgrid.Mail(to='john@email.com', subject='Example', html='Body', text='Body', from_email='doe@email.com')
    status, msg = sg.send(message)

Error handling
--------------

By default, ``.send`` method returns a tuple ``(http_status_code, message)``,
however you can pass ``raise_errors=True`` to ``SendGridClient`` constructor,
then ``.send`` method will raise ``SendGridClientError`` for 4xx errors,
and ``SendGridServerError`` for 5xx errors.

.. code:: python

    from sendgrid import SendGridError, SendGridClientError, SendGridServerError

    sg = sendgrid.SendGridClient(username, password, raise_errors=True)

    try:
        sg.send(message)
    except SendGridClientError:
        ...
    except SendGridServerError:
        ...

This behavior is going to be default from version 2.0.0. You are
encouraged to set ``raise_errors`` to ``True`` for forwards compatibility.

``SendGridError`` is a base-class for all SendGrid-related exceptions.

Usage
~~~~~

To begin using this library create a new instance of `SendGridClient` with your SendGrid credentials or a SendGrid API Key. API Key is the preferred method. API Keys are in beta. To configure API keys, visit https://app.sendgrid.com/settings/api_keys.

.. code:: python

    sg = sendgrid.SendGridClient('sendgrid_username', 'sendgrid_password')
    # or
    sg = sendgrid.SendGridClient('sendgrid_apikey')

Methods
~~~~~~~

There are multiple ways to add recipients:

add_to
^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_to('example@email.com')
    # or
    message.add_to('Example Dude <example@email.com>')
    # or
    message.add_to(['Example Dude <example@email.com>', 'john@email.com'])
    
add_to_name
^^^^^^^^^^^
    
.. code:: python

    message = sendgrid.Mail()
    message.add_to('example@email.com')
    message.add_to_name('Example Dude')
    
add_cc
^^^^^^
    
.. code:: python

    message = sendgrid.Mail()
    message.add_cc('example@email.com')
    message.add_cc(['example@email.com', 'john@email.com'])
    
add_bcc
^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_bcc('example@email.com')
    # or
    message.add_bcc(['Example Dude <example@email.com>', 'john@email.com'])
    
set_from
^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_from('example@email.com')

set_from_name
^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_from('example@email.com')
    message.set_from_name('Example Dude')

set_replyto
^^^^^^^^^^^

.. code:: python

    message.sendgrid.Mail()
    message.set_replyto('example@email.com')

set_subject
^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_subject('Example')

set_text
^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_text('Body')
    
set_html
^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_html('<html><body>Stuff, you know?</body></html>')
    
set_date
^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_date('Wed, 17 Dec 2014 19:21:16 +0000')
    
set_headers
^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_headers({'X-Sent-Using': 'SendGrid-API', 'X-Transport': 'web'});

Set File Attachments
~~~~~~~~~~~~~~~~~~~~

There are multiple ways to work with attachments:

add_attachment
^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_attachment('stuff.txt', './stuff.txt')
    # or
    message.add_attachment('stuff.txt', open('./stuff.txt', 'rb'))
    
add_attachment_stream
^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_attachment_stream('filename', 'somerandomcontentyouwant')
    # strings, unicode, or BytesIO streams
    
add_content_id
^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_attachment('image.png', open('./image.png', 'rb'))
    message.add_content_id('image.png', 'ID_IN_HTML')
    message.set_html('<html><body>TEXT BEFORE IMAGE<img src="cid:ID_IN_HTML"></img>AFTER IMAGE</body></html>')
    
WEB API v3
----------

.. _APIKeysAnchor:

`APIKeys`_
~~~~~~~~~~

List all API Keys belonging to the authenticated user.

.. code:: python
    
    client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    status, msg = client.apikeys.get()
    
`Advanced Suppression Manager (ASM)`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advanced Suppression Manager gives your recipients more control over the types of emails they want to receive by letting them opt out of messages from a certain type of email.

More information_. 

.. _information: https://sendgrid.com/docs/API_Reference/Web_API_v3/Advanced_Suppression_Manager/index.html

ASM Groups
~~~~~~~~~~

Retrieve all suppression groups associated with the user.

.. code:: python
    
    client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    status, msg = client.asm_groups.get()

Get a single record.

.. code:: python

    status, msg = client.asm_groups.get(record_id)
    
Create a new suppression group.

.. code:: python

    status, msg = client.asm_groups.post(name, description, is_default)
    
ASM Suppressions
~~~~~~~~~~~~~~~~

Suppressions are email addresses that can be added to groups to prevent certain types of emails from being delivered to those addresses.

Add recipient addresses to the suppressions list for a given group.

.. code:: python
    
    client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    group_id = <group_id_number> # If no group_id_number, the emails will be added to the global suppression group
    emails = ['elmer+test@thinkingserious.com', 'elmer+test2@thinkingserious.com']
    status, msg = client.asm_suppressions.post(group_id, emails)

Get suppressed addresses for a given group.

.. code:: python

    status, msg = client.asm_suppressions.get(<group_id>)

Get suppression groups associated with a given recipient address.

.. code:: python

    status, msg = client.asm_suppressions.get(None,<email_address>)
    
Delete a recipient email from the suppressions list for a group.

.. code:: python

    status, msg = client.asm_suppressions.delete(<group_id>,<email_address>)

ASM Global Suppressions
~~~~~~~~~~~~~~~~~~~~~~~

Global Suppressions are email addresses that will not receive any emails.

Check if a given email is on the global suppression list.

.. code:: python
    
    client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    email = ['elmer@thinkingserious.com']
    status, msg = client.asm_global_suppressions.get(email)

SendGrid's `X-SMTPAPI`_
-----------------------

If you wish to use the X-SMTPAPI on your own app, you can use the
`SMTPAPI Python library`_.

There are implementations for setter methods too.

`Recipients`_
~~~~~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.add_to('example@email.com')

`Substitution`_
~~~~~~~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.add_substitution('key', 'value')

add_substitution
^^^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_substitution('key', 'value')
    
set_substitutions
^^^^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_substitutions({'key1': ['value1', 'value2'], 'key2': ['value3', 'value4']})

`Section`_
~~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.add_section('section', 'value')
    
add_section
^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_section('section', 'value')
    
set_sections
^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_sections({'section1': 'value1', 'section2': 'value2'})

`Category`_
~~~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.add_category('category')
    
add_category
^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_category('category')
    
set_categories
^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_categories(['category1', 'category2'])

`Unique Arguments`_
~~~~~~~~~~~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.add_unique_arg('key', 'value')
    
add_unique_arg
^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_unique_arg('key', 'value')
    
set_unique_args
^^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_unique_args({'key1': 'value1', 'key2': 'value2'})

`Filter`_
~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.add_filter('filter', 'setting', 'value')
    
add_filter
^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.add_filter('filter', 'setting', 'value')

`ASM Group`_
~~~~~~~~~~~~

.. code:: python

    message = sendgrid.Mail()
    message.smtpapi.set_asm_group_id(value)

set_asm_group_id
^^^^^^^^^^^^^^^^

.. code:: python

    message = sendgrid.Mail()
    message.set_asm_group_id(value)
    
Using Templates from the Template Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    message.add_filter('templates', 'enable', '1')
    message.add_filter('templates', 'template_id', 'TEMPLATE-ALPHA-NUMERIC-ID')

Tests
~~~~~

**Prerequisites:**

- Mac OS X Prerequisite: 

.. code:: python

    xcode-select --install

- Install pyenv and tox

.. code:: python

    brew update
    brew install pyenv
    pip install tox

- Add `eval "$(pyenv init -)"` to your profile after installing tox, you only need to do this once.

.. code:: python

    pyenv install 2.6.9
    pyenv install 2.7.8
    pyenv install 3.2.6
    pyenv install 3.3.6
    pyenv install 3.4.3
    pyenv install 3.5.0

**Run the tests:**

.. code:: python

    virtualenv venv
    source venv/bin/activate #or . ./activate.sh
    python setup.py install
    pyenv local 3.5.0 3.4.3 3.3.6 3.2.6 2.7.8 2.6.9
    pyenv rehash
    tox

Deploying
~~~~~~~~~

- Confirm tests pass
- Bump the version in `sendgrid/version.py`
- Update `CHANGELOG.md`
- Confirm tests pass
- Commit `Version bump vX.X.X`
- `python setup.py sdist bdist_wininst upload`
- Push changes to GitHub
- Release tag on GitHub `vX.X.X`

.. _X-SMTPAPI: http://sendgrid.com/docs/API_Reference/SMTP_API/
.. _SMTPAPI Python library: https://github.com/sendgrid/smtpapi-python
.. _Substitution: http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html
.. _Section: http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html
.. _Category: http://sendgrid.com/docs/Delivery_Metrics/categories.html
.. _Unique Arguments: http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html
.. _Filter: http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html
.. _`Web API v3 endpoints`: https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html
.. _TOX: https://testrun.org/tox/latest/
.. _`few of the v3`: APIKeysAnchor_
