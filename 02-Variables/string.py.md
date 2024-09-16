Here’s the code with added comments and a brief explanation:

```python
# Example of String
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Defining string variables
str1 = 'hello Ram'  # string str1
str2 = ' How are you'  # string str2

# Printing first two characters of str1 using the slice operator
print(str1[0:2])  # Output: he

# Printing the 9th character of the string str1 (index 8 as indexing starts from 0)
print(str1[8])  # Output: m

# Printing the string str1 twice
print(str1 * 2)  # Output: hello Ramhello Ram

# Printing the concatenation of str1 and str2
print(str1 + str2)  # Output: hello Ram How are you
```

### Explanation:

1. **String Creation**:
   - Two string variables `str1` and `str2` are defined: `str1 = 'hello Ram'` and `str2 = ' How are you'`.

2. **String Slicing**:
   - `str1[0:2]`: This uses slicing to extract and print the first two characters of `str1`, which are `'he'`.

3. **Accessing a Specific Character**:
   - `str1[8]`: This accesses the 9th character (index `8`) of `str1`, which is `'m'`.

4. **String Repetition**:
   - `str1 * 2`: This repeats the string `str1` twice, printing `'hello Ramhello Ram'`.

5. **String Concatenation**:
   - `str1 + str2`: This concatenates `str1` and `str2` into a single string, resulting in `'hello Ram How are you'`.
