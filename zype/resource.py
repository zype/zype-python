try:
    from UserList import UserList
except ImportError:
    from collections import UserList

try:
    import json
except ImportError:
    import simplejson as json


class ZypeResource(object):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return json.dumps(self.data)

    def __getstate__(self):
        return self.data.items()

    def __setstate__(self, items):
        if not hasattr(self, 'data'):
            self.data = {}
        for key, val in items:
            self.data[key] = val

    def __getattr__(self, name):
        if name in self.data:
            return self.data.get(name)
        raise AttributeError("Attribute is not found.")

    def attrs(self):
        return self.data.keys()


class ZypeResourceList(UserList):

    def __init__(self, resources=[]):
        data = [ZypeResource(resource) for resource in resources]
        super(ZypeResourceList, self).__init__(data)


def create_resource(d):
    """Return a response wrapped in the appropriate wrapper type."""
    try:
        data = json.loads(d)['response']
    except Exception as e:
        print "Error (resource): " + e.message
        return None

    if isinstance(data, list):
        resource = ZypeResourceList(data)
    else:
        resource = ZypeResource(data)
    resource.raw_data = data

    return resource
