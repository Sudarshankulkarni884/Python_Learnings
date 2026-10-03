#tuples are immutable
a = (1, "rohan" , 3 , 45 , False , 45 , 5.6 )
print(type(a)) #<class 'tuple'>

#methods of tuple
#count() and index()
no = a.count(45) #count the number of 45 in tuple
print(no) #2

i = a.index(45) #index of 45 in tuple
print(i) #4