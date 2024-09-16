Here’s the code with added comments and a brief explanation:

```python
from datetime import datetime  # Importing 'datetime' from the 'datetime' module

# Get the current date and time
now = datetime.now()

# Format the current time as Hour:Minute:Second
current_time = now.strftime("%H:%M:%S")

# Printing the formatted current time
print("Current Time =", current_time)  # Output: Current time in HH:MM:SS format

# Printing the current hour
print("Current Hours =", now.hour)  # Output: The current hour (24-hour format)

# Printing the current minute
print("Current Minutes =", now.minute)  # Output: The current minute

# Printing the current second
print("Current Seconds =", now.second)  # Output: The current second
```

### Explanation:

1. **Importing `datetime`**:
   - The `datetime` class from the `datetime` module is imported to access both the current date and time.

2. **Getting Current Date and Time**:
   - `datetime.now()` retrieves the current date and time (both date and time values).

3. **Formatting the Time**:
   - `now.strftime("%H:%M:%S")` formats the current time into a string in the format of `HH:MM:SS` (24-hour format).

4. **Accessing Individual Time Components**:
   - `now.hour`: Retrieves the current hour.
   - `now.minute`: Retrieves the current minute.
   - `now.second`: Retrieves the current second.

5. **Output**:
   - The program prints the full current time in `HH:MM:SS` format and separately prints the hour, minute, and second components.
