#Inheritance is a mechanism by which one class inherits the properties of another class

#Multiple inheritance
'''
class Employee:
    company = "Microsoft"
    name = "Harry"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
class coder:
    language = "Python"
    def printlanguage(self):
        print(f"The language used by the employee is {self.language}")

class programmer(Employee,coder):
    company = "Google"
    def showlanguage(self):
        print(f"The name of the company is {self.company} and he is good with {self.language} language")

a = Employee()
b = programmer()

b.show()
b.showlanguage()
b.printlanguage()
'''
######
'''
#Multilevel inheritance
class Employee:
    company = "Microsoft"
    name = "Harry"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
class coder(Employee):
    language = "Python"
    def printlanguage(self):
        print(f"The language used by the employee is {self.language}")
class programmer(coder):
    company = "Google"
    def showlanguage(self):
        print(f"The name of the company is {self.company} and he is good with {self.language} language")

a = Employee()
b = coder()
c = programmer()

c.show()
c.printlanguage()
c.showlanguage()
'''

#####

'''
from random import randint
class train:
    def __init__(self,trainNo,name):
        self.trainNo = trainNo
        self.name = name

    @staticmethod
    def greet():
            print("Good morning")
    def book(self,fro,to):
        print(f"Booking {self.name}train number {self.trainNo} from {fro} to {to}")

    def trainstatus(self):
        print(f"The {self.name} train number {self.trainNo} is currently running on time")

    def trainfare(self,fro,to):
        print(f"The fare for {self.name} train number {self.trainNo} from {fro} to {to} is {randint(200,2000)}")

    @staticmethod
    def gr():
        print("Thank you...")
t = train(16535,"GolGumbaz")
t.greet()
t.book("Vijayapura","Mysore")
t.trainstatus()
t.trainfare("Vijayapura","Mysore")
t.gr()
'''

#####
'''
class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The class attribute of a is {self.a}")

    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.a = 45

e.name = "Harry Potter"
print(e.fname,e.lname)

e.show()
'''