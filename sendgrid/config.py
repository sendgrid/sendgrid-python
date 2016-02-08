import os

class Config(object):
    """All configuration for this app is loaded here"""
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):  # We are not in Heroku
            self.init_environment()

    @staticmethod
    def init_environment():
        """Allow variables assigned in .env available using
           os.environ.get('VAR_NAME')"""
        base_path = os.path.abspath('./')
        if os.path.exists(base_path + '/.env'):
            for line in open(base_path + '/.env'):
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]