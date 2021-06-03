import re

import redis.exceptions
from redis import Redis
import os

# Build Server class


class Server:
    def __init__(self):
        self.redis_host = "127.0.0.1"
        self.r = Redis(self.redis_host)

    def ping_start(self):
        retry = 0
        if retry < 6:
            try:
                self.r.ping()
                print("Connected!")
            except redis.exceptions.ConnectionError:
                print("Redis server not started, attempting start now...")
                retry = retry + 1
                os.system("/usr/bin/systemctl start redis")
        else:
            print("Failed to connect 5 times, is redis on the default port?")
            exit()

    def wipe_redis(self):
        self.r.flushdb()

    def add_string(self, key, value):
        self.r.set(key, value)

    def search(self, term):
        term_match = re.compile(".*" + term + ".*", re.IGNORECASE)
        result = []
        for key in self.r.scan_iter():
            matches = term_match.findall(key.decode("utf-8"))
            for each in matches:
                result.append(each)
        return result


