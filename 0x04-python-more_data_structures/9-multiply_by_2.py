#!/usr/bin/python3
def multiply_by_2(a_dictionary):
   return {k: v * 2 for k, v in a_dictionary.items()}

# Example usage:
my_dictionary = {'a': 3, 'b': 5, 'c': 7}
result = multiply_by_2(my_dictionary)
print(result)
