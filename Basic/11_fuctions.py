#functions are grp of statement performing sepcific task
#function name should be in lower case
'''
#Function definition
def avg():
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    c= (a+b)/2
    print(f"The average of these two numbers is: \"{c}\"")
avg()#function call
avg()#function call
'''

'''
#functions are len(),print(),input(),range(),etc
def greet(name,surname):
    print(f"Good day, {name}!")
    print(surname)
greet("Harry","Thank you")
greet("Rohan","Thnak u") 
greet("Divya","Thanks")   
'''

'''
#functions with "arguement"
def greet(name):
    gr="Hello," + name
    return gr
a = greet("Harry")
print(a) 
'''

'''
#default funtion arguement
def greet(name="Harry"):
    print("Good day",name)
greet("Rohan")
#if no arguement is passed then default arguement is used
'''
