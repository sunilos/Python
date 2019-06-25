
# Example of   Polymorphism 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# A simple Python function to demonstrate 
# Polymorphism 
print("A simple Python function to demonstrate ")
def add(x, y, z = 0): 
	return x + y+z 

# Driver code 
print(add(2, 3)) 
print(add(2, 3, 4)) 

print("Polymorphism with Class methods:\n")

class India(): 
	def capital(self): 
		print("New Delhi is the capital of India.") 

	def language(self): 
		print("Hindi the primary language of India.") 

	def type(self): 
		print("India is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def type(self): 
		print("USA is a developed country.") 

obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
	country.capital() 
	country.language() 
	country.type() 
