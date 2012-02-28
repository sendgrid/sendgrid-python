# sendgrid-python #
This library allows you to quickly and easily send emails through SendGrid using Python.

## License ##
Licensed under the MIT License.

## Install ##

Using Github:

```
git clone git@github.com:sendgrid/sendgrid-python.git
```

Using Pypi:

```
easy_install sendgrid-python
```

## SendGrid APIs ##
SendGrid provides two methods of sending email: the Web API, and SMTP API.  SendGrid recommends using the SMTP API for sending emails.
For an explanation of the benefits of each, refer to http://docs.sendgrid.com/documentation/get-started/integrate/examples/smtp-vs-rest/.

This library implements a common interface to make it very easy to use either API.

## Mail Pre-Usage ##

Before we begin using the library, its important to understand a few things about the library architecture...

* Sending an email is as simple as :
  1. Creating a SendGrid Instance
  1. Creating a SendGrid Mail object, and setting its data
  1. Sending the mail using either SMTP API or Web API.

## Mail Usage ##

```python
import sendgrid

s = sendgrid.Sendgrid('username', 'password', secure=True)
message = sendgrid.Message("from@mydomain.com", "subject", "plain body", "<b>Html here</b>")
message.add_to("someone@example.com", "John Doe")

s.web.send(message)
```

Or

```python
s.smtp.send(message)
```

### Using Categories ###

Categories are used to group email statistics provided by SendGrid.

To use a category, simply set the category name.  Note: there is a maximum of 10 categories per email.

```python
message = sendgrid.Message("from@mydomain.com", "subject", "plain body", "<b>Html here</b>")
message.add_category(["Category 1", "Category 2"])
```


### Using Attachments ###

File attachments are limited to 7 MB per file.

```python
message = sendgrid.Message("from@mydomain.com", "subject", "plain body", "<b>Html here</b>")
message.add_attachment("file1.doc", "/path/to/file.doc").add_attachment("file2.nfo", "File 2 content")
```

### Using Substitutions ###

Substitutions can be used to customize multi-recipient emails, and tailor them for the user

```python
message = sendgrid.Message("from@mydomain.com", "subject", "Hello %name%, your code is %code%", "<b>Hello %name%, your code is %code%</b>")
message.add_to(
    {
        'example1@example.com': {'%name%': 'Name 1', '%code%': 'Code 1'},
        'example2@example.com': {'%name%': 'Name 2', '%code%': 'Code 2'},
    }
)
```

### Using Sections ###

Sections can be used to further customize messages for the end users. A section is only useful in conjunction with a substition value.

```python
message = sendgrid.Message("from@mydomain.com", "subject", "Hello %name%, you work at %place%",
    "<b>Hello %name%, your code is %code%, you work at %place%</b>")
message.add_to(
    {
        'example1@example.com': {'%name%': 'Name 1', '%place%': '%home%'},
        'example2@example.com': {'%name%': 'Name 2', '%place%': '%office%'},
    }
).set_sections({"%office%": "an office", "%home%": "your house"})
```

### Using Unique Arguments ###

Unique Arguments are used for tracking purposes

```python
message = sendgrid.Message("from@mydomain.com", "subject", "plain body", "<b>Html here</b>")
message.add_unique_argument("Customer", "Someone")
```

### Using Filter Settings ###

Filter Settings are used to enable and disable apps, and to pass parameters to those apps.

```python
message = sendgrid.Message("from@mydomain.com", "subject", "plain body", "<b>Html here</b>")
message.add_filter_setting("footer", "text/plain", "Here is a plain text footer")
message.add_filter_setting("footer", "text/html", "<p style='color:red;'>Here is an HTML footer</p>")
```

### Using Headers ###

Headers can be used to add existing sendgrid functionality (such as for categories or filters), or custom headers can be added as necessary.

```python
message = sendgrid.Message("from@mydomain.com", "subject", "plain body", "<b>Html here</b>")
message.add_header("category", "My New Category")
```