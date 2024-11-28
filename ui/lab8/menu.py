from classes.dataClasses.DataLoader import DataLoader
from classes.dataClasses.DataAnalyzer import DataAnalyzer
from classes.dataClasses.DataPreparer import DataPreparer
from classes.dataClasses.UniversalVisualizer import UniversalVisualizer

from classes.plotClasses.PlotContext import PlotContext
from shared.classes.plotClasses.BarStrategy import BarStrategy
from classes.plotClasses.LineStrategy import LineStrategy
from classes.plotClasses.ScatterStrategy import ScatterStrategy
from classes.plotClasses.PieStrategy import PieStrategy


def menu():

    while True:
        try:
            filepath = input("Please enter the filepath for the data file (e.g., 'data.csv'): ")

            # Attempt to open the file to check if it exists and is accessible
            with open(filepath, 'r') as f:
                pass  # Simply opening and closing the file to validate its existence and readability
            break  # Exit the loop if the file is valid

        except FileNotFoundError:
            print(f"Error: The file '{filepath}' does not exist. Please try again.")
        except IOError:
            print(f"Error: The file '{filepath}' could not be opened. Check permissions or file format.")
        except Exception as e:
            print(f"An error occurred while trying to access the file: {e}")
            print("Please try again with a valid file.")
    loader = DataLoader(filepath)
    data = loader.get_data()

    analyzer = DataAnalyzer(data)

    preparer = DataPreparer(data)
    prepared_data = preparer.prepare_data_for_visualization()

    visualizer = UniversalVisualizer(prepared_data)
    while True:
        print("1. Print diagrams")
        print("2. Print extreme values")
        print("3. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                context = PlotContext(LineStrategy())
                context.plot(prepared_data)

                context.set_strategy(ScatterStrategy())
                context.plot(prepared_data)

                context.set_strategy(BarStrategy())
                context.plot(prepared_data)

                context.set_strategy(PieStrategy())
                context.plot(prepared_data)

                visualizer.plot_all_in_one()

            case "2":
                print(analyzer.get_extreme_values())
            case _:
                break