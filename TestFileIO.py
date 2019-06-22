#Prints properies of a file
def fileInfo():
    fo = open("Test.py", "wb") 
    print ("File Name: ", fo.name)
    print ("Mode of Opening: ", fo.mode)
    print ("Is Closed: ", fo.closed)
    return

#Read a file 
def readFile():
    file = open("UserModel.py") #Open a file
    text = file.read() # Read all data 
    print(text) 
    file.close() # Close a file
    return

#Read a file line by line
def readLine():
    # Iterate over the lines of the File
    file = open("UserModel.py") #Open a file
    for line in file :
        print(line, end=' ')
    file.close() # Close a file
    return

#Write to a file 
def writeFile():
    # Iterate over the lines of the File
    file = open("Test.txt","w") #Open a file
    file.write("Hi\n")
    file.write("This is Python file")
    file.close() # Close a file
    return


#fileInfo()
readFile()
#readLine()
#writeFile()
