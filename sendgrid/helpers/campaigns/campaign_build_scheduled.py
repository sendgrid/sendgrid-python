from .campaign_build import campaign_build


def campaign_build_scheduled(api_client, campaign, schedule, notify=None):
    """Builds a campaign and schedules for release

    See sendgrid.helpers.campaigns.campaign.get_schedule for kwargs

    :param api_client: SendGrid API Client
    :type api_client: sendgrid.SendGridAPIClient
    :param campaign: Campaign object to build
    :type campaign: sendgrid.helpers.campaigns.Campaign
    :param notify: Mail objects to send on completion
    :type notify: list,sendgrid.helpers.mail.mail.Mail
    :param schedule: Schedule object to get schedule body
    :type schedule: sendgrid.helpers.campaigns.schedule.Schedule
    :return: ID of created campaign
    :rtype: int
    """
    c_id = campaign_build(api_client, campaign)
    getattr(api_client.client.campaigns, str(c_id)).schedules.post(
        request_body=schedule.get()
    )
    if notify is not None:
        if isinstance(notify, list):
            for n in notify:
                api_client.client.mail.send.post(request_body=n.get())
        else:
            api_client.client.mail.send.post(request_body=notify.get())
    return c_id
