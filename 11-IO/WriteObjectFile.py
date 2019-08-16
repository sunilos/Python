import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
    
with open('emp.dat','wb')as f:
    e=Employee(1,'Mayank',1000,'Indore')
    pickle.dump(e,f)
    print("Pickling  of Employee Object completed")
