'''
# farenheit to celsius
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter a temperature in Farenheit: "))
print(f"Temperature in Celsius: {round(f_to_c(f), 2)}°C")
'''

'''
#sum(n)=sum(n-1)+n

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

n = int(input("Enter a number: "))
print(f"The sum of {n} is: {sum(n)}")
'''

'''
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
n= int(input("Enter a number: "))
pattern(n)
'''

'''
# inch to cm
def inch_to_cm(inch):
    return inch * 2.54
inch = int(input("Enter a number: "))
print(f"The centemeter value is:{inch_to_cm(inch)}")
'''

'''
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
n = int(input("Enter the number: "))
multiply(n)
'''