from functools import reduce

# Lambda functions
square = lambda x: x * x
cube = lambda x: x * x * x

def square_list(numbers):
    """Returns square of all numbers using map"""
    return list(map(lambda x: x * x, numbers))

def even_numbers(numbers):
    """Filters even numbers using filter"""
    return list(filter(lambda x: x % 2 == 0, numbers))

def sum_all(numbers):
    """Returns sum using reduce"""
    return reduce(lambda a, b: a + b, numbers)
