import pickle

with open('emp.dat','rb')as f:
    obj=pickle.load(f)
    print("Printing Employee information after unpickling")
    obj.display()
