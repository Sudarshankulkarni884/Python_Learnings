'''
class programmer:
    def __init__(self,name,company,salary):
        self.name = name
        self.company = company
        self.salary = salary
jeevan = programmer("Jeevan,","Microsoft,",1300000)
print(jeevan.name,jeevan.company,jeevan.salary)
jack = programmer("Jack,","Mircosoft,",1000000)
print(jack.name,jack.company,jack.salary)
akash = programmer("Akash,","Microsoft,",1200000)
print(akash.name,akash.company,akash.salary)
'''

'''
class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The squre of the given number is:{self.n * self.n}")
    def cube(self):
        print(f"The cube of the given number is:{self.n * self.n * self.n}")
    def square_root(self):
        print(f"The square root of the given number is:{self.n **1/2}")

a = calculator(4)
a.square()
a.cube()
a.square_root()
'''

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

