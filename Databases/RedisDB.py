from Databases.Database import Database
import redis


class RedisDB(Database):
    def __init__(self, host='localhost', port=6379, db=0):
        self.db = redis.Redis(host=host, port=port, db=db)
        if not self.db.exists('searches_counter'):
            self.db.set('searches_counter', 0)

    def insert_search(self, query):
        self.db.lpush('searches', query)
        self.db.incr('searches_counter')

    def get_num_of_queries(self):
        return int(self.db.get('searches_counter'))
