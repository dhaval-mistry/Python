class BankAccount:
    def __init__(self,account_number, owner_name,balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Amount should be greater than zero")

    def withdraw (self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print("Insufficient balance")
        else:
            print("Amount should be greater than zero")

    def check_balance(self):
        return self.balance
    

#BankAccount1 = BankAccount("123456","Dhaval",1000)
#BankAccount1.deposit(500)
#BankAccount1.withdraw(200)
#print("Account Number:", BankAccount1.account_number)
#print("Owner Name:", BankAccount1.owner_name)       
#print("Current Balance:", BankAccount1.check_balance())

class Book:
    title = ""
    author = ""
    list_of_review = []

    def __init__(self, title, author):
        Book.title = title
        Book.author = author
    
    def add_review(self, review):
        Book.list_of_review.append(review)

    def count_reviews(self):
        return len(Book.list_of_review)
    
    def display_all_reviews(self):
        for review in Book.list_of_review:
            print(review)

#book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
#book1.add_review("Amazing book!")
#book1.add_review("A timeless classic.")    
#print(book1.count_reviews())
#book1.add_review("Loved the characters and plot.")
#book1.display_all_reviews()

class Student:
    def __init__(self, name, roll_num, marks):
        self.__name = name
        self.__roll_num = roll_num
        self.__marks = marks

    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name = value
    def get_roll_num(self):
        return self.__roll_num
    def set_roll_num(self, value):
        if value > 0 and value <= 100:
            self.__roll_num = value
        else:
            print("Roll number must be between 1 and 100")  

    def get_marks(self):
        return self.__marks
    def set_marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Marks cannot be negative")


#student1 = Student("Dhaval", 10, 95)
#print("Name:", student1.get_name())
#print("Roll Number:", student1.get_roll_num())
#print("Marks:", student1.get_marks())
#student1.set_roll_num(150)
#print("Updated Roll Number:", student1.get_roll_num())
#student1.set_marks(-20)
#print("Updated Marks:", student1.get_marks())

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("circle")

class Rectangle(Shape):
    def area(self):
        print("Rectangle")

class Triangle(Shape):
    def area(self):
        print("Triangle")
'''
cir = Circle()
cir.area()
rec = Rectangle()
rec.area()
tri = Triangle()
tri.area()
'''

class Vehicle:
    brand=""
    model=""

class Car(Vehicle):
    seats = 0

class Bike(Vehicle):
    engine_cc = 0

# c = Car()
# c.brand = "Toyota"
# c.model = "Camary"
# c.seats = 5
# print(c.__dict__)

# b = Bike()
# b.model = "Ducati"
# b.model = "Scrambler"
# b.engine_cc = 803
# print(b.__dict__)

from abc import ABC

class Employee(ABC):

    def __init__(self,name):
        self.name = name
        
    def calculate_salary():
        pass

class Intern(Employee):

    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    
class FulltimeEmployee(Employee):

    def __init__(self, name, monthely_salary):
        super().__init__(name)
        self.monthely_salary = monthely_salary

    def calculate_salary(self):
        return self.monthely_salary

class ContractEmployee(Employee):
    def __init__(self, name,hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
    

# employee = [
#     Intern("AAA",500),
#     FulltimeEmployee("BBB", 5000),
#     ContractEmployee("CCC", 40, 120)
# ]

# for emp in employee:
#     print(emp.name, emp.calculate_salary())

class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address
    
# p1 = Person("Dhaval")
# p2 = Person("Shiv, 42")
# p3 = Person("Amit", 30, "123 Street")
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

class Herbivore:
    def eat_plants(self):
        return "Eating plants"
    def type(self):
        return "Herbivore"
    
class Omnivore:
    def eat_both(self):
        return "Eating both plants and meat"
    def type(self):
        return "Omnivore"
        
class Carnivore:
    def eat_meat(self):
        return "Eating meat"
    def type(self):
        return "Carnivore"



class Bear(Herbivore, Omnivore,  Carnivore):
    def roar(self):
        return "Roarrrr!"

# b = Bear()

# print(b.eat_both())
# print(b.roar())
# print(b.eat_plants())
# print(b.eat_meat())
# print(b.type())
# print(Bear.mro())