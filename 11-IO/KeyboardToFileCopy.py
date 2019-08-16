
#Reads text from keyboard and stores into a text file. 

def KeyboardToFileCopy():
    # Iterate over the lines of the File
    file = open("Test.txt","w") #Open a file
    text=input('Enter your meeage = ')

    while(text!="quit"):
        file.write(text)
        file.write(" ")
        text=input('')
    file.close() # Close a file

KeyboardToFileCopy()
