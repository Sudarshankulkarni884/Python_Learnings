a = "Darshh is bad boy\n"

print(len(a))# length of a

# string slice
print(a[0:5]) #Darsh

# string index
print(a[0]) 

print(a.startswith("Darshh"))#starts with Darshh (T or F)

#replace function
print(a.replace("bad","good").replace("boy","girl"))

#Esape sequence(\n , \t , \; , \" , \ )")
a = "Darshh is \tgood\t boy\nAnd\nHe is very \"bad\"\n"
print(a)