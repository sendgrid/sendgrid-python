from available_permissions import available_permissions, permissions
from common_groups import available_common_groups, common_groups


class Permissions(object):
    def __init__(self):
        self.api_key_permissions = permissions
        self.available_api_key_permissions = available_permissions
        self.common_api_key_groups = common_groups
        self.available_common_api_key_groups = available_common_groups

    def add_permission_to_list(self, group, permission):
        if (group in self.available_api_key_permissions):
            if (not permission in self.api_key_permissions[group]):
                self.api_key_permissions[group].append(permission)
            else:
                print("Permission {0} is already inside of group {1}.".format(
                    group, permission))
        else:
            print("Error: Invalid list name.")

    def add_permission_to_group(self, group, permission):
        if (group in self.available_common_api_key_groups):
            if (not permission in self.common_api_key_groups[group]):
                self.common_api_key_groups[group].append(permission)
            else:
                print("Permission {0} is already inside of group {1}.".format(
                    group, permission))
        else:
            print("Error: Invalid group name.")

    def delete_permission_from_list(self, group, permission):
        if (group in self.available_api_key_permissions):
            if (permission in self.api_key_permissions[group]):
                self.api_key_permissions[group].remove(permission)
            else:
                print("Permission {0} is not inside group {1}.".format(
                    group, permission))
        else:
            print("Error: Invalid list name.")

    def delete_permission_from_group(self, group, permission):
        if (group in self.available_common_api_key_groups):
            if (permission in self.common_api_key_groups[group]):
                self.common_api_key_groups[group].remove(permission)
            else:
                print("Permission {0} is not inside group {1}.".format(
                    group, permission))
        else:
            print("Error: Invalid group name")

    def read_permissions_from_list(self, group):
        if (group in self.available_api_key_permissions):
            print(str(self.api_key_permissions[group]))
        else:
            print("Error: Invalid list name")

    def read_permissions_from_group(self, group):
        if (group in self.available_common_api_key_groups):
            print(str(self.available_common_api_key_groups[group]))
        else:
            print("Error: Invalid group name")
