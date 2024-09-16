Here’s the code with added comments and a brief explanation:

```python
from datetime import date  # Importing the 'date' module from the 'datetime' library
  
# Function to calculate age based on the birthdate
def calculateAge(birthDate): 
    today = date.today()  # Getting today's date
    # Calculate the age by subtracting birth year from the current year
    # Adjust the calculation if the birth month and day haven't occurred yet this year
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age  # Return the calculated age

# Taking user input for birth year, month, and day
year = int(input("Enter your Birth Year = "))  # Input birth year
month = int(input("Enter your Birth Month = "))  # Input birth month
day = int(input("Enter your Birth Day = "))  # Input birth day

# Calculate the age by calling the 'calculateAge' function
age = calculateAge(date(year, month, day))

# Printing the age in years
print(age, "years")  # Output: user's age in years
```

### Explanation:

1. **Importing Modules**:
   - The `date` module from Python's `datetime` library is imported to work with dates.

2. **Function Definition**:
   - `calculateAge(birthDate)`: This function calculates the user's age by comparing the current date (`today`) with the provided birthdate (`birthDate`).
   - The expression `((today.month, today.day) < (birthDate.month, birthDate.day))` checks if the user's birthday has occurred this year; if not, it subtracts one year from the calculated age.

3. **User Input**:
   - The program takes input for the birth year, month, and day using `input()` and converts them to integers.

4. **Age Calculation**:
   - The `calculateAge()` function is called with the birthdate, and the result is stored in the `age` variable.

5. **Output**:
   - The program prints the calculated age along with the message "years." For example, if the user is 25 years old, it will output `25 years`.
