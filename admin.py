from bus import Bus


class Admin:
    def __init__(self, bus_system):
        self.username = "admin"
        self.password = "1234"
        self.bus_system = bus_system
        self.is_logged_in = False

    def login(self):
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if self.username == username and self.password == password:
            self.is_logged_in = True
            return True

        self.is_logged_in = False
        return False

    def logout(self):
        self.is_logged_in = False
        print("Logged out successfully!")



    def add_bus(self, number, route, seats):
        if not self.is_logged_in:
            print("Please login first!")
            return


        if seats <= 0:
            print("Invalid seat number!")
            return

        for bus in self.bus_system.buses:
            if bus.number == number:
                print("Bus number already exists!")
                return

        bus = Bus(number, route, seats)
        self.bus_system.buses.append(bus)
        print(f"Bus No. {number} added successfully!")

    def admin_menu(self):
        if not self.is_logged_in:
            print("Please login first!")
            return
        while True:
            print("\n***** ADMIN MENU *****")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            try:
                op = int(input("Enter your option: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
            if op == 1:
                try:
                    number = int(input("Enter Bus Number: "))
                    route = input("Enter Route: ")
                    seats = int(input("Enter Total Seats: "))
                    self.add_bus(number, route, seats)
                except ValueError:
                    print("Invalid input! Number and seats must be numeric.")

            elif op == 2:
                self.bus_system.show_buses()

            elif op == 3:
                self.logout()
                break
            else:
                print("Invalid option!")