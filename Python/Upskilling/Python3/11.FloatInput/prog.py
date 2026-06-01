def kiloToLbs(kilo):
    if(kilo<0):
        print("Invalid Input")
    else:
        lbs=kilo*2.20462
        print("Pound:",lbs)

kilo=float(input("Enter the kilogram:"))
kiloToLbs(kilo)