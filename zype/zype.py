
from functools import partial

from request import make_request
from resource import create_resource


class Zype(object):
    api_entry_point = "api.zype.com"
    api_key = ""
    protocol = "https://"

    def __init__(self, **kwargs):
        if 'api_key' in kwargs:
            self._set_up(kwargs)
        else:
            raise ValueError("At least an api_key must be provided.")

    def _set_up(self, settings):
        self.settings = settings
        self.api_key = self.settings.get('api_key')
        self.api_entry_point = self.settings.get(
            'api_entry_point', self.api_entry_point)

    def __getattr__(self, http_method, **kwargs):
        if http_method not in ('get', 'post', 'put', 'delete'):
            raise AttributeError("HTTP Method is wrong or not spupported.")
        return partial(self._request, http_method, **kwargs)

    def _request(self, http_method, resource, **kwargs):
        uri = self._build_resource_path(resource)
        kwargs.update(dict(api_key=self.api_key))

        try:
            result = make_request(http_method, uri, kwargs)
        except Exception as e:
            print "Error (zype): " + e.message
            return None
        else:
            return _handle_result(result)

    def _build_resource_path(self, resource):
        resource = resource.rstrip('/').lstrip('/')
        return '%s%s/%s' % (self.protocol, self.api_entry_point, resource)


def _handle_result(result):
    if result.content:
        return create_resource(result.content)
    else:
        return None
