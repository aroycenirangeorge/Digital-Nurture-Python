def validateCredentials(username,password):
    if(username=="admin"):
        if(password=="pass123"):
            print("Login successful!")
        else:
            print("Password Incorrect")
    else:
        print("Both username and password incorrect")

name=input("Enter the name:")
pwd=input("Enter the password:")
if(name=='' or pwd==''):
    print("Invalid Input")
else:
    validateCredentials(name,pwd)