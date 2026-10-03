#set is a collection of unique elements
# and it is mutable and unordered

s = {1 , 2 , 4 , "rohan" , 4 , 5.6 , False}
print(s,type(s)) #<class 'set'>

s.add(3)
print(s) #{1, 2, 3, 4, 'rohan', 5.6, False}

s.remove(3)
print(s) #{1, 2, 4, 'rohan', 5.6, False}

#sets operation(union , intersection)
s1 = {1 , 2 , 3 , 4 , 5}
s2 = {4 , 5 , 6 , 7 , 8}
print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2)) #{4, 5}

print(s1 - s2) #{1, 2, 3}
print(s2 - s1) #{6, 7, 8}