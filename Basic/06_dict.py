# dict is the collection of all database 
# and it is mutable and it is unordered

marks ={
    "rohan" : 90 ,
    "shubham" : 100,
    "sachin" : 80 
}

print(type(marks)) #<class 'dict'>
print(marks["rohan"]) #90

#dictionary methods

print(marks.items())
 #dict_items([('rohan', 90), ('shubham', 100), ('sachin', 80)])

print(marks.keys())
 #dict_keys(['rohan', 'shubham', 'sachin'])

print(marks.values())
 #dict_values([90, 100, 80])

marks.update({"rohan" : 95 , "renuka" : 85})#update the value of rohan
print(marks)
 #{'rohan': 95, 'shubham': 100, 'sachin': 80}

print(marks.pop("rohan"))#removes the key rohan and returns its value
print(marks)

print(marks.get("rohan1")) #prints none
print(marks["rohan1"])#returns an error