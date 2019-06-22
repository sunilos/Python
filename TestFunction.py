#Function defination
def sum( a,b ):
   "It sumd two numbers"
   print('a',a,'b',b)
   c = a + b
   return c;

print(sum(5,10))
print(sum(10,20))

#keyword argument 
d = sum(b=7,a=8)

#Pass by reference
def chageList( list ):
   list.append(6);
   print (list)
   return

list = [1,2,3,4,5]
print(list)
chageList(list)
print(list)

#Variable length 
def sumnum( a, *varg ):
   t = a
   for n in varg:
      t+=n
   return t;

total = sumnum(1,2,3,4,5)
print('Total', total)
