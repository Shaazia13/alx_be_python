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
            operation_text = "addition"
        case '-':
            result = num1 - num2
            operation_text = "subtraction"
        case '*':
            result = num1 * num2
            operation_text = "multiplication"
        case '/':
            if num2 != 0:
                result = num1 / num2
                operation_text = "division"
            else:
                print("Cannot divide by zero.")
                return
        case _:
            print("Invalid operation entered.")
            return

    # Output the result
    if operation_text:
        print(f"The result of {operation_text} is {result}.")

# Run the calculator
if __name__ == "__main__":
    match_case_calculator()
