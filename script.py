# ----- CALCULATOR -----

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
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
            choice = int(input("Choose (1-4): "))
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

        match choice:
            case 1:
                result = add(a, b)
                operationUsed = "Sum"
            case 2:
                result = subtract(a, b)
                operationUsed = "Difference"
            case 3:
                result = multiply(a, b)
                operationUsed = "Product"
            case 4:
                result = divide(a, b)
                operationUsed = "Quotient"

        print(operationUsed + " is", result)

        again = input("\nDo you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()