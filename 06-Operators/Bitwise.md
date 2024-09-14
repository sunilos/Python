Here’s the code with added comments and a brief explanation:

```python
# Example of Bitwise Operator
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Initialize variables
a = 60            # 60 in binary is 0011 1100
b = 13            # 13 in binary is 0000 1101
c = 0

# Bitwise AND
c = a & b         # 60 & 13 = 12 (in binary: 0000 1100)
print("Line 1 - Value of c is", c)  # Output will be 12

# Bitwise OR
c = a | b         # 60 | 13 = 61 (in binary: 0011 1101)
print("Line 2 - Value of c is", c)  # Output will be 61

# Bitwise XOR
c = a ^ b         # 60 ^ 13 = 49 (in binary: 0011 0001)
print("Line 3 - Value of c is", c)  # Output will be 49

# Bitwise NOT
c = ~a            # ~60 = -61 (in binary: 1100 0011, bitwise NOT inverts the bits)
print("Line 4 - Value of c is", c)  # Output will be -61

# Bitwise Left Shift
c = a << 2        # 60 << 2 = 240 (in binary: 1111 0000, shifts bits to the left by 2 positions)
print("Line 5 - Value of c is", c)  # Output will be 240

# Bitwise Right Shift
c = a >> 2        # 60 >> 2 = 15 (in binary: 0000 1111, shifts bits to the right by 2 positions)
print("Line 6 - Value of c is", c)  # Output will be 15
```

### Explanation:

1. **Initialization**:
   - `a = 60` (binary: `0011 1100`)
   - `b = 13` (binary: `0000 1101`)

2. **Bitwise AND (`&`)**:
   - `a & b` results in `12` (binary: `0000 1100`), where bits are set to `1` only if they are `1` in both operands.

3. **Bitwise OR (`|`)**:
   - `a | b` results in `61` (binary: `0011 1101`), where bits are set to `1` if they are `1` in either operand.

4. **Bitwise XOR (`^`)**:
   - `a ^ b` results in `49` (binary: `0011 0001`), where bits are set to `1` if they are different in the operands.

5. **Bitwise NOT (`~`)**:
   - `~a` results in `-61` (binary: `1100 0011`). Bitwise NOT inverts all the bits.

6. **Bitwise Left Shift (`<<`)**:
   - `a << 2` shifts the bits of `a` to the left by 2 positions, resulting in `240` (binary: `1111 0000`).

7. **Bitwise Right Shift (`>>`)**:
   - `a >> 2` shifts the bits of `a` to the right by 2 positions, resulting in `15` (binary: `0000 1111`).

This code demonstrates the usage of various bitwise operators and their effects on binary representations of integers.