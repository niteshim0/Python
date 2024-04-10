# 1.split

sentence = "Hello, world! This is a sentence."
words = sentence.split()  # Splitting by default (whitespace)
print(words)
# Output: ['Hello,', 'world!', 'This', 'is', 'a', 'sentence.']

parts = sentence.split(", ")  # Splitting by comma and space
print(parts)
# Output: ['Hello', 'world! This is a sentence.']

# 2.strip

string = "   This is a string.   "
cleaned_string = string.strip()
print(cleaned_string)
# Output: 'This is a string.'

string_with_chars = "###ABC#Hello, world!#ABC###"
cleaned_string = string_with_chars.strip("#ABC")
print(cleaned_string)
# Output: 'Hello, world!'

# 3.join

words = ["Hello", "world", "Python"]
sentence = " ".join(words)
print(sentence)
# Output: 'Hello world Python'

characters = ['a', 'b', 'c', 'd']
string = '-'.join(characters)
print(string)
# Output: 'a-b-c-d'
    
# 4.lower and upper

string = "Hello, World!"
print(string.lower())
# Output: 'hello, world!'

print(string.upper())
# Output: 'HELLO, WORLD!'

# 5.replace

sentence = "The quick brown fox jumps over the lazy dog."
new_sentence = sentence.replace("lazy", "sleepy")
print(new_sentence)
# Output: 'The quick brown fox jumps over the sleepy dog.'

# 6.startswith and endswith

string = "Hello, World!"
print(string.startswith("Hello"))
# Output: True

print(string.endswith("!"))
# Output: True

# 7.find and index

sentence = "Python is a powerful language."
print(sentence.find("Python"))
# Output: 0

print(sentence.index("powerful"))
# Output: 12

# 8.count

sentence = "Peter Piper picked a peck of pickled peppers."
count_of_p = sentence.count('p')
print("Count of 'p':", count_of_p)  # Output: Count of 'p': 8

count_of_peck = sentence.count('peck')
print("Count of 'peck':", count_of_peck)  # Output: Count of 'peck': 1

# Count occurrences of 'p' between index 10 and 20 (exclusive)
count_within_range = sentence.count('p', 10, 20)
print("Count of 'p' within range:", count_within_range)  # Output: Count of 'p' within range: 2

# 9.capitalize

string = "hello, world!"
print(string.capitalize())

# 10.title

string = "hello, world!"
print(string.title())

# 11.swapcase

string = "Hello, World!"
print(string.swapcase())

# 12.center

string = "Hello, World!"
print(string.center(20, '*'))

#13. isalpha, isalnum, isdigit, isdecimal, isspace,

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

# 14. format

name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: 'My name is John and I am 30 years old.'

# 15. len

string = "Hello, World!"
print(len(string))

# 16. ord and chr

print(ord('a'))
# Output: 97


print(chr(97))
# Output: 'a'


