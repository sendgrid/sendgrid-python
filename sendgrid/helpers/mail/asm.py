class ASM(object):

    def __init__(self, group_id=None, groups_to_display=None):
        self.group_id = group_id
        self.groups_to_display = groups_to_display

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    @property
    def groups_to_display(self):
        return self._groups_to_display

    @groups_to_display.setter
    def groups_to_display(self, value):
        self._groups_to_display = value

    def get(self):
        asm = {}
        if self.group_id is not None:
            asm["group_id"] = self.group_id

        if self.groups_to_display is not None:
            asm["groups_to_display"] = self.groups_to_display
        return asm
