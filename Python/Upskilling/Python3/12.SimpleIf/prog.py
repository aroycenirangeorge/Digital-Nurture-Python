def passOrFail(mark):
    if(mark>35):
        print("Pass")
    else:
        print("Fail")
    
mark=75
if(mark<0):
    print("Invalid mark")
else:
    passOrFail(mark)