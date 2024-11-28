class DataPreparer:
    def __init__(self, data):
        self.data = data

    def prepare_data_for_visualization(self):
        self.data.dropna(inplace=True)
        return self.data