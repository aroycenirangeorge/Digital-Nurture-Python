def display(coordinates):
    a,b=coordinates
    if(a<0 or b<0):
        print("Invalid Input")
    print("x-coordinate:",a)
    print("y-coordinate:",b)


x=int(input("Enter the x-coordinate:"))
y=int(input("Enter the y-coordinate:"))
coordinate=(x,y)
display(coordinate)