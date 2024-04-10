# Python Strings

In Python, a string is a sequence of characters enclosed within either single quotes (`'`) or double quotes (`"`) or triple quotes(`"""`). For example:

```python
my_string = 'Hello, World!'
another_string = "This is another string."
another_string2 = """ Hello , how are you ?. """
```
Strings in Python are immutable, meaning once they are created, their contents cannot be changed. However, you can create new strings based on existing strings.

# Important Python String Methods

Python provides a rich set of built-in string methods that are essential for string manipulation tasks. Here are some of the most commonly used ones:

1. **`split(sep=None, maxsplit=-1)`**: Splits the string into a list of substrings based on the specified separator (`sep`). If `sep` is not provided, whitespace characters are used as default separators. The optional argument `maxsplit` specifies the maximum number of splits to perform.

    ```python
    sentence = "Hello, world! This is a sentence."
    words = sentence.split()  # Splitting by default (whitespace)
    print(words)
    # Output: ['Hello,', 'world!', 'This', 'is', 'a', 'sentence.']

    parts = sentence.split(", ")  # Splitting by comma and space
    print(parts)
    # Output: ['Hello', 'world! This is a sentence.']
    ```

2. **`strip(chars=None)`**: Returns a copy of the string with leading and trailing whitespace removed. If `chars` is provided, it specifies a string of characters to be removed from the leading and trailing ends of the string.

    ```python
    string = "   This is a string.   "
    cleaned_string = string.strip()
    print(cleaned_string)
    # Output: 'This is a string.'

    string_with_chars = "###ABC#Hello, world!#ABC###"
    cleaned_string = string_with_chars.strip("#ABC")
    print(cleaned_string)
    # Output: 'Hello, world!'
    ```

3. **`join(iterable)`**: Concatenates the elements of an iterable (e.g., a list) into a single string, with the original string used as a separator between elements.

    ```python
    words = ["Hello", "world", "Python"]
    sentence = " ".join(words)
    print(sentence)
    # Output: 'Hello world Python'

    characters = ['a', 'b', 'c', 'd']
    string = '-'.join(characters)
    print(string)
    # Output: 'a-b-c-d'
    ```

4. **`lower()`** and **`upper()`**: These methods return copies of the string with all characters converted to lowercase (`lower()`) or uppercase (`upper()`), respectively.

    ```python
    string = "Hello, World!"
    print(string.lower())
    # Output: 'hello, world!'

    print(string.upper())
    # Output: 'HELLO, WORLD!'
    ```

5. **`replace(old, new, count=-1)`**: Returns a copy of the string with occurrences of the substring `old` replaced by `new`. The optional argument `count` specifies the maximum number of replacements to perform.

    ```python
    sentence = "The quick brown fox jumps over the lazy dog."
    new_sentence = sentence.replace("lazy", "sleepy")
    print(new_sentence)
    # Output: 'The quick brown fox jumps over the sleepy dog.'
    ```

6. **`startswith(prefix)`** and **`endswith(suffix)`**: These methods return `True` if the string starts with `prefix` or ends with `suffix`, respectively; otherwise, they return `False`.

    ```python
    string = "Hello, World!"
    print(string.startswith("Hello"))
    # Output: True

    print(string.endswith("!"))
    # Output: True
    ```

7. **`find(sub[, start[, end]])`** and **`index(sub[, start[, end]])`**: These methods search for the first occurrence of the substring `sub` within the string. `find()` returns the lowest index where `sub` is found (or -1 if not found), while `index()` raises a ValueError if `sub` is not found.

    ```python
    sentence = "Python is a powerful language."
    print(sentence.find("Python"))
    # Output: 0

    print(sentence.index("powerful"))
    # Output: 12
    ```

8. **`isdigit()`**, **`isalpha()`**, **`isalnum()`**, **`isspace()`**: These methods return `True` if the string contains only digits, alphabetic characters, alphanumeric characters, or whitespace characters, respectively.

    ```python
    number = "12345"
    print(number.isdigit())
    # Output: True

    name = "JohnDoe"
    print(name.isalpha())
    # Output: True

    password = "Secret123"
    print(password.isalnum())
    # Output: True

    whitespace = "   "
    print(whitespace.isspace())
    # Output: True
    ```

9. **`format()`**: Formats the string according to the specified format string and optional arguments. This method is powerful for string interpolation and formatting.

    ```python
    name = "John"
    age = 30
    print("My name is {} and I am {} years old.".format(name, age))
    # Output: 'My name is John and I am 30 years old.'
    ```

10. **`len()`** : This function returns the number of characters in the string, including whitespace characters.

    ```python
    my_string = "Hello, World!"
    length = len(my_string)
    print("Length of the string:", length)
    # Output: Length of the string: 13
    ```

11. **`count()`** : The count() method in Python is used to count the number of occurrences of a specified substring within a string. It returns the count as an integer.
     
     ```python
       sentence = "Peter Piper picked a peck of pickled peppers."
       count_of_p = sentence.count('p')
       print("Count of 'p':", count_of_p)  # Output: Count of 'p': 8

       count_of_peck = sentence.count('peck')
       print("Count of 'peck':", count_of_peck)  # Output: Count of 'peck': 1

       # Count occurrences of 'p' between index 10 and 20 (exclusive)
       count_within_range = sentence.count('p', 10, 20)
       print("Count of 'p' within range:", count_within_range)  # Output: Count of 'p' within range: 2

     ```

# Using ord() and chr() Functions in Python

In Python, `ord()` and `chr()` are built-in functions used to convert characters to their Unicode code points and vice versa.

- The `ord()` function takes a character as an argument and returns its Unicode code point (an integer representing the Unicode value of the character).
- The `chr()` function takes an integer representing a Unicode code point and returns the corresponding character.

Here's how you can use `ord()` and `chr()`:

```python
# Using ord() to get Unicode code point of a character
char = 'A'
unicode_value = ord(char)
print("Unicode code point of '{}' is: {}".format(char, unicode_value))
# Output: Unicode code point of 'A' is: 65

# Using chr() to get character from Unicode code point
code_point = 65
character = chr(code_point)
print("Character with Unicode code point {} is: '{}'".format(code_point, character))
# Output: Character with Unicode code point 65 is: 'A'
```

# Slicing in Python Strings

In Python, slicing is a technique used to extract a portion of a string by specifying start and stop indices. The syntax for slicing a string in Python is:

```python
string[start:stop:step]
```
where
 - **start** : Optional. The index representing the start of the slice (inclusive). If not provided, it defaults to 0, indicating the beginning of the string.
 - **stop**  : Required. The index representing the end of the slice (exclusive). This means the slice will include characters up to, but not including, the character at this index.
 - **step**  : Optional. The step or increment between characters in the slice. If not provided, it defaults to 1.

### Example : 

```python
string = "Hello, World!"

# Get the substring from index 7 to the end of the string
substring1 = string[7:]
print(substring1)  # Output: 'World!'

# Get the substring from index 0 to index 5 (exclusive)
substring2 = string[:5]
print(substring2)  # Output: 'Hello'

# Get the substring from index 7 to index 12 (exclusive)
substring3 = string[7:12]
print(substring3)  # Output: 'World'

# Get every second character in the string
substring4 = string[::2]
print(substring4)  # Output: 'Hlo ol!'

# Reverse the string
substring5 = string[::-1]
print(substring5)  # Output: '!dlroW ,olleH'

```

# Raw String Treatment in Python

In Python, a raw string is a string that is prefixed with the letter 'r' or 'R'. Raw strings treat backslashes (`\`) as literal characters instead of interpreting them as escape characters. This means that backslashes are treated as part of the string rather than indicating special characters like newline (`\n`) or tab (`\t`).

Here's an example to illustrate the difference between regular and raw strings:

```python
regular_string = "This is a regular string with a newline character: \n"
raw_string = r"This is a raw string with a newline character: \n"

print(regular_string)
print(raw_string)
```

# Including Special Characters in String in Python

In Python, you can include special characters in strings using escape sequences. Escape sequences are combinations of characters that have a special meaning within a string. They are prefixed by a backslash (`\`). Here are some commonly used escape sequences in Python:

- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\"`: Double quote
- `\'`: Single quote

Here's an example demonstrating how to include special characters in strings using escape sequences:

```python
# Including special characters in strings using escape sequences
string_with_newline = "Line 1\nLine 2"
print(string_with_newline)

string_with_tab = "Name:\tJohn"
print(string_with_tab)

string_with_backslash = "This is a backslash: \\"
print(string_with_backslash)

string_with_double_quote = "He said, \"Hello!\""
print(string_with_double_quote)

string_with_single_quote = 'She\'s happy'
print(string_with_single_quote)
```

**Output** : 
```vbnet
Line 1
Line 2
Name:   John
This is a backslash: \
He said, "Hello!"
She's happy
```

# Iterating Over a String in Python

In Python, there are several ways to iterate over a string. You can use loops such as `for` loops or `while` loops, or you can directly iterate over the characters of the string using a `for` loop or comprehension. Here are some common methods:

1. **Using a `for` loop:**

    ```python
    my_string = "Hello, World!"

    for char in my_string:
        print(char)
    ```

2. **Using a `while` loop with an index:**

    ```python
    my_string = "Hello, World!"

    index = 0
    while index < len(my_string):
        print(my_string[index])
        index += 1
    ```

3. **Using built-in `enumerate()` function with a `for` loop:**

    ```python
    my_string = "Hello, World!"

    for index, char in enumerate(my_string):
        print(f"Character at index {index}: {char}")
    ```

4. **Using list comprehension:**

    ```python
    my_string = "Hello, World!"

    characters = [char for char in my_string]
    print(characters)
    ```

5. **Using generator expression:**

    ```python
    my_string = "Hello, World!"

    characters = (char for char in my_string)
    for char in characters:
        print(char)
    ```




