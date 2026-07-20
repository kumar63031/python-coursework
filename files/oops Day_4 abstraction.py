
'''

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")
    def viewhistory(self):
        print("You can see your transactions")
    def userinfo(self):
        print("You can see your details")
    def transactions(self):
        print("You can transfer money through netbanking")

    @abstractmethod
    def depoist(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass


class CurrentAccount(BankAccount):
    def depoist(self):
        print("You can depoist - CA")
    def withdraw(self):
        print("You can Withdraw - CA")

class SavingsAccount(BankAccount):
    def depoist(self):
        print("You can depoist - SA")
    def withdraw(self):
        print("You can Withdraw - SA")


class FixedDepoist(BankAccount):
    def depoist(self):
        print("You can depoist - FD")
    def withdraw(self):
        print("You can Withdraw - FD") 


class SalaryAccount(BankAccount):
    def depoist(self):
        print("You can depoist - SAA")
    def withdraw(self):
        print("You can Withdraw - SAA")


class ZeroBalanceAccount(BankAccount):
    def depoist(self):
        print("You can depoist - ZBA")
    def withdraw(self):
        print("You can Withdraw - ZBA")

subbu = ZeroBalanceAccount()
subbu.depoist()
subbu.withdraw()
subbu.checkbalance()
subbu.userinfo()
subbu.transactions()
subbu.viewhistory()

kumar = SavingsAccount()
kumar.depoist()
kumar.withdraw()
kumar.checkbalance()
kumar.userinfo()
kumar.transactions()
kumar.viewhistory()

'''

# Bus Booking
class Bus:
    def __init__(self, bus_no, route, seats):
        self.bus_no = bus_no
        self.route = route
        self.seats = seats

    def show_bus(self):
        print(f"Bus No : {self.bus_no}")
        print(f"Route  : {self.route}")
        print(f"Seats Available : {self.seats}")


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Booking:
    def book_ticket(self, bus, passenger):
        if bus.seats > 0:
            bus.seats -= 1
            print("\nTicket Booked Successfully!")
            print("---------------------------")
            print(f"Passenger : {passenger.name}")
            print(f"Age       : {passenger.age}")
            print(f"Bus No    : {bus.bus_no}")
            print(f"Route     : {bus.route}")
            print(f"Seats Left: {bus.seats}")
        else:
            print("Sorry! No seats available.")


# Create Bus Object
bus1 = Bus("TS09AB1234", "Hyderabad -> Vijayawada", 3)

# Show Bus Details
bus1.show_bus()

# Passenger Details
name = input("\nEnter Passenger Name: ")
age = int(input("Enter Age: "))

passenger1 = Passenger(name, age)

# Book Ticket
booking = Booking()
booking.book_ticket(bus1, passenger1)

# Show Updated Seats
print("\nUpdated Bus Details")
bus1.show_bus()


















