from Basic_operation import add, subtract, multiply, divide
from Advanced_operation import square_list, even_numbers, sum_all
from Utility_operations import calculate_average, calculator_info, modify_list

print("=== Python Modular Calculator ===")

calculator_info(
    version="1.0",
    developer="Student",
    purpose="Interview Practical"
)

while True:
    print("""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square List
6. Filter Even Numbers
7. Sum of List
8. Average of Numbers
9. Pass by Reference Demo
0. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 0:
        break

    elif choice in [1, 2, 3, 4]:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))

    elif choice in [5, 6, 7]:
        nums = list(map(int, input("Enter numbers separated by space: ").split()))

        if choice == 5:
            print("Squares:", square_list(nums))
        elif choice == 6:
            print("Even Numbers:", even_numbers(nums))
        elif choice == 7:
            print("Sum:", sum_all(nums))

    elif choice == 8:
        nums = list(map(int, input("Enter numbers: ").split()))
        print("Average:", calculate_average(*nums))

    elif choice == 9:
        data = [1, 2, 3]
        modify_list(data)
        print("Modified List:", data)

    else:
        print("Invalid choice")
