First, follow the [Twilio Setup](twilio-setup.md) guide for creating a Twilio account and setting up environment variables with the proper credentials.

Then, initialize the Twilio Email Client.

```python
import sendgrid
import os

mail_client = sendgrid.TwilioEmailAPIClient(os.environ.get('TWILIO_API_KEY'), os.environ.get('TWILIO_API_SECRET'))

# or

mail_client = sendgrid.TwilioEmailAPIClient(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))
```

This client has the same interface as the `SendGridAPIClient` client.
