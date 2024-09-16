#Example of deserialization of an object from a file.
#Pickle library is used for serialization and deserialization 

import pickle

with open('emp.dat','rb')as f:
    obj=pickle.load(f)
    print("Printing Employee information after unpickling")
    obj.display()
