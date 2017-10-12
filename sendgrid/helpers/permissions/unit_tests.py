from permissions import Permissions

'''
    Testing features from first bullet point:
    Allow you to add create, delete, read, update permissions for each of the groups defined here -- these can be hard coded in
'''


# test case 1:
# add new permissions list "test" with permissions "test.test" and "test.test1"
def test1():
    permissions = Permissions()
    expected_results = ["test.test", "test.test1"]

    assert(permissions.add_new_permissions_list(
        "test", ["test.test", "test.test1"]))
    assert(permissions.read_permissions_from_list("test") == expected_results)


# test case 2:
# add new permissions group "test_group" with permissions "test_group.test" and "test_group.test_feature"
def test2():
    permissions = Permissions()
    expected_results = ["test_group.test", "test_group.test_feature"]

    assert(permissions.add_new_permissions_group(
        "test_group", ["test_group.test", "test_group.test_feature"]))
    assert(permissions.read_permissions_from_group(
        "test_group") == expected_results)


# test case 3:
# remove permissions list "alerts"
def test3():
    permissions = Permissions()
    assert(permissions.delete_permissions_list("alerts"))
    assert(permissions.read_permissions_from_list("alerts") == None)


# test case 4:
# remove permissions group "read_only_access_for_mail_send"
def test4():
    permissions = Permissions()
    assert(permissions.delete_permissions_group(
        "read_only_access_for_mail_send"))
    assert(permissions.read_permissions_from_group(
        "read_only_access_for_mail_send") == None)


# test case 5:
# update permissions list "api_keys" to contain only the "api_keys.test" permission
def test5():
    permissions = Permissions()
    expected_results = ["api_keys.test"]

    assert(permissions.update_permissions_list("api_keys", ["api_keys.test"]))
    assert(permissions.read_permissions_from_list(
        "api_keys") == expected_results)


# test case 6:
# update permissions group "full_access_for_mail_send" to contain only the "mail.batch.test" permission
def test6():
    permissions = Permissions()
    expected_results = ["mail.batch.test"]

    assert(permissions.update_permissions_group(
        "full_access_for_mail_send", ["mail.batch.test"]))
    assert(permissions.read_permissions_from_group(
        "full_access_for_mail_send") == expected_results)


# test case 7:
# read permissions list "billing"
def test7():
    permissions = Permissions()
    expected_results = [
        "billing.create",
        "billing.delete",
        "billing.read",
        "billing.update"
    ]

    assert(permissions.read_permissions_from_list(
        "billing") == expected_results)


# test case 8:
# read permissions group "read_only_access_for_alerts"
def test8():
    permissions = Permissions()
    expected_results = [
        "alerts.read"
    ]

    assert(permissions.read_permissions_from_group(
        "read_only_access_for_alerts") == expected_results)


'''
    Testing features from second bullet point:
    Allow for creating an array of all the scopes possible, as a "create admin permissions" method
'''


def test9():
    permissions = Permissions()
    expected_results = [
        "access_settings.activity.read",
        "access_settings.whitelist.create",
        "access_settings.whitelist.delete",
        "access_settings.whitelist.read",
        "access_settings.whitelist.update",
        "alerts.create",
        "alerts.delete",
        "alerts.read",
        "alerts.update",
        "api_keys.create",
        "api_keys.delete",
        "api_keys.read",
        "api_keys.update",
        "asm.groups.create",
        "asm.groups.delete",
        "asm.groups.read",
        "asm.groups.update",
        "billing.create",
        "billing.delete",
        "billing.read",
        "billing.update",
        "browsers.stats.read",
        "categories.create",
        "categories.delete",
        "categories.read",
        "categories.stats.read",
        "categories.stats.sums.read",
        "categories.update",
        "clients.desktop.stats.read",
        "clients.phone.stats.read",
        "clients.stats.read",
        "clients.tablet.stats.read",
        "clients.webmail.stats.read",
        "credentials.create",
        "credentials.delete",
        "credentials.read",
        "credentials.update",
        "devices.stats.read",
        "email_activity.read",
        "geo.stats.read",
        "ips.assigned.read",
        "ips.pools.create",
        "ips.pools.delete",
        "ips.pools.ips.create",
        "ips.pools.ips.delete",
        "ips.pools.ips.read",
        "ips.pools.ips.update",
        "ips.pools.read",
        "ips.pools.update",
        "ips.read",
        "ips.warmup.create",
        "ips.warmup.delete",
        "ips.warmup.read",
        "ips.warmup.update",
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
        "mail_settings.template.update",
        "mail.batch.create",
        "mail.batch.delete",
        "mail.batch.read",
        "mail.batch.update",
        "mail.send",
        "mailbox_providers.stats.read",
        "marketing_campaigns.create",
        "marketing_campaigns.delete",
        "marketing_campaigns.read",
        "marketing_campaigns.update",
        "newsletter.create",
        "newsletter.delete",
        "newsletter.read",
        "newsletter.update",
        "partner_settings.new_relic.read",
        "partner_settings.new_relic.update",
        "partner_settings.read",
        "partner_settings.sendwithus.read",
        "partner_settings.sendwithus.update",
        "stats.global.read",
        "stats.read",
        "subusers.create",
        "subusers.credits.create",
        "subusers.credits.delete",
        "subusers.credits.read",
        "subusers.credits.remaining.create",
        "subusers.credits.remaining.delete",
        "subusers.credits.remaining.read",
        "subusers.credits.remaining.update",
        "subusers.credits.update",
        "subusers.delete",
        "subusers.monitor.create",
        "subusers.monitor.delete",
        "subusers.monitor.read",
        "subusers.monitor.update",
        "subusers.read",
        "subusers.reputations.read",
        "subusers.stats.monthly.read",
        "subusers.stats.read",
        "subusers.stats.sums.read",
        "subusers.summary.read",
        "subusers.update",
        "suppression.blocks.create",
        "suppression.blocks.delete",
        "suppression.blocks.read",
        "suppression.blocks.update",
        "suppression.bounces.create",
        "suppression.bounces.delete",
        "suppression.bounces.read",
        "suppression.bounces.update",
        "suppression.create",
        "suppression.delete",
        "suppression.invalid_emails.create",
        "suppression.invalid_emails.delete",
        "suppression.invalid_emails.read",
        "suppression.invalid_emails.update",
        "suppression.read",
        "suppression.spam_reports.create",
        "suppression.spam_reports.delete",
        "suppression.spam_reports.read",
        "suppression.spam_reports.update",
        "suppression.unsubscribes.create",
        "suppression.unsubscribes.delete",
        "suppression.unsubscribes.read",
        "suppression.unsubscribes.update",
        "suppression.update",
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
        "templates.versions.update",
        "tracking_settings.click.read",
        "tracking_settings.click.update",
        "tracking_settings.google_analytics.read",
        "tracking_settings.google_analytics.update",
        "tracking_settings.open.read",
        "tracking_settings.open.update",
        "tracking_settings.read",
        "tracking_settings.subscription.read",
        "tracking_settings.subscription.update",
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
        "user.scheduled_sends.create",
        "user.scheduled_sends.delete",
        "user.scheduled_sends.read",
        "user.scheduled_sends.update",
        "user.settings.enforced_tls.read",
        "user.settings.enforced_tls.update",
        "user.timezone.read",
        "user.username.read",
        "user.username.update",
        "user.webhooks.event.settings.read",
        "user.webhooks.event.settings.update",
        "user.webhooks.event.test.create",
        "user.webhooks.event.test.read",
        "user.webhooks.event.test.update",
        "user.webhooks.parse.settings.create",
        "user.webhooks.parse.settings.delete",
        "user.webhooks.parse.settings.read",
        "user.webhooks.parse.settings.update",
        "user.webhooks.parse.stats.read",
        "whitelabel.create",
        "whitelabel.delete",
        "whitelabel.read",
        "whitelabel.update"
    ]

    assert(permissions.create_admin_permission_list() == expected_results)


'''
    Testing features from third bullet point:
    Allow for "read only" which pulls only read permissions
'''


# test case 10:
# get read only permissions from permissions list "categories"
def test10():
    permissions = Permissions()
    expected_results = [
        "categories.read",
        "categories.stats.read",
        "categories.stats.sums.read"
    ]

    assert(permissions.get_read_only_permissions_from_list(
        "categories") == expected_results)


# test case 11:
# get read only permissions from permisisons group "alerts"
def test11():
    permissions = Permissions()
    expected_results = ["alerts.read"]

    assert(permissions.get_read_only_permissions_from_group(
        "full_access_for_alerts") == expected_results)


'''
    Testing extra features:
    Adding/removing permissions from each permissions list and group.
'''


# test case 12:
# adding the "credentials.test" permission to the "credentials" permission list
def test12():
    permissions = Permissions()
    expected_results = [
        "credentials.create",
        "credentials.delete",
        "credentials.read",
        "credentials.update",
        "credentials.test"
    ]

    assert(permissions.add_permission_to_list(
        "credentials", "credentials.test"))
    assert(permissions.read_permissions_from_list(
        "credentials") == expected_results)


# test case 13:
# add new permission 'stats.test' to 'read_only_access_for_stats' group
def test13():
    permissions = Permissions()
    expected_results = [
        "email_activity.read",
        "stats.read",
        "stats.global.read",
        "browsers.stats.read",
        "devices.stats.read",
        "geo.stats.read",
        "mailbox_providers.stats.read",
        "stats.test"
    ]

    assert(permissions.add_permission_to_group(
        "read_only_access_for_stats", "stats.test"))
    assert(
        permissions.common_api_key_groups["read_only_access_for_stats"] == expected_results)


# test case 14:
# remove new permission "stats.read" from "stats" list
def test14():
    permissions = Permissions()
    expected_results = [
        "email_activity.read",
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

    assert(permissions.delete_permission_from_list("stats", "stats.read"))
    assert(permissions.api_key_permissions["stats"] == expected_results)


# test case 15:
# remove new permission 'suppressions.read' from 'read_only_access_for_suppressions' group
def test15():
    permissions = Permissions()
    expected_results = []

    assert(permissions.delete_permission_from_group(
        "read_only_access_for_suppressions", "suppressions.read"))
    assert(
        permissions.common_api_key_groups["read_only_access_for_suppressions"] == expected_results)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()


main()
