from __future__ import absolute_import, division, print_function, unicode_literals
import requests
from copy import deepcopy
import json
import warnings

class Client(object):
    _methods = ("get", "post", "put", "delete", "head", "options", "trace", "connect", "patch")

    def __init__(self, url="", oauth=None, **kwargs):
        _getattr = super(Client, self).__getattribute__
        self._attributes = attributes = {
            "_path": [url],
            "method": "get",
        }
        # we don't store http/oauth client in _attributes b/c don't want it deepcloned
        http = kwargs.pop("_http", requests)
        self._http = oauth or http
        method = kwargs.pop("method", "GET")
        attributes["method"] = method.lower()
        attributes.update(kwargs)

    def __getattribute__(self, name):
        _getattr = super(Client, self).__getattribute__
        attributes = _getattr("_attributes")
        attributes = deepcopy(attributes)
        # Hack to get around global keyword issue
        if name == "global_":
            name = "global"
        attributes["_path"].append(name)
        attributes["oauth"] = _getattr("_http")
        return Client(**attributes)

    def __repr__(self):
        _getattr = super(Client, self).__getattribute__
        attributes = _getattr("_attributes")
        return "%s: %s" % (attributes["method"], self._getUrl())

    def __call__(self, *args, **kwargs):
        """
        if an http method is called, set the method to that method and make a request
        if a method is called which actually exists on the client (e.g. request, getArgs, etc.)
        call that method.
        otherwise, update the arguments dict with the callees name, and the value of the arg or kwargs
        >>> x = Client("example.com")._setArgs(params={"first": "Jane", "last": "Jones"}, method="post")
        >>> y = x.method("put")
        >>> y.getArgs()["method"] == 'put'
        True
        >>> y = x.params(first="Jim")
        >>> y.getArgs()["params"] == {'last': 'Jones', 'first': 'Jim'}
        True
        if not called with any arguments, delete the argument from the arguments dict
        >>> y = x.params()
        >>> "params" in y.getArgs()
        False
        """
        _getattr = super(Client, self).__getattribute__
        attributes = _getattr("_attributes")
        calledAttr = attributes["_path"].pop()

        # handle a method call (ie GET, POST)
        methods = _getattr("_methods")
        if calledAttr.lower() in methods:
            # create new client with updated method, and call it
            return self._setArgs(method=calledAttr.lower()).request(*args, **kwargs)
        try:
            return _getattr(calledAttr)(*args, **kwargs)
        except AttributeError:
            # if there is no attribute to call, then we presume it is an attr to be added to the attribute dict
            if args:
                return self._setArgs(**{calledAttr: args[0]})
            elif kwargs:
                return self._setArgs(**{calledAttr: kwargs})
            else:
                return self._delArgs(calledAttr)

    def request(self, *args, **kwargs):
        """
        make a request to the server. Any kwargs passed to request will override the
        attributes passed to requests.request.
        calls the function at dataFilter with the contents of the data
        attribute iff dataFilter and data exist
        runs the url through format (http://docs.python.org/2/library/string.html#formatspec)
        passing as arguments any *args passed to request.
        """
        # update with any last-minute modifications to the attributes
        c = self._setArgs(**kwargs) if kwargs else self
        attributes = c._cloneAttributes()
        requests = attributes.pop("_http")

        # run the data through the dataFilter if both exist
        if "data" in attributes and "dataFilter" in attributes:
            attributes["data"] = attributes["dataFilter"](attributes["data"])

        # format and set the url
        attributes["url"] = c._getUrl().format(*args)

        # remove uneeded attributes
        for attr in ["_path", "dataFilter"]:
            attributes.pop(attr, None)

        #make the request
        return requests.request(**attributes)

    def oauth(self, rauth):
        """
        provide a fully authenticated rauth oauth client
        """
        return self._setArgs(oauth=rauth)

    def getArgs(self):
        """
        return the arguments currently stored in this client object.
        >>> x = Client("example.com")
        >>> args = x.getArgs()
        >>> del args['_http'] # for testing purposes - args['_http'] different on every machine
        >>> args == {'method': 'get', '_path': ['example.com']}
        True
        the returned arguments are actually deep copies - cannot be used to modify the client arguments
        >>> args['method']='put'
        >>> x.getArgs()['method'] == 'get'
        True
        """
        return self._cloneAttributes()

    def _setArgs(self, *args, **kwargs):
        """
        passed kwargs will update and override existing attributes.
        >>> x = Client("example.com")._setArgs(params={"first": "Jane", "last": "Jones"}, method="post")
        >>> y = x._setArgs(method="put")
        >>> y.getArgs()["method"] == 'put'
        True
        >>> y.getArgs()["params"] == {'last': 'Jones', 'first': 'Jane'}
        True
        if an existing attribute is a dict, and replacement is a dict,
        then update the attribute with the new value
        >>> y = x._setArgs(params={"first": "Jim"})
        >>> y.getArgs()["params"] == {'last': 'Jones', 'first': 'Jim'}
        True
        """
        attributes = self._cloneAttributes()
        # update rather than replace attributes that can be updated

        for k, v in attributes.items():
            if k in kwargs and hasattr(v, "update") and hasattr(kwargs[k], "update"):
                v.update(kwargs[k])
                del kwargs[k]
        attributes.update(kwargs)
        return Client(**attributes)

    def setArgs(self, **kwargs):
        warnings.warn("setArgs is deprecated; will be removed in 0.7. Change arg by calling method with arg name, e.g. client.method('get').", DeprecationWarning)
        self._setArgs(self, **kwargs)

    def _delArgs(self, *args):
        """
        passed args will be deleted from the attributes hash. No error will
        throw if the attribute does not exist.
        >>> x = Client('http://example.com')._setArgs(hello='world')
        >>> x.getArgs()['hello'] == 'world'
        True
        >>> y = x._delArgs('hello')
        >>> 'hello' in y.getArgs()
        False
        """
        attributes = self._cloneAttributes()
        for attr in args:
            attributes.pop(attr)
        return Client(**attributes)

    def delArgs(self, *args):
        warnings.warn("delArgs is deprecated; will be removed in 0.7. Delete arg by calling method with arg name with no value, e.g. client.method().", DeprecationWarning)
        self._delArgs(self, *args)

    def _(self, pathPart):
        """
        append a path part to the url. Should be used when the pathPart to
        append is not valid python dot notation. Can use positional, but
        not named, string formatters, ie {} or {3}, but not {name}.
        >>> x = Client('http://example.com')._("{1}").hello._("{0}")
        >>> x
        get: http://example.com/{1}/hello/{0}
        Can then replace those positionals with args passed to request
        >>> resp = x.request('zero', 'one')
        >>> resp.request.url
        'http://example.com/one/hello/zero'
        Will ensure the path part is a string:
        >>> x = Client('http://example.com')._(1).hello
        >>> x
        get: http://example.com/1/hello
        """
        attributes = self._cloneAttributes()
        attributes["_path"].append(str(pathPart))
        return Client(**attributes)

    def _cloneAttributes(self):
        """
        get all attributes, cloning occurrs in __getattribute__, so don't
        have to do twice
        """
        _getattr = super(Client, self).__getattribute__
        attributes = _getattr("_attributes")
        attributes["_http"] = _getattr("_http")
        return attributes

    def _getUrl(self):
        """
        get the url from _path
        """
        attributes = self._cloneAttributes()
        return "/".join(attributes["_path"])

    def __dir__(self):
        _getattr = super(Client, self).__getattribute__
        methods = _getattr("methods")
        methods += ("setArgs", "getArgs", "delArgs", "_", "oauth", "request")
        return list(methods)

jsonFilter = lambda data: json.dumps(data)

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'absolute_import': absolute_import, 'print_function': print_function, 'unicode_literals': unicode_literals})