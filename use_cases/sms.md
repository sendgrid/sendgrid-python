In order to add Twilio SMS to your app, you will need to:

1. Setup a [free Twilio account](https://www.twilio.com/try-twilio?source=sendgrid-python)
2. Update your environment variables

Your Account Sid and Auth Token from [twilio.com/console](https://twilio.com/console)

### Mac

```bash
echo "export TWILIO_ACCOUNT_SID='YOUR_TWILIO_ACCOUNT_SID'" > twilio.env
echo "export TWILIO_AUTH_TOKEN='YOUR_TWILIO_AUTH_TOKEN'" >> twilio.env
echo "twilio.env" >> .gitignore
source ./twilio.env
```

### Windows

Temporarily set the environment variable (accessible only during the current CLI session):

```bash
set TWILIO_ACCOUNT_SID=YOUR_TWILIO_ACCOUNT_SID
set TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
```

Permanently set the environment variable (accessible in all subsequent CLI sessions):

```bash
setx TWILIO_ACCOUNT_SID "YOUR_TWILIO_ACCOUNT_SID"
setx TWILIO_AUTH_TOKEN "YOUR_TWILIO_AUTH_TOKEN"
```

3. `pip install twilio`

Then, you can execute the following code.

```python
import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
from_number = '+15017122661'
to_number ='+15558675310'
body = "Join Earth's mightiest heroes. Like Kevin Bacon."
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=body,
                     from_=from_number,
                     to=to_number
                 )

print(message.sid)
```

For more information, please visit the [Twilio SMS Python documentation](https://www.twilio.com/docs/sms/quickstart/python).