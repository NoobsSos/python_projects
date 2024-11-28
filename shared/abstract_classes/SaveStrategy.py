from abc import abstractmethod

class SaveStrategy:
    @abstractmethod
    def save(self, data, filename):
        pass