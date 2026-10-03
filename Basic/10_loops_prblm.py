#prime numbers
n = int (input("Enter a number: "))
for i in range(2,n):
    if(n%i == 0):
        print("not prime number")
        break
else:
    print("prime number")

#sum of natural numbers using while loop
n=int(input("Enter a number: "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)    

#factorial of a number using for loop
Num = int(input("Enter a number: "))
i=1
factorial=1
for i in range(1,Num+1):
    factorial=factorial*i
print(factorial)

#star pattern using for loop
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

# star problem
n = int(input("Enter a number: "))
for i in range(1,n+1):
   if(i==1 or i==n):
      print(" * "*n,end="")
   else:
      print(" * ",end="")
      print("   "*(n-2),end="")
      print(" * ",end="")
   print("")

#Multiplication of numbers in reverse order
n = int(input("Enter a number: "))
i=1
for i in range(10,0,-1):
    print(f"{n} x {i} = {n*i}")

#or
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*11-i}")