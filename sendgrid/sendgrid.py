def memoize(f):
    """
    Memoization decorator
    """
    cache= {}
    def func(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return func


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
        self.username = username
        self.password = password
        self.secure = secure


    @property
    @memoize
    def web(self):
        """
        Return web transport
        """
        from transport import web
        return web.Http(self.username, self.password, self.secure)


    @property
    @memoize
    def smtp(self):
        """
        Return smtp transport
        """
        from transport import smtp
        return smtp.Smtp(self.username, self.password, self.secure)