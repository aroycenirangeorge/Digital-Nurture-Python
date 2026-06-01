def calculateArea(length,breadth):
    return length*breadth

length=5
breadth=3
print("Length:",length)
print("Breadth:",breadth)
if(length>=0 and breadth>=0):
    print("Area of rectangle:",calculateArea(length,breadth))
else:
    print("Invalid Input")