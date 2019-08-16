#Read a file 
def readFile():
    file = open("UserModel.py") #Open a file
    text = file.read() # Read all data 
    print(text) 
    file.close() # Close a file
    return
