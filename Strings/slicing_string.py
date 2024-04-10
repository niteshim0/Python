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
