from shared.abstract_classes.PlotFactory import AbstractPlotFactory
from shared.classes.plotClasses.PlotCreators import LinePlot, ScatterPlot, BarPlot, PiePlot

import matplotlib.pyplot as plt

class UniversalVisualizer:
    def __init__(self, data):
        self.data = data

    def plot(self, factory: AbstractPlotFactory):
        strategy = factory.create_plot_strategy()
        fig, ax = plt.subplots(figsize=(8, 6))
        strategy.plot(self.data, ax)
        plt.show()

    def plot_all_in_one(self):
        factories = [LinePlot(), ScatterPlot(), BarPlot(), PiePlot()]
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        for i, factory in enumerate(factories):
            strategy = factory.create_plot_strategy()
            strategy.plot(self.data, axs[i // 2, i % 2])

        plt.tight_layout()
        plt.show()