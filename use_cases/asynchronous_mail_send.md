# Asynchronous Mail Send

## Using `asyncio` (3.6+)

The built-in `asyncio` library can be used to send email in a non-blocking manner. `asyncio` helps us execute mail sending in a separate context, allowing us to continue the execution of business logic without waiting for all our emails to send first.

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Mail, From, To, Mail
from functools import partial
import os
import asyncio

try:
    # Python 3.7+ only.  This is more efficient than get_event_loop where
    # available.
    from asyncio import get_running_loop
    from asyncio import run as async_run
except ImportError:
    # Python 3.6+ compatibility
    from asyncio import get_event_loop as get_running_loop

    def async_run(future):
        loop = asyncio.new_event_loop()
        try:
            try:
                return loop.run_until_complete(future)
            finally:
                loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            loop.close()


sendgrid_client = SendGridAPIClient(
    api_key=os.environ.get('SENDGRID_API_KEY'))

from_email = From("test@example.com")
to_email = To("test1@example.com")

plain_text_content = Content("text/plain", "This is asynchronous sending test.")
html_content = Content("text/html", "<strong>This is asynchronous sending test.</strong>")

# instantiate `sendgrid.helpers.mail.Mail` objects
em1 = Mail(from_email, to_email, "Message #1", content)
em2 = Mail(from_email, to_email, "Message #2", content)
em3 = Mail(from_email, to_email, "Message #3", content)
em4 = Mail(from_email, to_email, "Message #4", content)
em5 = Mail(from_email, to_email, "Message #5", content)
em6 = Mail(from_email, to_email, "Message #6", content)
em7 = Mail(from_email, to_email, "Message #7", content)
em8 = Mail(from_email, to_email, "Message #8", content)
em9 = Mail(from_email, to_email, "Message #9", content)
em10 = Mail(from_email, to_email, "Message #10", content)


ems = [em1, em2, em3, em4, em5, em6, em7, em8, em9, em10]


async def send_email(n: int, email: Mail) -> None:
    '''
    send_mail wraps Twilio SendGrid's API client, and makes a POST request to
    the api/v3/mail/send endpoint with ``email``.
    '''
    try:
        loop = get_running_loop()

        # This runs the sending in a thread managed by the executor.  This is
        # what allows blocking IO calls to operate asynchronously, because they
        # are actually run in a different thread, allowing parallel
        # asynchronous operation to proceed as desired, at least while active
        # IO has released Python's GIL
        response = await loop.run_in_executor(
            None,
            partial(
                sendgrid_client.send,
                request_body=email))

        if response.status_code < 300:
            print("Email #{} processed".format(n), response.body, response.status_code)
    except urllib.error.HTTPError as e:
        e.read()


async def send_many(emails):
    '''
    send_many creates a number of non-blocking tasks (to send email)
    that will run on the existing event loop's executor (ThreadPoolExecutor by
    default).

    Args:
        emails: contains any # of `sendgrid.helpers.mail.Mail`.
    '''
    print("START - sending emails ...")

    # gather is necessary to actually batch futures to run in parallel.
    # create_task and ensure_future are also options to do the same, but you
    # would have to await all those tasks individually anyway otherwise you
    # could end up with your program killing unfinished futures.  This is the
    # simplest way to wait for all futures to finish.
    await asyncio.gather(*[send_email(n, em) for n, em in enumerate(emails)])
    print("END - returning control...")

if __name__ == "__main__":
    async_run(send_many(ems))
```
