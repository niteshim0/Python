# Python Numbers

In Python, numbers are represented by different data types, primarily integers, floating-point numbers, and complex numbers.

## Integers (`int`)

Integers are whole numbers, positive or negative, without any decimal point. For example: `5`, `-10`, `1000`, etc. In Python, integers have unlimited precision.

## Floating-Point Numbers (`float`)

Floating-point numbers represent real numbers and are written with a decimal point dividing the integer and fractional parts. For example: `3.14`, `-0.001`, `2.0`, etc. Floating-point numbers are implemented using the IEEE 754 standard, but they have finite precision and may not always represent numbers exactly.

## Complex Numbers (`complex`)

Complex numbers have a real and imaginary part, both represented as floating-point numbers. They are written with a `j` or `J` suffix to denote the imaginary part. For example: `2 + 3j`, `1.5 - 2.5j`, etc.

Python provides various operations and functions for working with numbers. Here's an example program demonstrating some common operations:

```python
# Arithmetic operations
a = 5
b = 2
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
integer_division = a // b
modulo = a % b
exponentiation = a ** b

# Complex number operations
c1 = 2 + 3j
c2 = 1 - 1j
complex_addition = c1 + c2
complex_conjugate = c1.conjugate()
complex_absolute = abs(c1)

# Mathematical functions (require `import math`)
import math
sqrt_result = math.sqrt(16)
sin_result = math.sin(math.pi / 2)
cos_result = math.cos(math.pi)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Integer Division:", integer_division)
print("Modulo:", modulo)
print("Exponentiation:", exponentiation)
print("Complex Addition:", complex_addition)
print("Complex Conjugate:", complex_conjugate)
print("Complex Absolute:", complex_absolute)
print("Square Root:", sqrt_result)
print("Sine of pi/2:", sin_result)
print("Cosine of pi:", cos_result)
```

# Operations on Numbers in Python

In Python, you can perform various operations on numbers, including arithmetic operations, bitwise operations, and comparison operations. Here's an overview of each category with examples:

## 1. Arithmetic Operations:

Arithmetic operations involve basic mathematical calculations such as addition, subtraction, multiplication, division, etc.

```python
# Addition
result = 5 + 3
print("Addition:", result)

# Subtraction
result = 5 - 3
print("Subtraction:", result)

# Multiplication
result = 5 * 3
print("Multiplication:", result)

# Division
result = 5 / 3
print("Division:", result)

# Integer Division
result = 5 // 3
print("Integer Division:", result)

# Modulo (Remainder)
result = 5 % 3
print("Modulo:", result)

# Exponentiation
result = 5 ** 3
print("Exponentiation:", result)
```
## 2. Bitwise Operations:

Bitwise operations are performed on binary representations of numbers.

```python
# Bitwise AND
result = 5 & 3
print("Bitwise AND:", result)

# Bitwise OR
result = 5 | 3
print("Bitwise OR:", result)

# Bitwise XOR
result = 5 ^ 3
print("Bitwise XOR:", result)

# Bitwise NOT
result = ~5
print("Bitwise NOT:", result)

# Left Shift
result = 5 << 1
print("Left Shift:", result)

# Right Shift
result = 5 >> 1
print("Right Shift:", result)

```

## 3. Comparison Operations:

Comparison operations are used to compare two numbers and return a boolean result (True or False).

```python
# Equal to
result = 5 == 3
print("Equal to:", result)

# Not equal to
result = 5 != 3
print("Not equal to:", result)

# Greater than
result = 5 > 3
print("Greater than:", result)

# Less than
result = 5 < 3
print("Less than:", result)

# Greater than or equal to
result = 5 >= 3
print("Greater than or equal to:", result)

# Less than or equal to
result = 5 <= 3
print("Less than or equal to:", result)
```

# Typecasting in Python

In Python, typecasting refers to the conversion of one data type into another. Python provides built-in functions to perform typecasting between different data types. Here are some common typecasting functions:

### 1. `int()`

The `int()` function is used to convert a value to an integer.

```python
# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10

# Convert float to integer
num_float = 3.14
num_int = int(num_float)
print(num_int)  # Output: 3
```

### 2. `float()`

The `float()` function is used to convert a value to a floating-point number.

```python
# Convert integer to float
num_int = 10
num_float = float(num_int)
print(num_float)  # Output: 10.0
```

### 3. `str()`

The `str()` function is used to convert a value to a string.

```python
# Convert integer to string
num_int = 10
num_str = str(num_int)
print(num_str)  # Output: "10"

# Convert float to string
num_float = 3.14
num_str = str(num_float)
print(num_str)  # Output: "3.14"

```

### 4. `bool()`

The `bool()` function is used to convert a value to a boolean.

```python
# Convert integer to boolean
num_int = 0
bool_val = bool(num_int)
print(bool_val)  # Output: False

# Convert non-zero integer to boolean
num_int = 10
bool_val = bool(num_int)
print(bool_val)  # Output: True

# Convert string to boolean
bool_str = "True"
bool_val = bool(bool_str)
print(bool_val)  # Output: True

```

### 5. `list()`, `tuple()`, `set()`, `dict()`

You can also convert between different collection types using these functions.

```python
# Convert tuple to list
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print(list_data)  # Output: [1, 2, 3]

# Convert list to set
list_data = [1, 2, 3, 3, 4]
set_data = set(list_data)
print(set_data)  # Output: {1, 2, 3, 4}

# Convert list of tuples to dictionary
list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
dict_data = dict(list_of_tuples)
print(dict_data)  # Output: {1: 'one', 2: 'two', 3: 'three'}
```

# Math Module in Python

The `math` module in Python provides access to various mathematical functions and constants. These functions and constants are useful for performing mathematical operations in your Python programs. Here's an overview of commonly used functions and constants available in the `math` module:

### Mathematical Functions:

1. **Trigonometric Functions:**
   - `math.sin(x)`: Returns the sine of x (in radians).
   - `math.cos(x)`: Returns the cosine of x (in radians).
   - `math.tan(x)`: Returns the tangent of x (in radians).
   - `math.asin(x)`: Returns the arc sine of x, in radians.
   - `math.acos(x)`: Returns the arc cosine of x, in radians.
   - `math.atan(x)`: Returns the arc tangent of x, in radians.

2. **Exponential and Logarithmic Functions:**
   - `math.exp(x)`: Returns e raised to the power of x.
   - `math.log(x[, base])`: Returns the natural logarithm of x (to base e) or the logarithm of x to the given base.
   - `math.log10(x)`: Returns the base-10 logarithm of x.
   - `math.log2(x)`: Returns the base-2 logarithm of x.

3. **Power and Root Functions:**
   - `math.pow(x, y)`: Returns x raised to the power of y.
   - `math.sqrt(x)`: Returns the square root of x.
   - `math.pow(x, 1/3)`: Returns the cube root of x.

4. **Angular Conversion Functions:**
   - `math.degrees(x)`: Converts angle x from radians to degrees.
   - `math.radians(x)`: Converts angle x from degrees to radians.

5. **Constants:**
   - `math.pi`: A mathematical constant representing the ratio of the circumference of a circle to its diameter (approximately 3.14159).
   - `math.e`: A mathematical constant representing the base of the natural logarithm (approximately 2.71828).

### Example Usage:

```python
import math

# Calculate sine, cosine, and tangent
print("sin(π/2):", math.sin(math.pi / 2))
print("cos(π):", math.cos(math.pi))
print("tan(π/4):", math.tan(math.pi / 4))

# Calculate logarithms
print("log10(100):", math.log10(100))
print("ln(e):", math.log(math.e))  # natural logarithm of e

# Calculate power and roots
print("2^3:", math.pow(2, 3))
print("√25:", math.sqrt(25))

# Convert degrees to radians
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print("45 degrees in radians:", angle_radians)

# Print mathematical constants
print("π:", math.pi)
print("e:", math.e)

```

# Random Module in Python

The `random` module in Python provides functionalities for generating random numbers, shuffling sequences, and selecting random elements from sequences. Here's an overview of some commonly used functions in the `random` module:

### 1. Generating Random Numbers:

- `random.random()`: Returns a random floating-point number in the range [0.0, 1.0).
- `random.uniform(a, b)`: Returns a random floating-point number between a and b.
- `random.randint(a, b)`: Returns a random integer between a and b (inclusive).
- `random.randrange(start, stop[, step])`: Returns a randomly selected element from the range(start, stop, step).
- `random.choice(seq)`: Returns a random element from the non-empty sequence seq.
- `random.choices(population, weights=None, k=1)`: Returns a list with k elements chosen from the population with replacement.
- `random.sample(population, k)`: Returns a list with k unique elements chosen from the population without replacement.

### 2. Shuffling Sequences:

- `random.shuffle(x)`: Shuffles the sequence x in place.

### 3. Setting Random Seed:

- `random.seed(a=None, version=2)`: Initializes the random number generator with a seed. If the same seed is used, the sequence of generated random numbers will be the same.

### Example Usage:

```python
import random

# Generate random floating-point number
print("Random float:", random.random())

# Generate random integer between 1 and 100
print("Random integer:", random.randint(1, 100))

# Generate random number between 10 and 20
print("Random number between 10 and 20:", random.uniform(10, 20))

# Select random element from a list
colors = ['red', 'green', 'blue', 'yellow']
print("Random color:", random.choice(colors))

# Shuffle a list
deck = list(range(1, 53))
random.shuffle(deck)
print("Shuffled deck:", deck)

# Set random seed for reproducibility
random.seed(42)
print("Random number with seed 42:", random.random())

# Select multiple random elements from a list without replacement
sampled_numbers = random.sample(range(1, 101), 5)
print("Sampled numbers:", sampled_numbers)
```
# Number Bases in Python

In Python, numbers can be represented in various bases other than decimal (base 10). These include binary (base 2), octal (base 8), and hexadecimal (base 16). Here's how you can represent numbers in different bases:

### 1. Binary (Base 2):

- To represent a binary number in Python, prefix the number with `0b` or `0B`.

Example:
```python
binary_number = 0b1010
print("Binary number:", binary_number)  # Output: 10
```

### 2. Octal (Base 8):

- To represent an octal number in Python, prefix the number with `0o` or `0O`.

Example:
```python
octal_number = 0o10
print("Octal number:", octal_number)  # Output: 8
```

### 3. HexaDecimal (Base 16):

- To represent a hexadecimal number in Python, prefix the number with `0x` or `0X`.

Example:
```python
hexadecimal_number = 0xA
print("Hexadecimal number:", hexadecimal_number)  # Output: 10
```

## Converting Numbers to Other Bases:

You can convert numbers from decimal to other bases using the `bin()`, `oct()`, and `hex()` functions.

### Example:

```python
decimal_number = 10

# Convert to binary
binary_representation = bin(decimal_number)
print("Binary representation:", binary_representation)  # Output: 0b1010

# Convert to octal
octal_representation = oct(decimal_number)
print("Octal representation:", octal_representation)  # Output: 0o12

# Convert to hexadecimal
hexadecimal_representation = hex(decimal_number)
print("Hexadecimal representation:", hexadecimal_representation)  # Output: 0xa

```






