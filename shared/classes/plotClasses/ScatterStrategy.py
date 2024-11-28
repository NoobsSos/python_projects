from shared.abstract_classes.PlotStrategy import PlotStrategy

class ScatterStrategy(PlotStrategy):
    def plot(self, data, ax):
        numeric_columns = data.select_dtypes(include='number').columns
        if len(numeric_columns) >= 2:
            ax.scatter(data[numeric_columns[0]], data[numeric_columns[1]])
            ax.set_xlabel(numeric_columns[0])
            ax.set_ylabel(numeric_columns[1])
            ax.set_title(f"{numeric_columns[1]} vs {numeric_columns[0]}")
        else:
            ax.set_title("Not enough data for scatter plot.")
