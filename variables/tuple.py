# Example of  Tuple
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#creating tuple 
my_tuple = ()
print(my_tuple)

#tuple of int, float, string
tuple_list1 = (1, 2.8, "Hello Python")
print(tuple_list1)

# tuple of string and list
tuple_list2 = ("Book", [1, 2, 3])
print(tuple_list2)


#Accessing elements from nested tuples
tuple_list4 = (1, "Steve", (11, 22, 33))  #1 represented the second element of that tuple.

print(tuple_list4[1][2])
print(tuple_list4[2][2])