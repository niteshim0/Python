# Mutable and Immutable in Python

In Python, objects can be categorized into two main types based on whether their state can be modified after creation: mutable and immutable.

1. **Mutable Objects**:
   Mutable objects are those whose state can be changed after creation. This means you can modify their content, add, remove, or update elements without changing their identity. Examples of mutable objects in Python include lists, dictionaries, sets, and objects of custom classes that are designed to be mutable.

   ```python
   # Example of mutable objects
   my_list = [1, 2, 3]  # This list can be modified
   my_dict = {'a': 1, 'b': 2}  # This dictionary can be modified
