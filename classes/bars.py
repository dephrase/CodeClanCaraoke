class Bar:
    def __init__(self, name):
        self.name = name
        self.stock = {}
        self.tab = {}
        self.tab_list = {}

    def add_drink_to_stock(self, drink, stockToAdd):
        if drink in self.stock.keys():
            self.stock[drink] += stockToAdd
        else:
            self.stock[drink] = stockToAdd

    def order_drink(self, drink):
        if drink in self.stock.keys():
            if drink in self.tab.keys():
                self.tab[drink] += 1
            else:
                self.tab[drink] = 1

    def start_tab(self, room):
        if not room.name in self.tab_list.keys():
            self.tab_list[room.name] = {}

    # def request_tab(self, bar):
    #     total_cost = 0
    #     for drink in bar.tab:
    #         pass