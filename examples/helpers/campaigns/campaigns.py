import json
from sendgrid.helpers.campaigns import *
from sendgrid import *

# NOTE: you will need move this file to the root directory of this project to execute properly.

# Assumes you set your environment variable:
# https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
SG = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

def pprint_json(json_raw):
    print(json.dumps(json.loads(json_raw), indent=4, sort_keys=True))


def print_campaigns():
    response = sg.client.categories.campaigns.get(query_params=stats_params)
    print(response.status_code)
    print(response.headers)
    pprint_json(response.body)


def get_campaigns():
    """Get Campaign objects"""
    campaigns = []
    response = SG.client.campaigns.get()
    for camp in json.loads(response.body.decode())["result"]:
        campaigns.append(Campaign(**camp))
    return campaigns


def create_campaign(call_func=False):
    camp_settings = {
        "title": "Test Campaign 1",
        "categories": ["test", "example"],
        "html_content": "<html><head><title>New Edition!</title></head><body><p>New edition is now live!</p></body></html>",
    }
    camp = Campaign(**camp_settings)

    if call_func:
        campaign_build(SG, camp)
    else:
        SG.client.campaigns.post(request_body=camp.get())


def schedule_campaign():
    """Schedule the first campaign retrieved"""
    # campaigns = []

    campaigns = Campaigns(offset=0, limit=2)
    response = SG.client.campaigns.get(query_params=campaigns.get())
    for camp in json.loads(response.body.decode())["result"]:
        print(schedule.get())
        print(camp["title"])
        c_response = getattr(SG.client.campaigns, str(camp["id"])).schedules.get()
        pprint_json(c_response.body.decode())

        schedule = Schedule(year=2018, month=12, day=1, hour=8, minute=23)
        c_response = getattr(SG.client.campaigns, str(camp["id"])).schedules.post(
            request_body=schedule.get()
        )
        pprint_json(c_response.body.decode())

        c_response = getattr(SG.client.campaigns, str(camp["id"])).schedules.get()
        pprint_json(c_response.body.decode())
        break


def main():
    get_campaigns()
    create_campaign()


if __name__ == "__main__":
    main()
