from guest import Guest

class Party:
    def __init__(self, capacity=50):
        # guests => []self.guest_count
        # capactiy => int
        self.guests = []
        self.capacity = capacity

    def welcome_guest(self, guest_name, importance=1, message="Welcome"):
        # make sure we have the capacity
        if(self.current_size() == self.capacity):
            print("sorry bro, no can do")
        else:
            # add name to guest
            print(f"{message}, {guest_name}")
            new_guest = Guest(guest_name, importance)
            self.guests.append(new_guest)
        

    def current_size(self):
        return len(self.guests)

    def boot_guest(self, guest_name):
        # check in name is in our guest list
        for guest in self.guests:
            if guest.name == guest_name:
                self.guests.remove(guest)
                return True
        
        print("Guest not found!")
        # if not, print error message

    def change_size(self, new_size):
        # check if new size exeeds current guest count
        if new_size < self.current_size():
            # if so, we gotta boot some guests
            to_remove = self.current_size() - new_size
            for i in range(to_remove):
                self.guests.pop()
        self.capacity = new_size

rager = Party()
chill_timez = Party()
chill_timez.welcome_guest("Angelo", 5, "Sup")
chill_timez.welcome_guest("Kian", 5, "YO")
chill_timez.welcome_guest("Marco", 2)
chill_timez.welcome_guest("Polo", "MARCO!")
chill_timez.change_size(3)
chill_timez.welcome_guest("Alex", 5, "Greetings!")

print(chill_timez.guests)

