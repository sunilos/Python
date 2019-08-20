from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day)) 
    return age 
      
year=int(input("Enter your Birth Year = "))
month=int(input("Enter your Birth Month = "))
day=int(input("Enter your Birth Day = "))
age=calculateAge(date(year, month, day))
print(age, "years")
