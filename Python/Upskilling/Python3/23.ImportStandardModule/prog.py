import math
def calculateArea(radius):
    return math.pi*(radius^2)

radius=int(input("Enter the radius:"))
if(radius<0):
    print("Invalid radius!")
else:
    print(f"Area of a circle: {calculateArea(radius):.2f}")