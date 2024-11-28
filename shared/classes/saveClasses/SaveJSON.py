from shared.abstract_classes.SaveStrategy import SaveStrategy
import json

class SaveJSON(SaveStrategy):
    def save(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved in JSON format to {filename}")