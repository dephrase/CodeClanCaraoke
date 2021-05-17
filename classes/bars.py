class Bar:
    def __init__(self, name):
        self.name = name
        self.stock = {}

    def add_drink_to_stock(self, drink, stockToAdd):
        if drink in self.stock.keys():
            self.stock[drink] += stockToAdd
        else:
            self.stock[drink] = stockToAdd