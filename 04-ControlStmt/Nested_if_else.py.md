Here’s the code with added comments and a brief explanation:

```python
# Example of Nested If-else control statement
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Taking user input for age
age = int(input(" Please Enter Your Age Here:  "))  # Input age as an integer

# First condition: Check if the person is a minor
if age < 18:
    print(" You are Minor ")  # Output message if the person is younger than 18
    print(" You are not Eligible to Work ")  # Informing that they are not eligible to work

# If the person is 18 or older
else:
    # Nested if-else: Check if the person is eligible to work
    if age >= 18 and age <= 60:
        print(" You are Eligible to Work ")  # Output if the person is between 18 and 60
        print(" Please fill in your details and apply")  # Prompt to fill in details for work
    else:
        # If the person is older than 60, they are considered too old to work
        print(" You are too old to work as per the Government rules")  # Output for those over 60
        print(" Please Collect your pension!")  # Suggest collecting pension
```

### Explanation:

1. **User Input**:
   - The program asks the user to input their age, which is then stored in the variable `age` after converting it to an integer using `int()`.

2. **If-Else Structure**:
   - The program checks if the user is less than 18 years old:
     - If true, it prints that the user is a minor and is not eligible to work.
   - If the user is 18 years or older, a nested `if-else` structure is used:
     - It checks if the user’s age is between 18 and 60 (inclusive). If true, it prints that the user is eligible to work.
     - If the user's age is greater than 60, it prints that the user is too old to work according to government rules and should collect their pension.

3. **Output**:
   - If the user enters an age below 18, the program prints a message saying they are a minor and not eligible to work.
   - If the user enters an age between 18 and 60, the program prints that they are eligible to work and prompts them to apply.
   - If the user enters an age above 60, the program prints a message saying they are too old to work and suggests collecting their pension.

This code demonstrates the use of nested if-else statements to handle multiple conditions based on the user's age.
