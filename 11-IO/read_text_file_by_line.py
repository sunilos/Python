#Read a file line by line
def readLine():
    # Iterate over the lines of the File
    file = open("UserModel.py") #Open a file
    for line in file :
        print(line, end=' ')
    file.close() # Close a file
  
readLine()
