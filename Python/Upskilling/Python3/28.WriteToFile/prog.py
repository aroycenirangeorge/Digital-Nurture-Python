def write():
    file=open("text.text","w")
    file.write("Hello World")
    file.close()

write()
print("File created successfully!")