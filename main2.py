import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={'id': str})


class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self,hotel_id):
        self.hotel_id  = hotel_id # Instance variable
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze() # Instance variable

    def book(self):
        """Books a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False) # index = False, Python does not add another column

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze() # we get yes/no in return
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # MAGIC METHODS
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id
            return True
        else:
            return False

# Abstract class means that all classes with Ticket in our case MUST include the generate()
# This is actually to remind the programmer that we need to use the generate() otherwise we get an error
class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.costumer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
        Thank you for your reseration!
        Here is your reservation data:
        Name: {self.the_customer_name}
        ID: {self.hotel.hotel_id}
        Hotel: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.costumer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        return "Hello, this is your digital ticket"
    def download(self):
        pass


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.available()) # Instance method
print(Hotel.get_hotel_count(data=df)) # Class method
print(hotel1.get_hotel_count(data=df)) # Class method

print(hotel1.name) # Instance variable
print(hotel2.name) # Instance variable

print(hotel1.watermark) # Class variable
print(hotel2.watermark) # Class variable

print(Hotel.watermark)

ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1) # property
print(ticket.the_customer_name) # Actually behaves like a variable
print(ticket.generate())

converted = ReservationTicket.convert(10) # static  method
print(converted)
