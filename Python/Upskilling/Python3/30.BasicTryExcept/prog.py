def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Number can't be divided by zero!")

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("Result:",divide(a,b))