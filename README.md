# Status_updater
Simple realtime status upadter  service demonstrated by creating a pizza order tracking app. Made with <b>Django channels</b> & <b>Redis</b>.
It is mostly based on <b>Web sockets</b> which send events to frontend when a signal generates from Database.

<b>Redis</b> is working as a channel layer.For example,in the tutorial section of channels <a href="https://channels.readthedocs.io/en/latest/tutorial/index.html">Documentation</a>, it is clear that Redis is used as a storage layer for channel names and group names. These are stored within Redis so that they can be accessed from any consumer instance. If for example, I create a group called 'users' and then add 3 different channel names to it, this information is stored in Redis. Now, whenever I want to send data to the channels in the group I can simply reference the group from my consumer and Django-channels will automatically retrieve the channel names stored under that group in Redis.

On the other hand, if you want to use consumers in a non-conventional way, that is, as background workers then Redis becomes a message queue. That's because when you send a message containing a task to be done by one of the background workers (a consumer that 'consumes' the tasks) those messages have to be stored somewhere so that the background workers can retrieve them as they finish up other tasks.

![](Hnet-image.gif)

You can add redis by defining it in the project/settings.py 
-----
Set up the channel layer in your Django settings file like so::

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("localhost", 6379)],
            },
        },
    }
