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