from available_permissions import available_permissions, permissions
from common_groups import available_common_groups, common_groups


class Permissions(object):
    def __init__(self):
        self.admin_group = None
        self.admin_api_list = None

        self.api_key_permissions = permissions
        self.available_api_key_permissions = available_permissions
        self.common_api_key_groups = common_groups
        self.available_common_api_key_groups = available_common_groups

    '''
        Requested features in first bullet point:
        Allow you to add create, delete, read, update permissions for each of the groups defined here -- these can be hard coded in
    '''

    def add_new_permissions_list(self, list_name, permissions):
        if (list_name not in self.available_api_key_permissions):
            self.api_key_permissions[list_name] = permissions
            self.available_api_key_permissions.append(list_name)
            return True
        else:
            print("There is already an existing permissions list with the name {0}".format(
                list_name))
            print(
                "Please use the update_list_permissions command to update the permissions in list")
            return False

    def add_new_permissions_group(self, group_name, permissions):
        if (group_name not in self.available_common_api_key_groups):
            self.common_api_key_groups[group_name] = permissions
            self.available_common_api_key_groups.append(group_name)
            return True
        else:
            print("There is already an existing permissions group with the name {0}".format(
                group_name))
            print(
                "Please use the update_group_permissions command to update the permissions in group")
            return False

    def delete_permissions_list(self, list_name):
        if (list_name in self.available_api_key_permissions):
            self.api_key_permissions.pop(list_name)
            self.available_api_key_permissions.remove(list_name)
            return True
        else:
            print("Error: Invalid list name")
            return False

    def delete_permissions_group(self, group_name):
        if (group_name in self.available_common_api_key_groups):
            self.common_api_key_groups.pop(group_name)
            self.available_common_api_key_groups.remove(group_name)
            return True
        else:
            print("Error: Invalid group name")
            return False

    def update_permissions_list(self, list_name, permissions):
        if (list_name in self.available_api_key_permissions):
            self.api_key_permissions[list_name] = permissions
            return True
        else:
            print("Error: Invalid list name")
            return False

    def update_permissions_group(self, group_name, permissions):
        if (group_name in self.available_common_api_key_groups):
            self.common_api_key_groups[group_name] = permissions
            return True
        else:
            print("Error: Invalid group name")
            return False

    def read_permissions_from_list(self, group):
        if (group in self.available_api_key_permissions):
            return (self.api_key_permissions[group])
        else:
            print(
                "There is no permissions list with that given name {0}".format(group))
            return None

    def read_permissions_from_group(self, group):
        if (group in self.available_common_api_key_groups):
            return (self.common_api_key_groups[group])
        else:
            print(
                "There is no permissions group with that given name {0}".format(group))
            return None

    '''
        Requested features in second bullet point:
        Allow for creating an array of all the scopes possible, as a "create admin permissions" method
    '''

    def create_admin_permission_list(self):
        if (self.admin_api_list):
            return self.admin_api_list
        else:
            self.admin_api_list = []
            for group in self.available_api_key_permissions:
                for permission in self.api_key_permissions[group]:
                    if (permission not in self.admin_api_list):
                        self.admin_api_list.append(permission)
            return self.admin_api_list

    def create_admin_group(self):
        if (self.admin_group):
            return self.admin_group
        else:
            self.admin_group = []
            for group in self.available_common_api_key_groups:
                for permission in common_api_key_groups[group]:
                    if (permissions not in self.admin_group):
                        self.admin_group.append(permission)
            return self.admin_group

    '''
        Requested features in third bullet point:
        Allow for "read only" which pulls only read permissions
    '''

    def get_read_only_permissions_from_list(self, group):
        if (group in self.available_api_key_permissions):
            read_only_permissions = []
            for permission in api_key_permissions[group]:
                if (".read" in permission):
                    read_only_permissions.append(permission)
            return read_only_permissions
        else:
            print(
                "There is no permissions list with that given name {0}".format(group))
            return None

    def get_read_only_permissions_from_group(self, group):
        if (group in self.available_common_api_key_groups):
            read_only_permissions = []
            for permission in self.common_api_key_groups[group]:
                if (".read" in permission):
                    read_only_permissions.append(permission)
            return read_only_permissions
        else:
            print(
                "There is no permissions group with that given name {0}".format(group))
            return None

    '''
        Extra features implemented to add/remove permissions from each permissions list and group.
        This is done so we don't have to update permisisons when we want to remove or add one permission.
    '''

    def add_permission_to_list(self, group, permission):
        if (group in self.available_api_key_permissions):
            if (not permission in self.api_key_permissions[group]):
                self.api_key_permissions[group].append(permission)
                return True
            else:
                print("Permission {0} is already inside of group {1}.".format(
                    group, permission))
                return False
        else:
            print("Error: Invalid list name.")
            return False

    def add_permission_to_group(self, group, permission):
        if (group in self.available_common_api_key_groups):
            if (not permission in self.common_api_key_groups[group]):
                self.common_api_key_groups[group].append(permission)
                return True
            else:
                print("Permission {0} is already inside of group {1}.".format(
                    group, permission))
                return False
        else:
            print("Error: Invalid group name.")
            return False

    def delete_permission_from_list(self, group, permission):
        if (group in self.available_api_key_permissions):
            if (permission in self.api_key_permissions[group]):
                self.api_key_permissions[group].remove(permission)
                return True
            else:
                print("Permission {0} is not inside group {1}.".format(
                    group, permission))
                return False
        else:
            print("Error: Invalid list name.")
            return False

    def delete_permission_from_group(self, group, permission):
        if (group in self.available_common_api_key_groups):
            if (permission in self.common_api_key_groups[group]):
                self.common_api_key_groups[group].remove(permission)
                return True
            else:
                print("Permission {0} is not inside group {1}.".format(
                    group, permission))
                return False
        else:
            print("Error: Invalid group name")
            return False
