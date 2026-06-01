def numberRange(m,n):
    for i in range(m,n+1):
        if(i%2==0):
            print("First even found:",i)
            break
        print(i)

a=int(input("Enter range 1:"))
b=int(input("Enter range 2:"))
if(a<b):
    numberRange(a,b)
else:
    print("Invalid range")