'''
class Employee:
    language = "Python"#This is a class attribute
    salary = 1200000

    def getInfo(self):#Self method
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
harry = Employee()
harry.name = "Harry"#This is an instance attribute
print(harry.name,harry.language,harry.salary)
harry = Employee()harry.name = "Rohan robin"
printharry.nameharry.languageharry.salary)

#Here name is instance attribute and salary and language are attribute
#as they directly belong to the class
harry.getInfo()harry.greet() 
'''

class Employee:
    language = "Python"#This is a class attribute
    salary = 1200000

    def __init__(self,name,salary,language):#Constructor
        self.name = name #This is an instance attribute
        self.salary = salary
        self.language = language

    def getInfo(self):#Self method
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")
harry = Employee("Harry",130000,"Javascript") 
#Here name is instance attribute and salary and language are class attribute
print(harry.name,harry.language,harry.salary)  