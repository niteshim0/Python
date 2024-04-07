# Python Data Types

In Python, data types refer to the classification of data items. Python has several built-in data types, which include:

1. **Numeric Types**:
   - Integers (`int`): Whole numbers without a fractional part, e.g., 5, -3, 1000.
   - Floating-point numbers (`float`): Numbers with a decimal point or an exponential (e.g., 3.14, -0.001, 2e3).

2. **Sequence Types**:
   - Strings (`str`): Ordered collection of characters enclosed within single, double, or triple quotes, e.g., "hello", 'Python', '''multi-line string'''.
   - Lists (`list`): Ordered collection of items enclosed within square brackets, e.g., [1, 2, 3], ['a', 'b', 'c'].
   - Tuples (`tuple`): Ordered collection of items enclosed within parentheses, e.g., (1, 2, 3), ('a', 'b', 'c'). Tuples are immutable.
   
3. **Mapping Types**:
   - Dictionaries (`dict`): Collection of key-value pairs enclosed within curly braces, e.g., {'name': 'John', 'age': 30}. Keys must be unique within a dictionary.

4. **Set Types**:
   - Sets (`set`): Unordered collection of unique items enclosed within curly braces, e.g., {1, 2, 3}, {'a', 'b', 'c'}.
   - Frozen Sets (`frozenset`): Immutable version of sets.

5. **Boolean Type**:
   - Boolean (`bool`): Represents True or False values. Used in logical operations and control flow.

6. **Binary Types**:
   - Bytes (`bytes`): Immutable sequence of bytes, e.g., b'hello'.
   - Byte Arrays (`bytearray`): Mutable sequence of bytes.

7. **None Type**:
   - None (`NoneType`): Represents the absence of a value or a null value.

Python also supports complex numbers (`complex`), which are represented as a sum of a real and imaginary part, e.g., 3 + 4j.

You can use the `type()` function to determine the data type of a variable or a value.

# Every Data Type is an Object in Python

In Python, every data type is an object. This is a fundamental principle of Python's design, reflecting its object-oriented nature.

An object in Python is a piece of memory that stores a value and has associated operations (functions/methods) that you can perform on it. Each object has a type, which determines the kind of value it represents and the operations that can be performed on it.

When you create a variable in Python and assign it a value, you are actually creating an object of a specific type and binding it to that variable name. For example:

```python
x = 5
```

