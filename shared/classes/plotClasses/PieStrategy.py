from shared.abstract_classes.PlotStrategy import PlotStrategy

class PieStrategy(PlotStrategy):
    def plot(self, data, ax):
        categorical_columns = data.select_dtypes(include='number').columns.drop("id", errors="ignore")
        if len(categorical_columns) > 0:
            category_column = categorical_columns[0]
            data[category_column].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
            ax.set_title(f"Distribution of {category_column}")
        else:
            ax.set_title("Not enough data for pie chart.")
