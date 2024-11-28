class SaveContext:
    def __init__(self, save_strategy):
        self.save_strategy = save_strategy

    def set_save_strategy(self, save_strategy):
        self.save_strategy = save_strategy

    def save_data(self, data, filename):
        self.save_strategy.save(data, filename)