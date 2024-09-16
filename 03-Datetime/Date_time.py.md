Here’s the code with added comments and a brief explanation:

```python
# Example of Date Time 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import datetime  # Importing the 'datetime' module

# Get current datetime
x = datetime.datetime.now()  # This fetches the current date and time
print(x)  # Output: Current date and time in the format YYYY-MM-DD HH:MM:SS

# Get the current year and name of the weekday
x = datetime.datetime.now()  # Fetches current date and time again
print(x.year)  # Output: The current year (e.g., 2024)
print(x.strftime("%A"))  # Output: The name of the current weekday (e.g., Monday)

# Get a datetime object of a specific date (June 1, 2018)
x = datetime.datetime(2018, 6, 1)  # Creating a datetime object for a specific date (June 1, 2018)

# Format the date using strftime() method to get the name of the month
print(x.strftime("%B"))  # Output: The name of the month for the given date (e.g., June)
```

### Explanation:

1. **Importing `datetime` Module**:
   - The `datetime` module is imported to work with date and time objects.

2. **Getting Current Date and Time**:
   - `datetime.datetime.now()` retrieves the current date and time, which is then printed in a standard format (`YYYY-MM-DD HH:MM:SS`).

3. **Getting Year and Weekday**:
   - `x.year`: Retrieves the current year.
   - `x.strftime("%A")`: Formats the current date to output the full weekday name (e.g., "Monday").

4. **Specific Date Object**:
   - `datetime.datetime(2018, 6, 1)`: Creates a datetime object for June 1, 2018.

5. **Formatting Date to Get Month**:
   - `x.strftime("%B")`: Formats the date to return the full name of the month (e.g., "June"). 

This code demonstrates how to fetch the current date and time, access specific components like the year and weekday, and create a datetime object for a specified date while formatting the output.
