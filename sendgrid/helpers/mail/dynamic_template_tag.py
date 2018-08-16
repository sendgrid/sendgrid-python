class DynamicTemplateTag(object):
    """A dynamic template tag can be used to be applied to the text and HTML contents of
    the body of your email, as well as in the Subject and Reply-To parameters.
    """

    def __init__(self, key=None, value=None):
        """Create a DynamicTemplateTag with the given key and value.

        :param key: Text to be replaced with "value" param
        :type key: string, optional
        :param value: Value to substitute into email, can be any JSON serializable object
        :type value: any
        """
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        """
        Get a JSON-ready representation of this Substitution.

        :returns: This DynamicTemplateTag, ready for use in a request body.
        :rtype: dict
        """
        dynamic_template_tag = dict()
        if self.key is not None and self.value is not None:
            dynamic_template_tag[self.key] = self.value
        return dynamic_template_tag
