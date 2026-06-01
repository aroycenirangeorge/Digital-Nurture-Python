def fetch(data,dept,name):
    if(dept not in data):
        print("Invalid department!")
        return
    if(name not in data[dept]):
        print("Invalid employee!")
        return
    print("Salary of",name,"in department",dept,"is",data[dept][name])
data={
    "ece":{
        "John":5000,
        "Jane":7000,
    },
    "cse":{
        "Juan":4000,
        "Jamie":2000,
    },
}
dept=input("Enter the department:")
name=input("Enter the employee name:")
fetch(data,dept,name)