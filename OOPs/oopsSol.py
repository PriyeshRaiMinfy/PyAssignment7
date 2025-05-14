# === Easy Questions ===

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # area nikal rahe hain

    def perimeter(self):
        return 2 * (self.width + self.height)  # perimeter ka formula


class Counter:
    def __init__(self):
        self.value = 0  # initial value 0

    def increment(self):
        self.value += 1  # value badha rahe hain

    def decrement(self):
        self.value -= 1  # value ghata rahe hain

    def reset(self):
        self.value = 0  # reset to zero


# === Medium Questions ===

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year  # basic info


class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type  # extra info car ke liye


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance  # private variables

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


# === Hard Questions ===

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")  # force karega implement karne ke liye


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2  
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # member ke books


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.checked_out = {}  # kisne kaunsi book li hai

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def checkout_book(self, book, member):
        if book in self.books and book not in self.checked_out:
            self.checked_out[book] = member
            member.borrowed_books.append(book)

    def return_book(self, book, member):
        if book in self.checked_out and self.checked_out[book] == member:
            del self.checked_out[book]
            member.borrowed_books.remove(book)

    def is_book_available(self, book):
        return book not in self.checked_out


#------------------------------Test Cases -----------

if __name__ == "__main__":
    # Easy
    r = Rectangle(5, 10)
    print(r.area())       
    print(r.perimeter())  

    c = Counter()
    c.increment()
    c.increment()
    print(c.value)  
    c.decrement()
    print(c.value)  
    c.reset()
    print(c.value)  

    # Medium
    car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
    print(car.make)   
    print(car.doors)  

    acc = BankAccount("123456", 1000)
    print(acc.get_balance())         
    acc.deposit(500)
    print(acc.get_balance())         
    acc.withdraw(200)
    print(acc.get_balance())         
    print(acc.get_account_number())  

    # Hard
    shapes = [Circle(5), Rect(4, 6), Triangle(3, 4, 5)]
    for shape in shapes:
        if isinstance(shape, Circle):
            print(f"Circle area: {shape.area()}")
        elif isinstance(shape, Rect):
            print(f"Rectangle area: {shape.area()}")
        elif isinstance(shape, Triangle):
            print(f"Triangle area: {shape.area()}")


    lib = Library()
    b1 = Book("Python Programming", "John Smith")
    b2 = Book("Data Structures", "Jane Doe")
    lib.add_book(b1)
    lib.add_book(b2)

    m = Member("Alice", "M001")
    lib.register_member(m)

    lib.checkout_book(b1, m)
    print(lib.is_book_available(b1))  
    print(lib.is_book_available(b2))  

    lib.return_book(b1, m)
    print(lib.is_book_available(b1))  
