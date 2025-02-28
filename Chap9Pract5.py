# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        print(f"Train {self.name} is created!")
        
    def getStatus(self):
        print(f"The number of seats available in {self.name} are {self.seats}")
    
    def getFare(self):
        print(f"The fare of the ticket is {self.fare}")
        
    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")
    
intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.getFare()
intercity.bookTicket()
print()
print("Thank you for using our services!")