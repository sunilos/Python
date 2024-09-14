# Importing the date and timedelta classes from the datetime module
from datetime import date, timedelta

# Getting the current date
currentStatus = date.today()

# Printing the current day
print("Current Date =", currentStatus.day)

# Printing the current month
print("Current Month =", currentStatus.month)

# Printing the current year
print("Current Year =", currentStatus.year)

# Calculating the date for tomorrow
tomorrowDate = currentStatus + timedelta(days=1)
print("Tomorrow Date = ", tomorrowDate)

# Calculating the date for the day after tomorrow
aftertomorrow = tomorrowDate + timedelta(days=1)
print("After tomorrow Date = ", aftertomorrow)

# Calculating the date for the previous day
previousDate = currentStatus - timedelta(days=1)
print("Previous Date = ", previousDate)
