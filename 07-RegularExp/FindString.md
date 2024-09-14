Here’s the code with added comments and a brief explanation:

```python
# Example to find string using findall() 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import re  # Import the regular expressions module

# Define a string to search
string = "The rain in Spain"

# Find all occurrences of the substring "ai" in the string
result = re.findall("ai", string) 

# Print the result of findall
print(result)  
# Output will be a list of all matches, e.g., ['ai', 'ai']

# Check if any matches were found
if result:
    print("YES! We have a match!")
else:
    print("No match")
```

### Explanation:

1. **Import `re` Module**:
   - `import re`: This imports the `re` module, which provides functions for working with regular expressions in Python.

2. **Define the String**:
   - `string = "The rain in Spain"`: This is the string where we want to search for the pattern.

3. **Find All Occurrences**:
   - `result = re.findall("ai", string)`: The `findall()` function searches the `string` for all non-overlapping occurrences of the substring `"ai"`. It returns a list of all matches.

4. **Print the Result**:
   - `print(result)`: This prints the list of matches. For the given string, it will print `['ai', 'ai']`.

5. **Check for Matches**:
   - `if result:`: This checks if the `result` list is not empty. If matches are found, it prints `"YES! We have a match!"`. Otherwise, it prints `"No match"`.

The `findall()` function is used to find all occurrences of a pattern in a string and returns them as a list.