# Importing the date class from the datetime module
from datetime import date 

# Defining a function to calculate age
def calculateAge(birthDate): 
    # Getting today's date
    today = date.today() 
    
    # Calculating the age based on the year difference
    # Subtract 1 if the current date hasn't reached the birth date in the current year
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    
    # Returning the calculated age
    return age 

# Taking the user's birth date as input
year = int(input("Enter your Birth Year = "))
month = int(input("Enter your Birth Month = "))
day = int(input("Enter your Birth Day = "))

# Calling the calculateAge function with the user's birth date
age = calculateAge(date(year, month, day))

# Printing the calculated age
print(age, "years")
