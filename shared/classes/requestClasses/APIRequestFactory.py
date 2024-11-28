from shared.classes.requestClasses.GetRequest import GetRequest
import datetime

class APIRequestFactory:

    def __init__(self, settings):
        self.settings = settings

    @staticmethod
    def create_request(self):
        if self.settings.method.lower() == 'get':
            return GetRequest(self.settings.url)
        elif self.settings.method.lower() == 'post':
            return 0
        else:
            raise ValueError("Unknown method")