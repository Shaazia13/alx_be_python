# match_case_calculator.py

def match_case_calculator():
    # Input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Match case for operations
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero.")
                return
        case _:
            print("Invalid operation entered.")
            return

    # Output the result
    print(f"The result is {result}.")

# Run the calculator
if __name__ == "__main__":
    match_case_calculator()

