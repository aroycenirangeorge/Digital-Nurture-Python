def updateDictionary(dictionary,id,name):
    dictionary.update({id:name})
    print("Updated Dictionary:",dictionary)

id=int(input("Enter employee id:"))
name=input("Enter employee name:")
dictionary=dict()
if(id>0 and name!=''):
    updateDictionary(dictionary,id,name)