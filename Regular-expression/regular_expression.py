# Example of Regular Expresion 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"

#x = re.search("The rain", txt)
#Return a list containing every occurrence of "ai":

#x = re.findall("ai", txt) 
#print(x)
#if (x):
#  print("YES! We have a match!")
#else:
 # print("No match")


  #search matching string
x = re.search('world', txt)
x = re.split("\s", txt)
x = re.split("\s", txt, 1)
# if x:
#   print("pattern found inside the string")
# else:
#   print("pattern not found")  
print(x)
#Find All Function returns a list containing values
print("Returns list containing Values :")
str = "The rain in Spain" #Return a list containing every occurrence of "ai":
x = re.findall("ai", str)
print(x)

print("Search the matching string")
txt = "The rain in Spain"
x = re.search('world', txt)
if x:
 print("pattern found inside the string")
else:
 print("pattern not found")


#Split the string

print("Split the String")
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#sub function replaces the matches with text of your string
print("replaces the Matches with text of your choice")
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
