# a = int(input("Enter number 1:"))
# b = int(input("Enter number 2:"))
# average = (a + b) / 2
# print("Average is", int(average))

#a = "24.5"
#t = type(a)
#print(t)
#output: <class 'str'>

n=int(input("Enter number of elements:"))
sum=0
for i in range(n):
    # print("Enter number", i+1,":")
    num = int(input("Enter number " + str(i+1) + ": "))
    sum = sum + num
average = (sum / n)
print("Average is", int(average))