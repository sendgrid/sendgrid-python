SendGrid-Python
===============

This library allows you to quickly and easily send emails through
SendGrid using Python.

**Warning!** This library was recently updated to bring it up to date
with all of our other libraries. It behaves completely different from
the previous release. Also, SMTP has been deprecated in support for the
Web API.

Install
-------

.. code::

    pip install sendgrid
    # or
    easy_install sendgrid

Example
-------

.. code::

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

.. code::

    from sendgrid import SendGridError, SendGridClientError, SendGridServerError

    sg = sendgrid.SendGridClient(username, password, raise_errors=True)

    try:
        sg.send(message)
    except SendGridClientError:
        ...
    except SendGridServerError:
        ...

This behavior is going to be default from version 1.0.0. You are
encouraged to set ``raise_errors`` to ``True`` for forwards compatibility.

``SendGridError`` is a base-class for all SendGrid-related exceptions.

Adding Recipients
~~~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_to('example@email.com')
    # or
    message.add_to('Example Dude <example@email.com>')
    # or
    message.add_to(['Example Dude <example@email.com>', 'john@email.com'])

Adding BCC Recipients
~~~~~~~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_bcc('example@email.com')
    # or
    message.add_bcc(['Example Dude <example@email.com>', 'john@email.com'])

Setting the Subject
~~~~~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.set_subject('Example')

Set Text or HTML
~~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.set_text('Body')
    # or
    message.set_html('<html><body>Stuff, you know?</body></html>')

Set From
~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.set_from('example@email.com')

Set ReplyTo
~~~~~~~~~~~

.. code::

    message.sendgrid.Mail()
    message.set_replyto('example@email.com')

Set File Attachments
~~~~~~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_attachment('./stuff.txt')
    # or
    message.add_attachment_stream('filename', 'somerandomcontentyouwant')
    # strings, unicode, or BytesIO streams

SendGrid's `X-SMTPAPI`_
-----------------------

If you wish to use the X-SMTPAPI on your own app, you can use the
`SMTPAPI Python library`_.

There are implementations for setter methods too.

`Substitution`_
~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_substitution("key", "value")

`Section`_
~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_section("section", "value")

`Category`_
~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_category("category")

`Unique Arguments`_
~~~~~~~~~~~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_unique_arg("key", "value")

`Filter`_
~~~~~~~~~

.. code::

    message = sendgrid.Mail()
    message.add_filter("filter", "setting", "value")

TODO:
~~~~~

-  Add support for CID

Tests
~~~~~

.. code::

    python test/__init__.py

MIT License
-----------

.. _X-SMTPAPI: http://sendgrid.com/docs/API_Reference/SMTP_API/
.. _SMTPAPI Python library: https://github.com/sendgrid/smtpapi-python
.. _Substitution: http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html
.. _Section: http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html
.. _Category: http://sendgrid.com/docs/Delivery_Metrics/categories.html
.. _Unique Arguments: http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html
.. _Filter: http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html
