def add(a, b):
    """Returns sum of two numbers"""
    return a + b

def subtract(a, b):

    """Returns difference of two numbers"""
    return a - b

def multiply(a, b):
    """Returns product of two numbers"""
    return a * b

def divide(a, b=1):
    """
    Returns division result
    Default argument used for denominator
    """
    if b == 0:
        return "Division by zero not allowed"
    return a / b
