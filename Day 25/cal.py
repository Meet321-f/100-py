#---math functions---
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


logo = """
_____________________
|  _________________  |
| | Python Calc   0.| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def calculator():
    print(logo)
    print("Welcome to the Python Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        print("\nAvailable Operations:")
        for symbol in operations:
            print(f"  {symbol}")

        operation_symbol = input("Pick an operation from the above line: ")
        if operation_symbol not in operations:
            print("Invalid operation selected. Try again.")
            continue

        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print("-" * 30)
        print(f"result of {num1} {operation_symbol} {num2} = {answer}")
        print("-" * 30)

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ).lower()

        if choice == 'y':
            num1 = answer
            continue
        elif choice == 'n':
            print("Starting a new calculation...")
            break
        else:
            print("Invalid choice. Starting a new calculation...")
            break


calculator()



