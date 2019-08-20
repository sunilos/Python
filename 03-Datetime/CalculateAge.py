from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day)) 
    return age 
      
year=int(input("Year your Birth Year = "))
month=int(input("Year your Birth Month = "))
day=int(input("Year your Birth Day = "))
age=calculateAge(date(year, month, day))
print(age, "years")
