from transport import smtp, web

class Sendgrid(object):
    """
    Sendgrid API
    """

    def __init__(self, username, password, secure=True):
        """
        Construct Sendgrid API object

        Args:
            username: Sendgrid uaername
            password: Sendgrid password
            ssl: Use SSL
        """

        self.web = web.Http(username, password, secure)
        self.smtp = smtp.Smtp(username, password, secure)