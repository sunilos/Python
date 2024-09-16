# Importing the datetime class from the datetime module
from datetime import datetime

# Getting the current date and time
now = datetime.now()

# Formatting the current time to display in "Hours:Minutes:Seconds" format
current_time = now.strftime("%H:%M:%S")

# Printing the formatted current time
print("Current Time =", current_time)

# Printing the current hour
print("Current Hours = ", now.hour)

# Printing the current minutes
print("Current Minutes = ", now.minute)

# Printing the current seconds
print("Current Seconds = ", now.second)
