from shared.abstract_classes.SaveStrategy import SaveStrategy
import csv

class SaveCSV(SaveStrategy):
    def save(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data[0].keys())  # Write headers
            for item in data:
                writer.writerow(item.values())
        print(f"Data saved in CSV format to {filename}")
