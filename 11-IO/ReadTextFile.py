#Read all text from a file 
def readFile():
    file = open("abc.txt") #Open a file
    text = file.read() # Read all data 
    print(text) 
    file.close() # Close a file
    
readFile()    
 
