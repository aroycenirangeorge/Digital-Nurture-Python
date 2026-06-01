def assignGrade(num):
    if(mark<=100 and mark>=80):
        print("Grade A")
    elif(mark<=79 and mark>=60):
        print("Grade B")
    else:
        print("Grade C")
    
mark=88
if(type(mark)==int):
    assignGrade(mark)
else:
    print("Invalid Input")