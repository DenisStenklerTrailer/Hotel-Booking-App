import pandas

df = pandas.read_csv("hotels.csv", dtype={'id': str})

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id  = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Books a hotel by changing its availabilit to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False ) # index = False, Python does not add another column
    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze() # we get yes/no in return
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.costumer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
        Thank you for your reseration!
        Here is your reservation data:
        Name: {self.costumer_name}
        ID: {self.hotel.hotel_id}
        Hotel: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free...")


