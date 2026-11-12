from bus import BusSystem
from admin import Admin

system = BusSystem()
admin = Admin(system)
while True:
    print("\n***** BUS SYSTEM *****")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")
    try:
        op = int(input("\nEnter your option: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if op == 1:
        if admin.login():
            print("\nLogin successful!")
            admin.admin_menu()
        else:
            print("\nInvalid username or password!")
    elif op == 2:
        try:
            bus_number = int(input("Enter Bus Number: "))
            name = input("Enter Passenger Name: ")
            phone = input("Enter Phone Number: ")
            system.book_ticket(bus_number, name, phone)
        except ValueError:
            print("Invalid bus number!")
    elif op == 3:
        system.show_buses()
    elif op == 4:
        print("Thank you for using our Bus!")
        break
    else:
        print("Invalid option! Please try again.")