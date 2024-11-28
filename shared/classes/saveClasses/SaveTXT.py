from shared.abstract_classes.SaveStrategy import SaveStrategy

class SaveTXT(SaveStrategy):
    def save(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(str(item) + "\n")
        print(f"Data saved in TXT format to {filename}")
