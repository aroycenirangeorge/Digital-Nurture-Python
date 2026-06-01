def stringLength(string):
    return len(string)

name=input("Enter the string:")
if(type(name)==str):
    print("Length of the string:",stringLength(name))
else:
    print("Invalid Input")