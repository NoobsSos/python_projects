from shared.abstract_classes.PlotStrategy import PlotStrategy
import matplotlib.pyplot as plt


class PlotContext:
    def __init__(self, strategy: PlotStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PlotStrategy):
        self.strategy = strategy

    def plot(self, data):
        fig, ax = plt.subplots(figsize=(8, 6))
        self.strategy.plot(data, ax)
        plt.show()
