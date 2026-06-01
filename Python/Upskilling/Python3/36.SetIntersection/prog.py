def commonSkills(a,b):
    print("Common skills:",a&b)

a=set(input("Enter skills of person A:").split())
b=set(input("Enter skills of person B:").split())
commonSkills(a,b)