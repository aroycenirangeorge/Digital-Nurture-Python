def evenOrOdd(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")
    
n=8
if(type(n)==int):
    evenOrOdd(n)
else:
    print("Invalid Input")