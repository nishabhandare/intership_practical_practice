print("WELCOME IN FLIGHT BOOKING APPLICATION")
class Flight:
    def __init__(self,code,airline,route,seats,fare):
        self.code=code
        self.airline = airline
        self.route=route
        self.seats=seats
        self.fare=fare
    def details(self):
        print(self.code,self.airline,self.route,self.seats,self.fare)     
flight1 = Flight("PB102", "Air India","Pune → Delhi",20,4000)
flight2 = Flight("MD200","IndiGo","Mumbai → Bengaluru",15,3500)
flight3 = Flight("PF301", "SpiceJet","Pune → Hyderabad",25,3000)
flights=[flight1,flight2,flight3] 

class Booking:
    next_id = 12301

    def __init__(self):
        self.booking_id = Booking.next_id
        Booking.next_id += 1
    
    def select_passenger_type(self):
        print("1. Regular Passenger")
        print("2. Student Passenger")
        choice = int(input("Choose passenger type: "))
        match choice:
            case 1:
                return "regular"
            case 2:
                return "student"
            case _:
                print("Invalid choice. Try again.")
                return self.select_passenger_type()

    def select_flight(self):
        while True:
            print("Available Flights:")
            for f in flights:
                f.details()

            code = input("Enter Flight Code: ").strip().upper()

            for f in flights:
                if f.code == code:
                    self.selected_flight = f
                    return

            print("Invalid Flight Code. Please try again.")
    
    def information(self):
        self.select_flight()

        self.passenger_name = input("Enter passenger name: ")
        self.age = int(input("Enter age: "))
        if self.age <= 0:
            print("Age must be greater than 0.")
            return False
        self.passenger_type = self.select_passenger_type()
        if self.passenger_type == "student":
            self.passenger = StudentPassenger(
                self.passenger_name, self.age
                )
        else:
            self.passenger = RegularPassenger(
                self.passenger_name, self.age
                )
    
        self.ticket_count = int(input("Enter ticket count: "))

        if self.ticket_count <= 0:
            print("Ticket count must be greater than 0.")
            return False

        if self.ticket_count > self.selected_flight.seats:
            print("Not enough seats available!")
            return False

        return True

        
    def fare_calculation(self):
        discount = self.passenger.discount()
        self.subtotal = self.selected_flight.fare * self.ticket_count
        self.student_discount = self.subtotal * discount / 100
        self.final_fare = self.subtotal - self.student_discount
        print("Subtotal:", self.subtotal)
        print("Discount:", self.student_discount)
        print("Final Amount:", self.final_fare)
b = None           

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def discount(self):
        return 0

class RegularPassenger(Passenger):
    def discount(self):
        return 0

class StudentPassenger(Passenger):
    def discount(self):
        return 10

while True:
    print("\nMain Menu:")
    print("1. View Flights \n2. Book Flight \n3. View Booking \n4. Exit.\n")
    choice=int(input("Enter your Choice: "))
    match choice:
        case 1:
            print("\nViewing Flights...")
            for flight in flights:
                flight.details()
                break
        case 2:
            print("\nBooking Flight...")
            new_booking = Booking()

            if new_booking.information():
                new_booking.fare_calculation()
                new_booking.selected_flight.seats -= new_booking.ticket_count
                b = new_booking
                print("Booking successful!")
            else:
                print("Booking failed!")
                
            
        case 3:
            if b is None:
                print("No booking found. Please book a flight first.")
            else:
                print("\nViewing Booking...")
                print("--Booking Summary--")
                print("Booking ID:", b.booking_id)
                print("Passenger Name:", b.passenger_name)
                print("Age:", b.age)
                print("Passenger Type:", b.passenger_type)
                print("\nFlight Code: ", b.selected_flight.code)
                print("Airline: ", b.selected_flight.airline)
                print("Route: ", b.selected_flight.route)
                print("Number of Tickets: ", b.ticket_count)
                print("Base fare per Ticket: ", b.selected_flight.fare)
                print("subtotal: ", b.subtotal)
                print("Student Discount: ", b.student_discount)
                print("Final Amount: ", b.final_fare)

        case 4:
            print("\nThank You for visiting Kiran Airport")
            break
        case _:
            print("\nInvalid choice. Please try again.")