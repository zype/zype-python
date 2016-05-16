zype-python 0.1.0
-----------------
.. image:: https://travis-ci.org/khfayzullaev/zype-python.svg?branch=master
    :target: https://travis-ci.org/khfayzullaev/zype-python

A simple wrapper around Zype API inspired by SoundCloud API `client <https://github.com/soundcloud/soundcloud-python>`_.

Installation
------------
Run::
    
    pip install zype

To use:

.. code:: python
    
    from zype import Zype
    client = Zype(api_key="<YOUR API KEY>")

Examples
-------

To get all videos available on your account, you can do:

.. code:: python
    
    from zype import Zype
    client = Zype(api_key="<YOUR API KEY>")
    videos = client.get('videos')
    if videos is not None:
        for v in videos:
            print v.title
