Here’s the code with added comments and a brief explanation:

```python
from datetime import date, timedelta  # Importing 'date' and 'timedelta' from the 'datetime' module

# Get today's date
currentStatus = date.today()

# Printing the current day, month, and year
print("Current Date =", currentStatus.day)  # Output: Current day
print("Current Month =", currentStatus.month)  # Output: Current month
print("Current Year =", currentStatus.year)  # Output: Current year

# Check tomorrow's date by adding 1 day using 'timedelta'
tomorrowDate = currentStatus + timedelta(days=1)
print("Tomorrow Date =", tomorrowDate)  # Output: Tomorrow's date

# Check the day after tomorrow by adding 1 more day
aftertomorrow = tomorrowDate + timedelta(days=1)
print("After Tomorrow Date =", aftertomorrow)  # Output: Date of the day after tomorrow

# Check the previous date by subtracting 1 day using 'timedelta'
previousDate = currentStatus - timedelta(days=1)
print("Previous Date =", previousDate)  # Output: Previous day's date
```

### Explanation:

1. **Importing Modules**:
   - The `date` and `timedelta` classes from the `datetime` module are imported to handle date manipulation.

2. **Current Date**:
   - `date.today()` retrieves the current date. The day, month, and year are accessed separately and printed.

3. **Tomorrow’s Date**:
   - `timedelta(days=1)` is used to add one day to the current date to calculate tomorrow's date.

4. **Day After Tomorrow**:
   - By adding one more day to `tomorrowDate`, the day after tomorrow is calculated and printed.

5. **Previous Date**:
   - Subtracting one day using `timedelta(days=1)` calculates the previous day's date.

This code helps you work with dates by retrieving the current date, adding or subtracting days, and manipulating them as needed.