import json


def campaign_build(api_client, campaign, notify=None):
    """Build a Campaign via the SendGrid API

    :param api_client: SendGrid API Client
    :type api_client: sendgrid.SendGridAPIClient
    :param campaign: Campaign object to build
    :type campaign: sendgrid.helpers.campaigns.Campaign
    :param notify: Mail objects to send on completion
    :type notify: list,sendgrid.helpers.mail.mail.Mail
    :return: Campaid.id for newly created Campaign
    """
    response = api_client.client.campaigns.post(request_body=campaign.get())
    camp_id = json.loads(response.body.decode())["id"]
    if notify is not None:
        if isinstance(notify, list):
            for n in notify:
                api_client.client.mail.send.post(request_body=n.get())
        else:
            api_client.client.mail.send.post(request_body=notify.get())
    return camp_id
