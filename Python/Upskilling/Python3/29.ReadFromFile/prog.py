def read(filename):
    try:
        file=open(filename,'r')
        content=file.read()
        print(content)
        file.close()
    except:
        print("File not found")
    
read("text.txt")