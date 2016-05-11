try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

try:
    import json
except ImportError:
    import simplejson as json

import requests
import six

import logging
# logging.basicConfig(level=logging.INFO)


def format_data(data, prefix=""):
    query_string = {}
    prefixed = lambda key: prefix and "%s[%s]" % (prefix, key) or key
    for key, value in six.iteritems(data):
        if isinstance(value, dict):
            query_string.update(format_data(value, prefix=key))
        else:
            query_string[prefixed(key)] = value
    return query_string


def get_request_settings():
    settings = {
        'allow_redirects': 'false',
        'headers': {
            'content-type': 'application/json',
            'accept': 'application/json',
            'User-Agent': ""
        }
    }
    return settings


def add_query_string(url, params):
    query_string = urlencode(params)
    if '?' in url:
        url_with_query_string = '%s&%s' % (url, query_string)
    else:
        url_with_query_string = '%s?%s' % (url, query_string)
    return url_with_query_string


def make_request(method, url, params):
    request_function = getattr(requests, method, None)
    if request_function is None:
        raise TypeError('Unknown method: %s' % (method,))

    kwargs = get_request_settings()

    if method == 'get' or method == 'delete':
        url = add_query_string(url, params)
        result = request_function(url, **kwargs)
    else:
        kwargs['data'] = json.dumps(format_data(params))
        result = request_function(url, **kwargs)

    try:
        result.raise_for_status()
        return result
    except requests.exceptions.HTTPError as e:
        print "Error (request): ", e.message
        raise
