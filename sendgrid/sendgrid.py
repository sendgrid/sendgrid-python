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
    def __init__(self, username, password, **opts):
        """
        Construct Sendgrid API object

        Args:
            username: Sendgrid uaername
            password: Sendgrid password
            secure: Use SSL/TLS
            user: Send mail on behalf of this user (web only)
        """
        self.username = username
        self.password = password
        self.secure = opts.get('secure', True)
        self.user = opts.get('user', None)


    @property
    @memoize
    def web(self):
        """
        Return web transport
        """
        from transport import web
        return web.Http(self.username, self.password, ssl=self.secure, user=self.user)


    @property
    @memoize
    def smtp(self):
        """
        Return smtp transport
        """
        from transport import smtp
        return smtp.Smtp(self.username, self.password, tls=self.secure)
