#Write to a file 
def writeFile():
    # Iterate over the lines of the File
    file = open("Test.txt","w") #Open a file
    file.write("Hi\n")
    file.write("This is Python file")
    file.close() # Close a file

writeFile()
   
