def unpack(tuple):
    x,y=tuple
    if(x<0 or y<0):
        print("Invalid Coordinates")
        return
    print("x-coordinate",x)
    print("y-coordinate",y)
unpack((int(input()),int(input()))) 