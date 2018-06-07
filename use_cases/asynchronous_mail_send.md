# Asynchronous Mail Send

## Using `asyncio` (3.5+)

The built-in `asyncio` library can be used to send email in a non-blocking manner. `asyncio` helps us execute mail sending in a separate context, allowing us to continue execution of business logic without waiting for all our emails to send first.

```python
import sendgrid
from sendgrid.helpers.mail import *
import os
import asyncio


sg = sendgrid.SendGridAPIClient(
    apikey=os.getenv("SENDGRID_API_KEY")
)

from_email = Email("test@example.com")
to_email = Email("test1@example.com")

content = Content("text/plain", "This is asynchronous sending test.")

# instantiate `sendgrid.helpers.mail.Mail` objects
em1 = Mail(from_email, "Message #1", to_email, content)
em2 = Mail(from_email, "Message #2", to_email, content)
em3 = Mail(from_email, "Message #3", to_email, content)
em4 = Mail(from_email, "Message #4", to_email, content)
em5 = Mail(from_email, "Message #5", to_email, content)
em6 = Mail(from_email, "Message #6", to_email, content)
em7 = Mail(from_email, "Message #7", to_email, content)
em8 = Mail(from_email, "Message #8", to_email, content)
em9 = Mail(from_email, "Message #9", to_email, content)
em10 = Mail(from_email, "Message #10", to_email, content)


ems = [em1, em2, em3, em4, em5, em6, em7, em8, em9, em10]


async def send_email(n, email):
    '''
    send_mail wraps SendGrid's API client, and makes a POST request to
    the api/v3/mail/send endpoint with `email`.
    Args:
        email<sendgrid.helpers.mail.Mail>: single mail object.
    '''
    try:
        response = sg.client.mail.send.post(request_body=email.get())
        if response.status_code < 300:
            print("Email #{} processed".format(n), response.body, response.status_code)
    except urllib.error.HTTPError as e:
        e.read()


@asyncio.coroutine
def send_many(emails, cb):
    '''
    send_many creates a number of non-blocking tasks (to send email)
    that will run on the existing event loop. Due to non-blocking nature,
    you can include a callback that will run after all tasks have been queued.

    Args:
        emails<list>: contains any # of `sendgrid.helpers.mail.Mail`.
        cb<function>: a function that will execute immediately.
    '''
    print("START - sending emails ...")
    for n, em in enumerate(emails):
        asyncio.async(send_email(n, em))
    print("END - returning control...")
    cb()


def sample_cb():
    print("Executing callback now...")
    for i in range(0, 100):
        print(i)
    return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = asyncio.async(send_many(ems, sample_cb))
    loop.run_until_complete(task)
```