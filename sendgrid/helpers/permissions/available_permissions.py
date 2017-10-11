available_permissions = [
    "alerts",
    "api_keys",
    "asm_groups",
    "billing",
    "categories",
    "credentials",
    "stats",
    "ips",
    "mail_settings",
    "mail",
    "marketing_campaigns",
    "partner_settings",
    "scheduled_sends",
    "subusers",
    "suppressions",
    "teammates",
    "templates",
    "tracking",
    "user_settings",
    "webhook",
    "whitelabel",
    "whitelist",
]

alerts = [
    "alerts.create",
    "alerts.delete",
    "alerts.read",
    "alerts.update"
]

api_keys = [
    "api_keys.create",
    "api_keys.delete",
    "api_keys.read",
    "api_keys.update"
]

asm_groups = [
    "asm.groups.create",
    "asm.groups.delete",
    "asm.groups.read",
    "asm.groups.update"
]

billing = [
    "billing.create",
    "billing.delete",
    "billing.read",
    "billing.update"
]

categories = [
    "categories.create",
    "categories.delete",
    "categories.read",
    "categories.update",
    "categories.stats.read",
    "categories.stats.sums.read"
]

credentials = [
    "credentials.create",
    "credentials.delete",
    "credentials.read",
    "credentials.update"
]

stats = [
    "email_activity.read",
    "stats.read",
    "stats.global.read",
    "browsers.stats.read",
    "devices.stats.read",
    "geo.stats.read",
    "mailbox_providers.stats.read",
    "clients.desktop.stats.read",
    "clients.phone.stats.read",
    "clients.stats.read",
    "clients.tablet.stats.read",
    "clients.webmail.stats.read"
]

ips = [
    "ips.assigned.read",
    "ips.read",
    "ips.pools.create",
    "ips.pools.delete",
    "ips.pools.read",
    "ips.pools.update",
    "ips.pools.ips.create",
    "ips.pools.ips.delete",
    "ips.pools.ips.read",
    "ips.pools.ips.update",
    "ips.warmup.create",
    "ips.warmup.delete",
    "ips.warmup.read",
    "ips.warmup.update"
]

mail_settings = [
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

mail = [
    "mail.batch.create",
    "mail.batch.delete",
    "mail.batch.read",
    "mail.batch.update",
    "mail.send"
]

marketing_campaigns = [
    "marketing_campaigns.create",
    "marketing_campaigns.delete",
    "marketing_campaigns.read",
    "marketing_campaigns.update"
]

partner_settings = [
    "partner_settings.new_relic.read",
    "partner_settings.new_relic.update",
    "partner_settings.read",
    "partner_settings.sendwithus.read",
    "partner_settings.sendwithus.update"
]

scheduled_sends = [
    "user.scheduled_sends.create",
    "user.scheduled_sends.delete",
    "user.scheduled_sends.read",
    "user.scheduled_sends.update"
]

subusers = [
    "subusers.create",
    "subusers.delete",
    "subusers.read",
    "subusers.update",
    "subusers.credits.create",
    "subusers.credits.delete",
    "subusers.credits.read",
    "subusers.credits.update",
    "subusers.credits.remaining.create",
    "subusers.credits.remaining.delete",
    "subusers.credits.remaining.read",
    "subusers.credits.remaining.update",
    "subusers.monitor.create",
    "subusers.monitor.delete",
    "subusers.monitor.read",
    "subusers.monitor.update",
    "subusers.reputations.read",
    "subusers.stats.read",
    "subusers.stats.monthly.read",
    "subusers.stats.sums.read"
    "subusers.summary.read"
]

suppressions = [
    "suppression.create",
    "suppression.delete",
    "suppression.read",
    "suppression.update",
    "suppression.bounces.create",
    "suppression.bounces.read",
    "suppression.bounces.update",
    "suppression.bounces.delete",
    "suppression.blocks.create",
    "suppression.blocks.read",
    "suppression.blocks.update",
    "suppression.blocks.delete",
    "suppression.invalid_emails.create",
    "suppression.invalid_emails.read",
    "suppression.invalid_emails.update",
    "suppression.invalid_emails.delete",
    "suppression.spam_reports.create",
    "suppression.spam_reports.read",
    "suppression.spam_reports.update",
    "suppression.spam_reports.delete",
    "suppression.unsubscribes.create",
    "suppression.unsubscribes.read",
    "suppression.unsubscribes.update",
    "suppression.unsubscribes.delete"
]

teammates = [
    "teammates.create",
    "teammates.read",
    "teammates.update",
    "teammates.delete"
]

templates = [
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

tracking = [
    "tracking_settings.click.read",
    "tracking_settings.click.update",
    "tracking_settings.google_analytics.read",
    "tracking_settings.google_analytics.update",
    "tracking_settings.open.read",
    "tracking_settings.open.update",
    "tracking_settings.read",
    "tracking_settings.subscription.read",
    "tracking_settings.subscription.update"
]

user_settings = [
    "user.account.read",
    "user.credits.read",
    "user.email.create",
    "user.email.delete",
    "user.email.read",
    "user.email.update",
    "user.multifactor_authentication.create",
    "user.multifactor_authentication.delete",
    "user.multifactor_authentication.read",
    "user.multifactor_authentication.update",
    "user.password.read",
    "user.password.update",
    "user.profile.read",
    "user.profile.update",
    "user.settings.enforced_tls.read",
    "user.settings.enforced_tls.update",
    "user.timezone.read",
    "user.timezone.update",
    "user.username.read",
    "user.username.update"
]

webhook = [
    "user.webhooks.event.settings.read",
    "user.webhooks.event.settings.update",
    "user.webhooks.event.test.create",
    "user.webhooks.event.test.read",
    "user.webhooks.event.test.update",
    "user.webhooks.parse.settings.create",
    "user.webhooks.parse.settings.delete",
    "user.webhooks.parse.settings.read",
    "user.webhooks.parse.settings.update",
    "user.webhooks.parse.stats.read"
]

whitelabel = [
    "whitelabel.create",
    "whitelabel.delete",
    "whitelabel.read",
    "whitelabel.update"
]

whitelist = [
    "access_settings.activity.read",
    "access_settings.whitelist.create",
    "access_settings.whitelist.delete",
    "access_settings.whitelist.read",
    "access_settings.whitelist.update"
]

permissions = {
    "alerts": alerts,
    "api_keys": api_keys,
    "asm_groups": asm_groups,
    "billing": billing,
    "categories": categories,
    "credentials": credentials,
    "stats": stats,
    "ips": ips,
    "mail_settings": mail_settings,
    "mail": mail,
    "marketing_campaigns": marketing_campaigns,
    "partner_settings": partner_settings,
    "scheduled_sends": scheduled_sends,
    "subusers": subusers,
    "suppressions": suppressions,
    "teammates": teammates,
    "templates": templates,
    "tracking": tracking,
    "user_settings": user_settings,
    "webhook": webhook,
    "whitelabel": whitelabel,
    "whitelist": whitelist
}
