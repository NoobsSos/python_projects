from abc import abstractmethod


class Request:
    def __init__(self, url):
        self.url = url
    @abstractmethod
    def send(self):
        pass