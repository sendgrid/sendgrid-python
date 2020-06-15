from sendgrid.helpers.eventwebhook import EventWebhook, EventWebhookHeader

def is_valid_signature(request):
    public_key = 'base64-encoded public key'

    event_webhook = EventWebhook()
    ec_public_key = event_webhook.convert_public_key_to_ecdsa(public_key)

    return event_webhook.verify_signature(
        request.text,
        request.headers[EventWebhookHeader.SIGNATURE],
        request.headers[EventWebhookHeader.TIMESTAMP],
        ec_public_key
    )
