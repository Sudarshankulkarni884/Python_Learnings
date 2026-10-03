# Conditional Statements
a = int(input("Enter your age: "))

#if elif else statement
#relational operators: >, <, >=, <=, ==, !=
if(a>=18):
    print("You are eligible for voting")

elif(a<0):
    print("Invalid age entered")

else:
    print("You are not eligible for voting")

#if statement
if(a%2==0):
    print("You have entered an even number")

print("End of the program")