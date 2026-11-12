# 🚌 Bus Reservation System

A simple **Bus Reservation System** built using Python and Object-Oriented Programming (OOP). This console-based application allows passengers to book bus tickets and administrators to manage buses.

## ✨ Features

### 👨‍💼 Admin Features
- Secure admin login.
- Add new buses.
- View all available buses.
- Logout from the admin panel.
- Prevent unauthorized bus management.

### 🎫 Passenger Features
- View available buses.
- Book bus tickets.
- Check seat availability.
- Receive ticket booking details.
- Fixed ticket fare of **৳500** per seat.

## 🔐 Admin Login Credentials

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `1234` |

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python Modules and Classes
- Lists and Objects

## 📂 Project Structure

```text
Bus_Reservation_System/
│
├── main.py
├── admin.py
├── bus.py
├── passenger.py
└── README.md
```


** Run the application**

```bash
python main.py
```

## 📋 Main Menu

```text
========== BUS RESERVATION SYSTEM ==========

1. Admin Login
2. Book Ticket
3. View Buses
4. Exit
```

## ⚙️ OOP Concepts Implemented

- **Classes and Objects:** Used to represent buses, passengers, administrators, and the reservation system.
- **Encapsulation:** Organizes data and related methods within classes.
- **Object Relationships:** Passengers maintain a reference to their booked bus.
- **Composition:** The `BusSystem` manages bus and passenger objects.
- **Methods:** Used to handle login, bus management, seat booking, and availability.

## 💰 Ticket Information

| Item | Details |
|---|---|
| Ticket Fare | ৳500 |
| Booking Method | One seat per booking |
| Seat Management | Automatic seat availability update |

## 🎯 Project Objective

The main objective of this project is to practice Python Object-Oriented Programming by developing a real-world bus reservation application with separate admin and passenger functionalities.

---
