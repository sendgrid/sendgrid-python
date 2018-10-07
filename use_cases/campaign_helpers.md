# Campaign Helper Usage

Campaigns can be created using helper classes, then used to generate requests to the SendGrid API.

```python
import os
from sendgrid import *
from sendgrind.helpers.campaigns import *

SG = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

data = {
    "categories": [
        "summer line"
    ],
    "html_content": "<html><head><title></title></head><body><p>Check out our summer line!</p></body></html>",
    "plain_content": "Check out our summer line!",
    "subject": "New Products for Summer!",
    "title": "May Newsletter"
}

camp = Campaign(**data)

# Use the build helper
campaign_id = campaign_build(SG, camp)

# OR use the client
response = SG.client.campaigns.post(request_body=camp.get())
print(response.status_code)
print(response.body)
print(response.headers)


# Schedule the campaign
schedule = Schedule(year=2018, month=12, day=1, hour=11, minute=59)
response = getattr(SG.client.campaigns, campaign_id).schedules.post(
    request_body=schedule.get()
)
```