from abc import abstractmethod
import os

class Generator:
    def __init__(self, settings):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._folderToSave = os.path.join(project_root, 'result')
        self._settings = settings

    @property
    def settings(self):
        return self._settings

    @property
    def folderToSave(self):
        return self._folderToSave

    @abstractmethod
    def generate(self):
        pass