dict1={"name":"Raju", "marks":56}
def keypresent(input):
    if input in dict1:
        print("Exists")
    else:
        print("Not Exist")
keypresent(input("enter the input: "))