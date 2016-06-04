
from functools import partial

from request import make_request
from resource import create_resource


class Zype(object):
    api_entry_point = "api.zype.com"
    auth_type = ""
    auth_val = ""
    protocol = "https://"

    def __init__(self, **kwargs):
        self._set_up(kwargs)

    def _set_up(self, settings):
        self.settings = settings

        self.api_entry_point = self.settings.get(
            'api_entry_point', self.api_entry_point)
        self.protocol = self.settings.get(
            'protocol', self.protocol)

        self._set_up_auth(self.settings)

    def _set_up_auth(self, settings):

        self.auth_type, self.auth_val = self._only_one_auth_type(settings)
        if not self.auth_type or not self.auth_val:
            raise ValueError(
                "At least and and most one of the auth options (api_key, app_key, and access_token) must be provided.")

    def _only_one_auth_type(self, settings):
        default_auth_types = ['app_key', 'api_key', 'access_token']
        auth_type = [key for key in default_auth_types if key in settings]
        auth_type_count = len(auth_type)
        if auth_type_count == 0 or auth_type_count > 1:
            return (None, None)
        else:
            return (auth_type[0], settings[auth_type[0]])

    def __getattr__(self, http_method, **kwargs):
        if http_method not in ('get', 'post', 'put', 'delete'):
            raise AttributeError("HTTP Method is wrong or not spupported.")
        return partial(self._request, http_method, **kwargs)

    def _request(self, http_method, resource, **kwargs):
        uri = self._build_resource_path(resource)
        kwargs.update({self.auth_type: self.auth_val})

        try:
            result = make_request(http_method, uri, kwargs)
        except Exception as e:
            print "Error (zype): " + e.message
            return None
        else:
            return self._handle_result(result)

    def _build_resource_path(self, resource):
        resource = resource.rstrip('/').lstrip('/')
        return '%s%s/%s' % (self.protocol, self.api_entry_point, resource)

    def _handle_result(self, result):
        if result.content:
            return create_resource(result.content)
        else:
            return None
