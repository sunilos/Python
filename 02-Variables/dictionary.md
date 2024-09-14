Here’s the code with added comments and a brief explanation:

```python
# Example of Dictionary
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Creating a dictionary with integer keys and string values
dictionary_list = {1: 'Ram', 2: 'Shyam', 3: 'Balram', 4: 'Raju'}

# Accessing and printing values from the dictionary using their keys
print("1st name is " + dictionary_list[1])  # Output: 1st name is Ram
print("2nd name is " + dictionary_list[4])  # Output: 2nd name is Raju

# Printing the entire dictionary
print(dictionary_list)  # Output: {1: 'Ram', 2: 'Shyam', 3: 'Balram', 4: 'Raju'}

# Printing all the keys of the dictionary
print(dictionary_list.keys())  # Output: dict_keys([1, 2, 3, 4])

# Printing all the values of the dictionary
print(dictionary_list.values())  # Output: dict_values(['Ram', 'Shyam', 'Balram', 'Raju'])
```

### Explanation:

1. **Dictionary Creation**:
   - A dictionary `dictionary_list` is created with integer keys (`1`, `2`, `3`, `4`) and corresponding string values (`'Ram'`, `'Shyam'`, `'Balram'`, `'Raju'`).

2. **Accessing Dictionary Values**:
   - The program uses keys to access specific values from the dictionary and prints them.

3. **Print Dictionary**:
   - The entire dictionary is printed, displaying all the key-value pairs.

4. **Keys and Values**:
   - `dictionary_list.keys()` prints all the keys of the dictionary.
   - `dictionary_list.values()` prints all the values stored in the dictionary.