First, follow the [Twilio Setup](twilio-setup.md) guide for creating a Twilio account and setting up environment variables with the proper credentials.

Then, install the Twilio Helper Library.

```bash
pip install twilio
```

Finally, send a message.

```python
import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
from_number = '+15017122661'
to_number ='+15558675310'
body = "Join Earth's mightiest heroes. Like Kevin Bacon."
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=body,
    from_=from_number,
    to=to_number
)

print(message.sid)
```

For more information, please visit the [Twilio SMS Python documentation](https://www.twilio.com/docs/sms/quickstart/python).
