from redis import StrictRedis
from common.config import yeti_feeds_config
from redis import PubSubError


class Streamer:
    def __init__(self):
        self.red = StrictRedis(host=yeti_feeds_config.get('async',
                                                          'redis_server')
                               , port=yeti_feeds_config.get('async',
                                                            'redis_port'),
                               db=2)

    def publish(self, name_queue, data):
        if self.red and data and name_queue:
            try:
                self.red.publish(name_queue, data)
                return True
            except PubSubError:
                return False
            except ConnectionError:
                return False
            except TimeoutError:
                return False
