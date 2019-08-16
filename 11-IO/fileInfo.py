# Example of File I/o  
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Prints properies of a file
def fileInfo():
    fo = open("Test.py", "wb") 
    print ("File Name: ", fo.name)
    print ("Mode of Opening: ", fo.mode)
    print ("Is Closed: ", fo.closed)
    
fileInfo()
