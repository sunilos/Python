from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Current Hours = ",now.hour)
print("Current Minutes = ",now.minute)
print("Current Seconds = ", now.second)
