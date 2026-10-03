# commented statements are only used in finally function
def main():# funnction is not needed for try and else 
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
    #   return
    except Exception as e:
        print(e)
    #   return
    else:
        print("You enterd number correctly")
    
    #finally:#This is only when try is inside the function and 
    # after return this function(finally) works
    #   print("Thank you...!!")

main()