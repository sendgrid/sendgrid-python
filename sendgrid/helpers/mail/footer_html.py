class FooterHtml(object):
    """The FooterHtml of an Attachment."""

    def __init__(self, footer_html=None):
        """Create a FooterHtml object

        :param footer_html: The html content of your footer.
        :type footer_html: string, optional
        """
        self._footer_html = None
        
        if footer_html is not None:
            self.footer_html = footer_html

    @property
    def footer_html(self):
        """The html content of your footer.

        :rtype: string
        """
        return self._footer_html

    @footer_html.setter
    def footer_html(self, value):
        self._footer_html = value

    def get(self):
        """
        Get a JSON-ready representation of this FooterHtml.

        :returns: This FooterHtml, ready for use in a request body.
        :rtype: string
        """
        return self.footer_html