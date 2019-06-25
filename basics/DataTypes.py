# Example of Data Types
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#Integers Numbers 
#
a = 100
ids=101
price =99.99

print(a)
print(ids)
print(price)

#Decimals numbers
x = 10.5
y = 5

##Type casting
print (x + y) #without type cast
print (int(x) + y) #after type cast


#List
list1 = ['a', 'b', 'c', 'd', 'e' ]
list2 = [1, 2, 3, 4, 5 ]
list3 =list1+ list2
list4 = list1 * 2
list5 = list1[2:3] #sublist starting from index#2 to #3
list6 = list1[2:]


print(list1)
print(list2)
print(list3)
print(list4)

#Length of ist
print(len(list1))


#Print elements
print(list1[1])

#Modify element
list1[1] = 'BB'
print(list1[1])

#Delete an element 
del list1[1]
print(list1)



