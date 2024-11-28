from abc import abstractmethod

class PlotStrategy():
    @abstractmethod
    def plot(self, data, ax):
        pass