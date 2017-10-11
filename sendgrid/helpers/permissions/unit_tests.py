from permissions import Permissions


# test case 1:
# add new permission 'alerts.test' to 'alerts' list
def test1(permissions):
    permissions.add_permission_to_list("alerts", "alerts.test")
    expected_results = [
        "alerts.create",
        "alerts.delete",
        "alerts.read",
        "alerts.update",
        "alerts.test"
    ]
    assert(permissions.api_key_permissions["alerts"] == expected_results)


# test case 2:
# remove new permission 'alerts.test' from 'alerts' list
def test2(permissions):
    permissions.delete_permission_from_list("alerts", "alerts.test")
    expected_results = [
        "alerts.create",
        "alerts.delete",
        "alerts.read",
        "alerts.update",
    ]
    assert(permissions.api_key_permissions["alerts"] == expected_results)


# test case 3:
# add new permission 'mail.batch.test' to 'read_only_access_for_mail_send' group
def test3(permissions):
    permissions.add_permission_to_group(
        "read_only_access_for_mail_send", "mail.batch.test")
    expected_results = [
        "mail.batch.read",
        "mail.batch.test"
    ]
    assert(
        permissions.common_api_key_groups["read_only_access_for_mail_send"] == expected_results)


def main():
    permissions = Permissions()
    test1(permissions)
    test2(permissions)
    test3(permissions)


main()
