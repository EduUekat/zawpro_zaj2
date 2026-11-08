from library import Book, Employee, Library, Order
from property_cls_zad3 import Flat, House
from student import Student

print("zad_1 z python_oop")
stud1 = Student("Anna Kowalska", [60, 70, 80])
print(f"{stud1.name} zdał(a)? {stud1.is_passed()}")

print("\nzad_2 z python_oop")
lib1 = Library("Warszawa", "Marszałkowska 10", "00-001", "8:00 - 20:00", "221112233")
emp1 = Employee(
    "Adam",
    "Mickiewicz",
    "2020-03-01",
    "1990-12-24",
    "Warszawa",
    "Nowy Świat 5",
    "00-496",
    "500600700",
)
book1 = Book(lib1, "2020", "Henryk", "Sienkiewicz", 450)
order1 = Order(emp1, stud1, [book1], "2026-06-10")
print(order1)

print("\nzad_3 z python_oop")
house_obj = House(
    area=160, rooms=5, price=890000, address="ul. Słoneczna 14, Piaseczno", plot=650
)
print(house_obj)
