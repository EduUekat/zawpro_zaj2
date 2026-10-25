import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from zad_1.zad_1 import Student


class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka [ul. {self.street}, {self.zip_code} {self.city},"
            f" tel: {self.phone}, czynne: {self.open_hours}]"
        )


class Employee:

    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name} (Zatrudniony:"
            f" {self.hire_date}, Adres: {self.street}, {self.zip_code}, {self.city})"
        )


class Book:

    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: '{self.author_name} {self.author_surname}', wyd."
            f" {self.publication_date}, stron: {self.number_of_pages} | Miejsce:"
            f" {self.library}"
        )


class Order:

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list_str = "\n    - ".join([str(book) for book in self.books])
        return (
            f"--- Zamówienie z dnia: {self.order_date} ---\n"
            f"  Obsługujący: {self.employee}\n"
            f"  Zamawiający: {self.student}\n"
            f"  Zamówione książki:\n    - {books_list_str}"
        )


lib1 = Library("Warszawa", "Marszałkowska 10", "00-001", "8:00 - 20:00", "221112233")
lib2 = Library("Kraków", "Floriańska 5", "31-021", "9:00 - 18:00", "123334455")

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
emp2 = Employee(
    "Maria",
    "Konopnicka",
    "2021-05-15",
    "1988-05-23",
    "Kraków",
    "Grodzka 12",
    "31-006",
    "600700800",
)
emp3 = Employee(
    "Juliusz",
    "Słowacki",
    "2022-01-10",
    "1992-09-04",
    "Warszawa",
    "Krakowskie Przedmieście 3",
    "00-071",
    "700800900",
)

stud1 = Student("Katarzyna Wójcik", [55, 60, 70])
stud2 = Student("Tomasz Kamiński", [40, 45, 30])
stud3 = Student("Magdalena Zielińska", [80, 85, 90])

book1 = Book(lib1, "2020", "Henryk", "Sienkiewicz", 450)
book2 = Book(lib1, "2019", "Bolesław", "Prus", 380)
book3 = Book(lib2, "2021", "Stanisław", "Lem", 320)
book4 = Book(lib2, "2018", "Władysław", "Reymont", 510)
book5 = Book(lib1, "2022", "Olga", "Tokarczuk", 290)

order1 = Order(emp1, stud1, [book1, book2], "2026-06-10")
order2 = Order(emp2, stud3, [book3, book4, book5], "2026-06-11")

print("Zamówienia:\n")
print(order1, "\n")
print(order2)
