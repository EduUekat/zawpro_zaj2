class Property:

  def __init__(self, area, rooms, price, address):
    self.area = area
    self.rooms = rooms
    self.price = price
    self.address = address

  def __str__(self):
    return (
        f"Adres: {self.address}, Powierzchnia: {self.area} m², Pokoje:"
        f" {self.rooms}, Cena: {self.price} PLN"
    )

class House(Property):

  def __init__(self, area, rooms, price, address, plot):
    super().__init__(area, rooms, price, address)
    self.plot = plot

  def __str__(self):
    return f"Dom -> {super().__str__()}, Działka: {self.plot} m²"

class Flat(Property):

  def __init__(self, area, rooms, price, address, floor):
    super().__init__(area, rooms, price, address)
    self.floor = floor

  def __str__(self):
    return f"Mieszkanie -> {super().__str__()}, Piętro: {self.floor}"

house_obj = House(
    area=160, rooms=5, price=890000, address="ul. Słoneczna 14, Piaseczno", plot=650
)

flat_obj = Flat(
    area=62, rooms=3, price=540000, address="ul. Marszałkowska 20/4, Warszawa", floor=3
)

print(house_obj)
print(flat_obj)