from datetime import date 
def calculateAge(birthDate,currentDate): 
    today = date.today() 
    age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) <(birthDate.month, birthDate.day)) 
    return age 
      
year=int(input("Enter your Birth Year = "))
month=int(input("Enter your Birth Month = "))
day=int(input("Enter your Birth Day = "))

print("-------- Enter Current Date --------")
print()
cyear=int(input("Enter your Current Year = "))
cmonth=int(input("Enter your Current Month = "))
cday=int(input("Enter your Current Day = "))


age=calculateAge(date(year, month, day),date(cyear, cmonth, cday))
print(age, "years")
