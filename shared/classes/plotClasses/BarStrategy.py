from shared.abstract_classes.PlotStrategy import PlotStrategy

class BarStrategy(PlotStrategy):
    def plot(self, data, ax):
        categorical_columns = data.select_dtypes(include=['object', 'category']).columns
        numeric_columns = data.select_dtypes(include='number').columns
        if len(categorical_columns) > 0 and len(numeric_columns) > 0:
            category_column = categorical_columns[0]
            value_column = numeric_columns[0]
            data_grouped = data.groupby(category_column)[value_column].mean()
            data_grouped.plot(kind='bar', ax=ax)
            ax.set_xlabel(category_column)
            ax.set_ylabel(f"Average {value_column}")
            ax.set_title(f"Average {value_column} by {category_column}")
        else:
            ax.set_title("Not enough data for bar chart.")


