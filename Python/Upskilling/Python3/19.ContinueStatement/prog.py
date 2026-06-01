def sumOfOdds(n):
    sum=0
    for i in range(n+1):
        if(i%2==0):
            continue
        sum+=i
    return sum

n=10
if(type(n)==int):
    print("Sum of Odd Number in range:",sumOfOdds(n))
else:
    print("Invalid number")