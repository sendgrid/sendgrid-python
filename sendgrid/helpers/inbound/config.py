"""Setup credentials (.env) and application variables (config.yml)"""
import os
import yaml


class Config(object):
    """All configuration for this app is loaded here"""
    def __init__(self, **opts):
        if os.environ.get('ENV') != 'prod':  # We are not in Heroku
            self.init_environment()

        """Allow variables assigned in config.yml available the following variables
           via properties"""
        self.path = opts.get(
            'path', os.path.abspath(os.path.dirname(__file__))
        )
        with open(self.path + '/config.yml') as stream:
            config = yaml.load(stream)
            self._debug_mode = config['debug_mode']
            self._endpoint = config['endpoint']
            self._host = config['host']
            self._keys = config['keys']
            self._port = config['port']

    @staticmethod
    def init_environment():
        """Allow variables assigned in .env available using
           os.environ.get('VAR_NAME')"""
        base_path = os.path.abspath(os.path.dirname(__file__))
        if os.path.exists(base_path + '/.env'):
            for line in open(base_path + '/.env'):
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]

    @property
    def debug_mode(self):
        return self._debug_mode

    @property
    def endpoint(self):
        return self._endpoint

    @property
    def host(self):
        return self._host

    @property
    def keys(self):
        return self._keys

    @property
    def port(self):
        return self._port
