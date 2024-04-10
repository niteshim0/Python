# Lists in Python

In Python, a list is a built-in data structure used to store collections of items. Lists are ordered, mutable (modifiable), and can contain elements of different data types. They are defined by enclosing comma-separated values within square brackets `[ ]`. Here's an example of a list:

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
# Output: [1, 2, 3, 4, 5]
mixed_list = [1, 'apple', True, 3.14, [5, 6, 7]]
print(mixed_list)
# Output: [1, 'apple', True, 3.14, [5, 6, 7]]
print(my_list[0])   # Output: 1
print(my_list[-1])  # Output: 5
```
# Commonly Used Built-in Methods for Python Lists

Here are some of the most commonly used built-in methods for Python lists:

1. **`append(x)`**: Adds an item `x` to the end of the list.

    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

2. **`extend(iterable)`**: Extends the list by appending elements from the iterable.

    ```python
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```

3. **`insert(i, x)`**: Inserts an item `x` at a specified index `i`.

    ```python
    my_list = [1, 2, 3]
    my_list.insert(1, 4)
    print(my_list)  # Output: [1, 4, 2, 3]
    ```

4. **`remove(x)`**: Removes the first occurrence of item `x` from the list.

    ```python
    my_list = [1, 2, 3, 4, 3]
    my_list.remove(3)
    print(my_list)  # Output: [1, 2, 4, 3]
    ```

5. **`pop(i)`**: Removes and returns the item at index `i`. If no index is specified, removes and returns the last item in the list.

    ```python
    my_list = [1, 2, 3, 4]
    popped_item = my_list.pop(1)
    print(popped_item)  # Output: 2
    ```

6. **`clear()`**: Removes all items from the list.

    ```python
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list)  # Output: []
    ```

7. **`index(x, start, end)`**: Returns the index of the first occurrence of item `x`. Optionally, start and end indices can be provided to search within a specific range.

    ```python
    my_list = [1, 2, 3, 4, 3]
    index = my_list.index(3)
    print(index)  # Output: 2
    ```

8. **`count(x)`**: Returns the number of occurrences of item `x` in the list.

    ```python
    my_list = [1, 2, 3, 4, 3]
    count = my_list.count(3)
    print(count)  # Output: 2
    ```

9. **`sort(key=None, reverse=False)`**: Sorts the items of the list in place.

    ```python
    my_list = [3, 1, 4, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

10. **`reverse()`**: Reverses the elements of the list in place.

    ```python
    my_list = [1, 2, 3, 4]
    my_list.reverse()
    print(my_list)  # Output: [4, 3, 2, 1]
    ```

11. **`copy`** : Returns a shallow copy of the list.

    ```python
    my_list = [1, 2, 3]
    copied_list = my_list.copy()
    print(copied_list)  # Output: [1, 2, 3]
    ```

# Slicing in Python Lists

Slicing in Python lists allows you to extract a portion of the list by specifying a start index, an end index, and an optional step size. The syntax for slicing a list is similar to slicing a string.

Here's the general syntax:

```python
new_list = original_list[start:end:step]
```
where

- **start** : Optional. The index to start slicing from (inclusive). If not provided, it defaults to 0.
- **stop**  :Required. The index to stop slicing (exclusive). If not provided, it defaults to the end of the list.
- **step**  :Optional. The step or increment between elements in the slice. If not provided, it defaults to 1.

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get a slice of the list from index 2 to index 5 (exclusive)
slice1 = my_list[2:5]
print(slice1)  # Output: [2, 3, 4]

# Get a slice of the list from index 3 to the end
slice2 = my_list[3:]
print(slice2)  # Output: [3, 4, 5, 6, 7, 8, 9]

# Get a slice of the list from the beginning to index 6 (exclusive)
slice3 = my_list[:6]
print(slice3)  # Output: [0, 1, 2, 3, 4, 5]

# Get a slice of the list with a step of 2
slice4 = my_list[::2]
print(slice4)  # Output: [0, 2, 4, 6, 8]

# Reverse the list using slicing
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

```

# Iterating Over a List in Python

Iterating over a list in Python can be done using loops such as `for` loops or `while` loops, or by using built-in functions like `enumerate()`. Here are examples of different ways to iterate over a list:

1. **Using a `for` loop:**

    ```python
    my_list = [1, 2, 3, 4, 5]

    for item in my_list:
        print(item)
    ```

2. **Using a `while` loop with an index:**

    ```python
    my_list = [1, 2, 3, 4, 5]
    index = 0

    while index < len(my_list):
        print(my_list[index])
        index += 1
    ```

3. **Using built-in `enumerate()` function with a `for` loop:**

    ```python
    my_list = [1, 2, 3, 4, 5]

    for index, item in enumerate(my_list):
        print(f"Index {index}: {item}")
    ```

4. **Using list comprehension:**

    ```python
    my_list = [1, 2, 3, 4, 5]

    [item for item in my_list]
    ```

5. **Using generator expression:**

    ```python
    my_list = [1, 2, 3, 4, 5]

    (generator_expression for item in my_list)
    ```





