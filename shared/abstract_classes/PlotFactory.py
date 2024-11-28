from abc import abstractmethod

class AbstractPlotFactory:
    @abstractmethod
    def create_plot_strategy(self):
        pass