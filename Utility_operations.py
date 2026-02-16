def calculate_average(*numbers):
    """Calculates average using *args"""
    return sum(numbers) / len(numbers)

def calculator_info(**details):
    """Displays calculator info using **kwargs"""
    for key, value in details.items():
        print(f"{key} : {value}")

def modify_list(values):
    """
    Demonstrates pass by reference
    Modifies original list
    """
    values.append(100)
