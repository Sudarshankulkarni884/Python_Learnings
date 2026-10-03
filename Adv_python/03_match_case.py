'''
#match case
#match case is like switch case in "C" language
def match_case(status):
    match status:
        case 200:
            return "Success"
        case 404:
            return "NotFound"
        case 500:
            return "ServerError"
        case _:
            return "Something_went_wrong"

print(match_case(200))
print(match_case(404))
print(match_case(500))  
print(match_case(100))
'''

'''
#Dictionary Merge and Update operation
d1 = {"name":"Harry","age":25}
d2 = {"name":"AKash","age":30}

Merged_dict = {**d1,**d2}
print(Merged_dict)
#Or
Merged =d1|d2
print(Merged)
'''

'''
#opening multiple file from with open statement
with(
    open("file1.txt") as f1,
    open("file2.txt") as f2,
    open("file3.txt") as f3
):
'''