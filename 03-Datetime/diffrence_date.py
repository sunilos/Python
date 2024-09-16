# Importing the date class from the datetime module
from datetime import date 

# Defining the function to calculate age
def calculateAge(birthDate, currentDate): 
    # Getting today's date
    today = date.today()  
    
    # Calculating the age based on year difference
    # Subtract 1 if the current date hasn't reached the birth date in the current year
    age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day)) 
    
    # Returning the calculated age
    return age 
      
# Taking the user's birth date as input
year = int(input("Enter your Birth Year = "))
month = int(input("Enter your Birth Month = "))
day = int(input("Enter your Birth Day = "))

# Asking for the current date from the user
print("-------- Enter Current Date --------")
print()
cyear = int(input("Enter your Current Year = "))
cmonth = int(input("Enter your Current Month = "))
cday = int(input("Enter your Current Day = "))

# Calling the calculateAge function with the user's birth date and current date as arguments
age = calculateAge(date(year, month, day), date(cyear, cmonth, cday))

# Printing the calculated age
print(age, "years")
