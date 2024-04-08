# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10

# Convert float to integer
num_float = 3.14
num_int = int(num_float)
print(num_int)  # Output: 3

# Convert integer to float
num_int = 10
num_float = float(num_int)
print(num_float)  # Output: 10.0

# Convert integer to string
num_int = 10
num_str = str(num_int)
print(num_str)  # Output: "10"

# Convert float to string
num_float = 3.14
num_str = str(num_float)
print(num_str)  # Output: "3.14"

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
