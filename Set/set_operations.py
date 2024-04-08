# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Creating a set from a list
my_list = [1, 2, 3, 4, 5]
set_from_list = set(my_list)
print("Set from list:", set_from_list)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

my_set.add(6)
print("After adding:", my_set)

# Removing elements from a set
my_set.remove(3)
print("After removing:", my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# Membership testing
print("Is 3 in set1?", 3 in set1)  # Output: True
print("Is 9 in set1?", 9 in set1)  # Output: False

squares_set = {x ** 2 for x in range(1, 6)}
print("Squares set:", squares_set)  # Output: {1, 4, 9, 16, 25}

