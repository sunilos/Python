
```python
from datetime import date  # Import the 'date' class from the 'datetime' module

# Function to calculate age based on birth date and current date
def calculateAge(birthDate, currentDate): 
    # Calculate the age by subtracting birth year from the current year
    # Adjust the calculation if the birth month and day haven't occurred yet this year
    age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
    return age  # Return the calculated age

# Taking user input for birth date
year = int(input("Enter your Birth Year = "))  # Input birth year
month = int(input("Enter your Birth Month = "))  # Input birth month
day = int(input("Enter your Birth Day = "))  # Input birth day

# Taking user input for the current date
print("-------- Enter Current Date --------\n")
cyear = int(input("Enter your Current Year = "))  # Input current year
cmonth = int(input("Enter your Current Month = "))  # Input current month
cday = int(input("Enter your Current Day = "))  # Input current day

# Calculate the age by calling the 'calculateAge' function
age = calculateAge(date(year, month, day), date(cyear, cmonth, cday))

# Print the calculated age in years
print(age, "years")  # Output: user's age in years
```

### Explanation:

1. **Importing `date` Class**:
   - The `date` class from the `datetime` module is imported to work with date objects.

2. **`calculateAge` Function**:
   - This function takes two arguments: `birthDate` (the user's birthdate) and `currentDate` (the provided current date).
   - The function calculates the user's age by subtracting the birth year from the current year and adjusts the result if the birthday hasn’t occurred yet in the current year.

3. **User Input for Birth Date**:
   - The program prompts the user to input their birth year, month, and day.

4. **User Input for Current Date**:
   - The program then prompts the user to input the current year, month, and day (instead of using today's date automatically, this allows for manual input).

5. **Age Calculation**:
   - The `calculateAge()` function is called, passing the birthdate and current date as arguments. The function computes the user's age, which is then printed.

