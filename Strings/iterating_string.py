my_string = "Hello, World!"

for char in my_string:
    print(char)


my_string = "Hello, World!"

index = 0
while index < len(my_string):
    print(my_string[index])
    index += 1


my_string = "Hello, World!"

for index, char in enumerate(my_string):
    print(f"Character at index {index}: {char}")


my_string = "Hello, World!"

characters = [char for char in my_string]
print(characters)


my_string = "Hello, World!"

characters = (char for char in my_string)
for char in characters:
    print(char)
