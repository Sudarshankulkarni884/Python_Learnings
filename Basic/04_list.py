# lists are the collection of all database and it is mutable
Names = ["garpes" , "Orange" , 5 , 56.02 , False]
print(Names[0]) #garpes
Names[0] = "Mango" #change value of index 0
print(Names[0]) #Mango

l1=[1,34,62,2,6,11]
l1.sort() #sort the list in ascending order
print(l1) #[1, 2, 6, 11, 34, 62]

l2=[1,34,62,2,6,11]
l2.reverse() #reverse the list
print(l2) #[62, 34, 11, 6, 2, 1]

l3=[1,34,62,2,6,11]
l3.append(100) #add value at the end of the list
print(l3) #[1, 34, 62, 2, 6, 11, 100]

l4=[1,34,62,2,6,11]
l4.insert(0,100) #add value at the beginning of the list
print(l4) #[100, 1, 34, 62, 2, 6, 11]

l5=[1,34,62,2,6,11]
l5.remove(34) #remove value from the list
print(l5) #[1, 62, 2, 6, 11]