'''
n : int = 5

name:str ="Harry"
def sum(a:int,b:int) -> int:
    return a+b

print(f"{sum(5,7)}")
'''
from typing import List,Union,Tuple,Dict

#List of int
numbers:List[int] = [1,2,3,4,5]
print(numbers)

#Tuple of a string and int
tup:Tuple[str,int] = ("Harry",5)
print(tup)

#Dict with string as keys and int values
dict:Dict[str,int] = {"Harry":1,"AKash":2,"Prakash":3}
print(dict)

#Union type for varioable that can hold muliple values
identifior:Union[int,str] = "ID123"
identifior = 12345 #This is valid
identifior = "ID123" #This is valid
print(identifior)