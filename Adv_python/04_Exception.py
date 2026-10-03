'''
try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except ValueError as v:
    print(v)

except Exception as e:
    print(e)

print("Thank you.!!!")
'''

a = int(input("Enter a number: "))
b = int(input("Enter sec number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide" \
    "numbers by zero")
else:
    print(f"The division a/b is{a/b}")