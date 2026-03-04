# ----- CALCULATOR -----

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError( "Error: Cannot divide by zero.")
    return a / b


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Please enter valid numbers.\n")


def get_operation():
    print("""
ENTER OPERATION:
1. Add
2. Subtract
3. Multiply
4. Divide
""")
    while True:
        try:
            choice = int(input("Choose: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please choose 1-4.\n")
        except ValueError:
            print("Please enter a valid number.\n")


def main():
    operationUsed = ""
    while True:
        a, b = get_numbers()
        choice = get_operation()

        if choice == 1:
            result = add(a, b)
            operationUsed = "Sum"
        elif choice == 2:
            result = subtract(a, b)
            operationUsed = "Difference"
        elif choice == 3:
            result = multiply(a, b)
            operationUsed = "Product"
        elif choice == 4:
            try:
                result = divide(a, b)
                operationUsed = "Quotient"
            except ZeroDivisionError as e:
                print(e)

        if result.is_integer():
            print(f"The {operationUsed} is {result:g}")
        else:
            print(f"The {operationUsed} is {result:.2f}")

        again = input("\nDo you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()

