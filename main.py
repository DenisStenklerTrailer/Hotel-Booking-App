import pandas

df = pandas.read_csv("hotels.csv", dtype={'id': str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_security = pandas.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id  = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
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


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


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


class CreditCard:
    def __init__(self, number):
        self.number = number
    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration":expiration,"holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_security.loc[df_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

class SpaTicket:
    def __init__(self, costumer_name, hotel_object):
        self.costumer_name = costumer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
                Thank you for your SPA reseration!
                Here is your SPA reservation data:
                Name: {self.costumer_name}
                Hotel: {self.hotel.name}
                """
        return content


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = SpaHotel(hotel_id)


if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())

            spa = input("Do you want to book a spa package?")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(name, hotel)
                print(spa_ticket.generate())
        else:
            print("Credit card authentication failed...")
    else:
        print("There was a problem with your payment...")
else:
    print("Hotel is not free...")


