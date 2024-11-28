from ui.MenuItem import MenuItem
from ui.MenuBuilder import MenuBuilder

from shared.classes.dataClasses.DataLoader import DataLoader
from shared.classes.dataClasses.DataAnalyzer import DataAnalyzer
from shared.classes.dataClasses.DataPreparer import DataPreparer
from shared.classes.dataClasses.UniversalVisualizer import UniversalVisualizer

from shared.classes.plotClasses.BarStrategy import BarStrategy
from shared.classes.plotClasses.PlotContext import PlotContext
from shared.classes.plotClasses.LineStrategy import LineStrategy
from shared.classes.plotClasses.ScatterStrategy import ScatterStrategy
from shared.classes.plotClasses.PieStrategy import PieStrategy

class PlotRunner:
    def menu(self):
        while True:
            try:
                filepath = input("Please enter the filepath for the data file (e.g., 'data.csv'): ")

                # Validate file
                with open(filepath, 'r') as f:
                    pass
                break

            except FileNotFoundError:
                print(f"Error: The file '{filepath}' does not exist. Please try again.")
            except IOError:
                print(f"Error: The file '{filepath}' could not be opened. Check permissions or file format.")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again with a valid file.")

        loader = DataLoader(filepath)
        data = loader.get_data()

        analyzer = DataAnalyzer(data)
        preparer = DataPreparer(data)
        prepared_data = preparer.prepare_data_for_visualization()
        visualizer = UniversalVisualizer(prepared_data)

        def print_diagrams():
            context = PlotContext(LineStrategy())
            context.plot(prepared_data)

            context.set_strategy(ScatterStrategy())
            context.plot(prepared_data)

            context.set_strategy(BarStrategy())
            context.plot(prepared_data)

            context.set_strategy(PieStrategy())
            context.plot(prepared_data)

            visualizer.plot_all_in_one()

        def print_extreme_values():
            print(analyzer.get_extreme_values())

        menu_items = [
            MenuItem("1", "Print Diagrams", print_diagrams),
            MenuItem("2", "Print Extreme Values", print_extreme_values),
            MenuItem("0", "Exit", exit),
        ]

        menu_builder = MenuBuilder(menu_items)
        while True:
            menu_builder.initialize()
