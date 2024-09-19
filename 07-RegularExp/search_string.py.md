
```python
# Example to search string using search()
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Import the regular expressions module
import re

# Define a string to search within
string = "The rain in Spain"

# Search for the first occurrence of the substring 'the' in the string
result = re.search('the', string, re.IGNORECASE)

# Check if a match was found and print the appropriate message
if result:
    print("String Found ")
else:
    print("Not found")
```

### Explanation:

1. **Import `re` Module**:
   - `import re`: Imports the `re` module, which provides functions for working with regular expressions.

2. **Define the String**:
   - `string = "The rain in Spain"`: This is the string in which we are searching for the pattern.

3. **Search for a Substring**:
   - `result = re.search('the', string, re.IGNORECASE)`: The `re.search()` function searches for the first occurrence of the substring `'the'` in `string`. The `re.IGNORECASE` flag makes the search case-insensitive, meaning it will match `'the'`, `'The'`, `'tHe'`, etc.

4. **Check and Print Results**:
   - `if result:`: This checks if a match was found. If a match is found, it prints `"String Found"`. Otherwise, it prints `"Not found"`.

The `re.search()` function is used to find the first occurrence of a pattern in a string. If the pattern is found, it returns a match object; otherwise, it returns `None`.
