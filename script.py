# -----CALCULATOR-----
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def main():

    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("""
ENTER OPERATION:
 1. Add
 2. Subtract
 3. Multiply
 4. Divide
"""))

            match c:
                case 1:
                    print(add(a,b))
                    break
                case 2:
                    print(subtract(a,b))
                    break
                case 3:
                    print(multiply(a,b))
                    break
                case 4:
                    print(divide(a,b))
                    break
                case _:
                    print("Invalid operation!")

        except ValueError:
            print("Please enter a valid number")



if __name__ == "__main__":
    main()