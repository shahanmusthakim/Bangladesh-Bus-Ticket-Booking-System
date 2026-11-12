from passenger import Passenger
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    def available_seats(self):
        return self.total_seats - self.booked_seats
    def book_seat(self, seats):
        if seats <= 0:
            return False
        if self.booked_seats + seats <= self.total_seats:
            self.booked_seats += seats
            return True
        return False

class BusSystem:
    FARE = 500
    def __init__(self):
        self.buses = []
        self.passengers = []
    def show_buses(self):
        print("\n***** ALL AVAILABLE BUSES *****\n")

        if not self.buses:
            print("No buses available")
            return
        for bus in self.buses:
            print(f"Bus Number: {bus.number}")
            print(f"Route: {bus.route}")
            print(f"Total Seats: {bus.total_seats}")
            print(f"Available Seats: {bus.available_seats()}")
            print(f"Ticket Fare: Tk. {self.FARE}")
            print("----------------------------------------")

    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:

                if bus.available_seats() > 0:
                    if bus.book_seat(1):
                        passenger = Passenger(name, phone, bus)
                        self.passengers.append(passenger)

                        print("\n***** TICKET *****")
                        print(f"Passenger Name: {name}")
                        print(f"Phone Number: {phone}")
                        print(f"Bus Number: {bus.number}")
                        print(f"Route: {bus.route}")
                        print(f"Ticket Fare: Tk. {self.FARE}")
                        print("Ticket booked successfully!")
                        print("====================================")
                        return
                print("Sorry! No available seats.")
                return
        print("Bus not found!")