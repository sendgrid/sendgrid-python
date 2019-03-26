class DynamicTemplateData(object):
    """In order to send a dynamic template, specify the template ID with the template_id parameter.
    """
    
    def __init__(self, dynamic_template_data=None, p=0):
        """Data for dynamic transactional template.
        Should be JSON-serializeable structure. 

        :param dynamic_template_data: Data for dynamic transactional template.
        :type dynamic_template_data: A JSON-serializeable structure
        :param name: p is the Personalization object or Personalization object index
        :type name: Personalization or integer, optional
        """
        self._dynamic_template_data = None
        self._personalization = None

        if dynamic_template_data is not None:
            self.dynamic_template_data = dynamic_template_data
        if p is not None:
            self.personalization = p

    @property
    def dynamic_template_data(self):
        """Data for dynamic transactional template.

        :rtype: A JSON-serializeable structure
        """
        return self._dynamic_template_data

    @dynamic_template_data.setter
    def dynamic_template_data(self, value):
        self._dynamic_template_data = value

    @property
    def personalization(self):
        return self._personalization

    @personalization.setter
    def personalization(self, value):
        self._personalization = value

    def __str__(self):
        """Get a JSON representation of this object.

        :rtype: A JSON-serializeable structure
        """
        return str(self.get())

    def get(self):
        """
        Get a JSON-ready representation of this DynamicTemplateData object.

        :returns: Data for dynamic transactional template.
        :rtype: A JSON-serializeable structure.
        """
        return self.dynamic_template_data
