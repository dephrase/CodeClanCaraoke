class Room:
    def __init__(self, name, max_capacity, entry_fee):
        self.name = name
        self.guests = []
        self.songs = []
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.entry_fee = entry_fee
        self.total_cash = 0

    def fullCapacityCheck(self):
        if self.current_capacity == self.max_capacity:
            return True
        else:
            return False

    def customer_can_afford_room_entry_fee(self, guest):
        if guest.wallet < self.entry_fee:
            return False
        else:
            return True

    def checkIn(self, guest):
        fullCapacity = self.fullCapacityCheck()
        canAfford = self.customer_can_afford_room_entry_fee(guest)
        if fullCapacity == True:
            print(f"Sorry, {self.name} is currently at max capacity")
        elif canAfford == False:
            print(f"Unfortunately {guest.name} only has {guest.wallet}, the entry fee is {self.entry_fee}")
        else:
            self.guests.append(guest)
            self.current_capacity += 1
            self.total_cash += self.entry_fee

    def checkOut(self, guest):
        self.guests.remove(guest)
        self.current_capacity -= 1

    def addSong(self, song):
        self.songs.append(song)

    def room_has_favourite_song(self, guest):
        for song in self.songs:
            if song.name == guest.favourite_song:
                return "Whoo!"
        return "Boo!"

        #Add a bar class
        #Bar has an empty list of drinks(dictionarys)
        #Bar has an add drink class, which adds a drink object to the dictionary
        #Drink is the key of the dictionary, value is the amount remaining
        #Room has a take order method
        #Take order method will take a list of dictionarys, key is drink name, value is amount