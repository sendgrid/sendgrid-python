# Integrate with Slack Events API

It's fairly straightforward to integrate Twilio SendGrid with Slack, to allow emails to be triggered by events happening on Slack.

For this, we make use of the [Official Slack Events API](https://github.com/slackapi/python-slack-events-api), which can be installed using pip.

To allow our application to get notifications of slack events, we first create a Slack App with Event Subscriptions as described [here](https://github.com/slackapi/python-slack-events-api#--development-workflow)

Then, we set `SENDGRID_API_KEY` _(which you can create on the Twilio SendGrid dashboard)_ and `SLACK_VERIFICATION_TOKEN` _(which you can get in the App Credentials section of the Slack App)_ as environment variables.

Once this is done, we can subscribe to [events on Slack](https://api.slack.com/events) and trigger emails when an event occurs. In the example below, we trigger an email to `test@example.com` whenever someone posts a message on Slack that has the word "_help_" in it.

```python
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Subject, PlainTextContent, HtmlContent, Mail

sendgrid_client = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))


SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]
slack_events_adapter = SlackEventAdapter(SLACK_VERIFICATION_TOKEN, "/slack/events")

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "help", then send an email using Twilio SendGrid
    if message.get("subtype") is None and "help" in message.get('text').lower():
        message = "Someone needs your help: \n\n %s" % message["text"]
        r = send_email(message)
        print(r)


def send_email(message):
    from_email = From("slack_integration@example.com")
    to_email = To("test@example.com")
    subject = Subject("Psst... Someone needs help!")
    plain_text_content = PlainTextContent(message)
    html_content = HtmlContent('{0}message{0}'.format('<strong>','</strong>'))
    message = Mail(from_email, to_email, subject, plain_text_content, html_content)
    response = sendgrid_client.send(message=message)
    return response.status_code

# Start the slack event listener server on port 3000
slack_events_adapter.start(port=3000)
```
