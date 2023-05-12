from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def insert_search(self, query):
        pass

    @abstractmethod
    def get_num_of_queries(self):
        pass
