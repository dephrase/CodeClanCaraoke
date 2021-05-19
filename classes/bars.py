class Bar:
    def __init__(self, name):
        self.name = name
        self.stock = {}
        self.tab_list = {}

    def add_drink_to_stock(self, drink, stockToAdd):
        if drink in self.stock.keys():
            self.stock[drink] += stockToAdd
        else:
            self.stock[drink] = stockToAdd

    def order_drink(self, drink, room):
        if drink in self.stock.keys():
            if drink in self.tab_list[room.name].keys():
                self.tab_list[room.name][drink] += 1
            else:
                self.tab_list[room.name][drink] = 1

    def start_tab(self, room):
        if not room.name in self.tab_list.keys():
            self.tab_list[room.name] = {}

    def request_tab_cost(self, room):
        cost = 0
        for drink, amount in self.tab_list[room.name].items():
            cost += drink.price * amount
        return cost

    # def pay_tab(self, room):
    #     tab_cost = self.request_tab_cost(room)
    #     group_cash = 0
    #     for guest in room.guests:
    #         group_cash += guest.wallet
    #     if group_cash >= tab_cost:

    #         return True
    #     else:
    #         return False
