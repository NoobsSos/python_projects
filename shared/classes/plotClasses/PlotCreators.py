from shared.abstract_classes.PlotFactory import AbstractPlotFactory

from shared.classes.plotClasses.BarStrategy import BarStrategy
from shared.classes.plotClasses.LineStrategy import LineStrategy
from shared.classes.plotClasses.ScatterStrategy import ScatterStrategy
from shared.classes.plotClasses.PieStrategy import PieStrategy

class LinePlot(AbstractPlotFactory):
    def create_plot_strategy(self):
        return LineStrategy()

class ScatterPlot(AbstractPlotFactory):
    def create_plot_strategy(self):
        return ScatterStrategy()

class BarPlot(AbstractPlotFactory):
    def create_plot_strategy(self):
        return BarStrategy()

class PiePlot(AbstractPlotFactory):
    def create_plot_strategy(self):
        return PieStrategy()