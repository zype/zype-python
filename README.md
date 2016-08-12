zype-python
===========

[![Build Status](https://travis-ci.org/khfayzullaev/zype-python.svg?branch=master)](https://travis-ci.org/khfayzullaev/zype-python)

A simple wrapper around Zype API inspired by [SoundCloud API client](https://github.com/soundcloud/soundcloud-python). For instance, you can use the module to build custom web apps based on Python frameworks, like Flask, Django.

It is really easy to use it. To illustrate, in order to get all videos from your account, you can simply do:

```python
from zype import Zype
client = Zype(api_key="<YOUR API KEY>")
videos = client.get('videos')
if videos is not None:
    for v in videos:
        print v.title
```

Installation
------------

`$ pip install zype`

Contribute
----------

- Issue tracker: [https://github.com/khfayzullaev/zype-python/issues](https://github.com/khfayzullaev/zype-python/issues)
- Source code: [https://github.com/khfayzullaev/zype-python](https://github.com/khfayzullaev/zype-python)

Setting up the project
----------------------

1. Clone the project `git clone https://github.com/khfayzullaev/zype-python.git`
2. Then, in the project root (`$ cd zype-python`):
	* 	`$ virtualenv venv`
	* 	`$ . venv/bin/activate`
	* 	`$ pip install -r requirements.txt`
3. Run tests `python setup.py test`

Support
-------

If you are having issues, please let me know: **khurshidfayzullaev@yahoo.com**

License
-------

The project is licensed under the Apache License 2.0 license.
