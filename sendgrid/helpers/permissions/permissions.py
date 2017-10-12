from available_permissions import available_permissions, permissions
from common_groups import available_common_groups, common_groups


class Permissions(object):

    # initialization of class object
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

    #   Adds a new permissions list to the class
    #   inputs:
    #       list_name:string variable that contains the name of the new list
    #       permissions:string[] variable that contains permissions of the new list
    #   outputs:
    #       success:boolean True if operation is successful, False if not
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
    
    #   Adds a new permissions group to the class
    #   inputs:
    #       group_name:string variable that contains the name of the new group
    #       permissions:string[] variable that contains permission of the new list
    #   outputs:
    #       success:boolean True if operation is successful, False if not
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
    

    #   Deletes a permissions list
    #   inputs:
    #       list_name:string variable that contains the name of the list
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def delete_permissions_list(self, list_name):
        if (list_name in self.available_api_key_permissions):
            self.api_key_permissions.pop(list_name)
            self.available_api_key_permissions.remove(list_name)
            return True
        else:
            print("Error: Invalid list name")
            return False


    #   Deletes a permissions group
    #   inputs:
    #       group_name:string variable that contains the name of the group
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def delete_permissions_group(self, group_name):
        if (group_name in self.available_common_api_key_groups):
            self.common_api_key_groups.pop(group_name)
            self.available_common_api_key_groups.remove(group_name)
            return True
        else:
            print("Error: Invalid group name")
            return False


    #   Updates permissions for a permissions list
    #   inputs:
    #       list_name:string variable that contains the name of list
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def update_permissions_list(self, list_name, permissions):
        if (list_name in self.available_api_key_permissions):
            self.api_key_permissions[list_name] = permissions
            return True
        else:
            print("Error: Invalid list name")
            return False

    
    #   Updates permissions for a permissions group
    #   inputs:
    #       group_name:string variable that contains the name of a group
    #   outputs:
    #       success:boolean True if operation is sucessful, False if not
    def update_permissions_group(self, group_name, permissions):
        if (group_name in self.available_common_api_key_groups):
            self.common_api_key_groups[group_name] = permissions
            return True
        else:
            print("Error: Invalid group name")
            return False


    #   Reads permissions that a permissions list contains
    #   inputs:
    #       list_name:string variable that contains the name of a list
    #   outputs:
    #       permissions:string[] variable that contains the permissions of a list,
    #       or None if no list name found
    def read_permissions_from_list(self, list_name):
        if (list_name in self.available_api_key_permissions):
            return (self.api_key_permissions[list_name])
        else:
            print(
                "There is no permissions list with that given name {0}".format(list_name))
            return None


    #   Read permissions that a permissions group contains
    #   inputs:
    #       group_name:string variable that contains the name of a group
    #   outputs:
    #       permissions:string[] variable that contains the permissions of a group,
    #       or None if no group name found
    def read_permissions_from_group(self, group_name):
        if (group_name in self.available_common_api_key_groups):
            return (self.common_api_key_groups[group_name])
        else:
            print(
                "There is no permissions group with that given name {0}".format(group_name))
            return None

    '''
        Requested features in second bullet point:
        Allow for creating an array of all the scopes possible, as a "create admin permissions" method
    '''


    #   Create an admin list - a list containing all available permissions
    #   outputs:
    #       admin_list:string[] variable containing all possible permissions
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



    #   Create an admin group - a group containing all available permissions from all groups
    #   outputs:
    #       admin_group:string[] variable inheriting all possible groups
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


    #   Return read only permissions from a permissions list
    #   inputs:
    #       list_name:string variable containing the name of a list
    #   outputs:    
    #       read_only_list:string[] variable containing all read only permissions of given list
    def get_read_only_permissions_from_list(self, list_name):
        if (list_name in self.available_api_key_permissions):
            read_only_permissions = []
            for permission in self.api_key_permissions[list_name]:
                if ("read" in permission):
                    read_only_permissions.append(permission)
            return read_only_permissions
        else:
            print(
                "There is no permissions list with that given name {0}".format(list_name))
            return None


    #   Return read only permissions from a permissions group
    #   inputs:
    #       group_name:string variable containing the name of a group
    #   outputs:
    #       read_only_group:string[] variable containing all read only permissions
    #       of given group
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
    
    #   Add permission to permissions list
    #   inputs:
    #       list_name:string variable containing name of list
    #       permission:string variable containing permission to be added
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def add_permission_to_list(self, list_name, permission):
        if (list_name in self.available_api_key_permissions):
            if (not permission in self.api_key_permissions[list_name]):
                self.api_key_permissions[list_name].append(permission)
                return True
            else:
                print("Permission {0} is already inside of list {1}.".format(
                    list_name, permission))
                return False
        else:
            print("Error: Invalid list name.")
            return False


    #   Add permission to permissions group
    #   inputs:
    #       group_name:string variable containing name of group
    #       permission:string variable containing permission to be added
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def add_permission_to_group(self, group_name, permission):
        if (group_name in self.available_common_api_key_groups):
            if (not permission in self.common_api_key_groups[group_name]):
                self.common_api_key_groups[group_name].append(permission)
                return True
            else:
                print("Permission {0} is already inside of group {1}.".format(
                    group_name, permission))
                return False
        else:
            print("Error: Invalid group name.")
            return False


    #   Delete permission from permissions list
    #   inputs:
    #       list_name:string variable containing the name of list
    #       permission:string variable containing the permissions to be deleted
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def delete_permission_from_list(self, list_name, permission):
        if (list_name in self.available_api_key_permissions):
            if (permission in self.api_key_permissions[list_name]):
                self.api_key_permissions[list_name].remove(permission)
                return True
            else:
                print("Permission {0} is not inside group {1}.".format(
                    list_name, permission))
                return False
        else:
            print("Error: Invalid list name.")
            return False

    #   Delete permission from permissions group
    #   inputs:
    #       group_name:string variable containing the name of group
    #       permission:string variable containing the permissions to be deleted
    #   outputs:
    #       success:boolean True if operation is successful, False if not
    def delete_permission_from_group(self, group_name, permission):
        if (group_name in self.available_common_api_key_groups):
            if (permission in self.common_api_key_groups[group_name]):
                self.common_api_key_groups[group_name].remove(permission)
                return True
            else:
                print("Permission {0} is not inside group {1}.".format(
                    group_name, permission))
                return False
        else:
            print("Error: Invalid group name")
            return False
