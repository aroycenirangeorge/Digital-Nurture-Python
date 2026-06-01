def nextYearAge(age):
    age=int(age)
    if(age<0):
        print("Invalid age")
    else:
        print("Next year you'll be",age+1)

age=input("Enter your age:")
nextYearAge(age)