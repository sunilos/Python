#Example of deserialization on an object from a file.
#Pickle liabrary is used for serialization and deserialization 

import pickle

with open('emp.dat','rb')as f:
    obj=pickle.load(f)
    print("Printing Employee information after unpickling")
    obj.display()
