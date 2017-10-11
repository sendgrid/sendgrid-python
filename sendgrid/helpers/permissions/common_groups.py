available_common_groups = [
    "read_only_access_for_mail_send",
    "full_access_for_mail_send",
    "read_only_access_for_alerts",
    "full_access_for_alerts",
    "read_only_access_for_stats",
    "read_only_access_for_suppressions",
    "full_access_for_suppressions",
    "read_only_access_for_whitelabels",
    "full_access_for_whitelabels",
    "read_only_access_for_ip_management",
    "full_access_for_ip_management",
    "read_only_access_for_templates",
    "full_access_for_templates",
    "read_only_access_for_inbound_parse",
    "full_access_for_inbound_parse",
    "read_only_access_for_mail_settings",
    "full_access_for_mail_settings",
    "read_only_access_for_marketing_campaigns",
    "full_access_for_marketing_campaigns"
]

read_only_access_for_mail_send = [
    "mail.batch.read"
]

full_access_for_mail_send = [
    "mail.batch.create",
    "mail.batch.delete",
    "mail.batch.read",
    "mail.batch.update",
    "mail.send"
]

read_only_access_for_alerts = [
    "alerts.read"
]

full_access_for_alerts = [
    "alerts.create",
    "alerts.delete",
    "alerts.read",
    "alerts.update"
]

read_only_access_for_stats = [
    "email_activity.read",
    "stats.read",
    "stats.global.read",
    "browsers.stats.read",
    "devices.stats.read",
    "geo.stats.read",
    "mailbox_providers.stats.read"
]

read_only_access_for_suppressions = [
    "suppressions.read"
]

full_access_for_suppressions = [
    "suppressions.create",
    "suppressions.delete",
    "suppressions.read",
    "suppressions.update"
]

read_only_access_for_whitelabels = [
    "whitelabel.read"
]

full_access_for_whitelabels = [
    "whitelabel.create",
    "whitelabel.delete",
    "whitelabel.read",
    "whitelabel.update"
]

read_only_access_for_ip_management = [
    "ips.assigned.read",
    "ips.read",
    "ips.pools.read",
    "ips.warmup.read"
]

full_access_for_ip_management = [
    "ips.assigned.read",
    "ips.read",
    "ips.pools.create",
    "ips.pools.delete",
    "ips.pools.read",
    "ips.pools.update",
    "ips.pools.ips.create",
    "ips.pools.ips.delete",
    "ips.warmup.create",
    "ips.warmup.delete",
    "ips.warmup.read"
]

read_only_access_for_templates = [
    "templates.read",
    "templates.versions.activate.read",
    "templates.versions.read"
]

full_access_for_templates = [
    "templates.create",
    "templates.delete",
    "templates.read",
    "templates.update",
    "templates.versions.activate.create",
    "templates.versions.activate.delete",
    "templates.versions.activate.read",
    "templates.versions.activate.update",
    "templates.versions.create",
    "templates.versions.delete",
    "templates.versions.read",
    "templates.versions.update"
]

read_only_access_for_inbound_parse = [
    "user.webhooks.parse.settings.read",
    "user.webhooks.parse.stats.read"
]

full_access_for_inbound_parse = [
    "user.webhooks.parse.settings.create",
    "user.webhooks.parse.settings.delete",
    "user.webhooks.parse.settings.read",
    "user.webhooks.parse.settings.update",
    "user.webhooks.parse.stats.read"
]

read_only_access_for_mail_settings = [
    "mail_settings.address_whitelist.read",
    "mail_settings.bcc.read",
    "mail_settings.bounce_purge.read",
    "mail_settings.footer.read",
    "mail_settings.forward_bounce.read",
    "mail_settings.forward_spam.read",
    "mail_settings.plain_content.read",
    "mail_settings.read",
    "mail_settings.spam_check.read",
    "mail_settings.template.read"
]

full_access_for_mail_settings = [
    "mail_settings.address_whitelist.read",
    "mail_settings.address_whitelist.update",
    "mail_settings.bcc.read",
    "mail_settings.bcc.update",
    "mail_settings.bounce_purge.read",
    "mail_settings.bounce_purge.update",
    "mail_settings.footer.read",
    "mail_settings.footer.update",
    "mail_settings.forward_bounce.read",
    "mail_settings.forward_bounce.update",
    "mail_settings.forward_spam.read",
    "mail_settings.forward_spam.update",
    "mail_settings.plain_content.read",
    "mail_settings.plain_content.update",
    "mail_settings.read",
    "mail_settings.spam_check.read",
    "mail_settings.spam_check.update",
    "mail_settings.template.read",
    "mail_settings.template.update"
]

read_only_access_for_marketing_campaigns = [
    "marketing_campaigns.read"
]

full_access_for_marketing_campaigns = [
    "marketing_campaigns.create",
    "marketing_campaigns.delete",
    "marketing_campaigns.read",
    "marketing_campaigns.update",
    "partner_settings.new_relic.read"
]

common_groups = {
    "read_only_access_for_mail_send": read_only_access_for_mail_send,
    "full_access_for_mail_send": full_access_for_mail_send,
    "read_only_access_for_alerts": read_only_access_for_alerts,
    "full_access_for_alerts": full_access_for_alerts,
    "read_only_access_for_stats": read_only_access_for_stats,
    "read_only_access_for_suppressions": read_only_access_for_suppressions,
    "full_access_for_suppressions": full_access_for_suppressions,
    "read_only_access_for_whitelabels": read_only_access_for_whitelabels,
    "full_access_for_whitelabels": full_access_for_whitelabels,
    "read_only_access_for_ip_management": read_only_access_for_ip_management,
    "full_access_for_ip_management": full_access_for_ip_management,
    "read_only_access_for_templates": read_only_access_for_templates,
    "full_access_for_templates": full_access_for_templates,
    "read_only_access_for_inbound_parse": read_only_access_for_inbound_parse,
    "full_access_for_inbound_parse": full_access_for_inbound_parse,
    "read_only_access_for_mail_settings": read_only_access_for_mail_settings,
    "full_access_for_mail_settings": full_access_for_mail_settings,
    "read_only_access_for_marketing_campaigns": read_only_access_for_marketing_campaigns,
    "full_access_for_marketing_campaigns": full_access_for_marketing_campaigns
}
