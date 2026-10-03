myList=[1,2,5,7,3,9]

# squredlist=[]
# for item in myList:
#     squredlist.append(item**2)

# print(squredlist)

squredlist=[item**2 for item in myList]
#or
squredlist=[i*i for i in myList]
print(squredlist)
