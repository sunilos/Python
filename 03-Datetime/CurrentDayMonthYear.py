from datetime import date,timedelta
currentStatus= date.today()
print("Current Date =", currentStatus.day)
print("Current Month =", currentStatus.month)
print("Current Year =", currentStatus.year)

#check tomorrow Date
tomorrowDate=currentStatus+timedelta(days=1)
print("tomorrow Date = ",tomorrowDate)

#check after tomorrow Date
aftertomorrow=tomorrowDate+timedelta(days=1)
print("After tomorrow Date = ",aftertomorrow)



