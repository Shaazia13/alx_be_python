def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to perform calculations based on user input
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operation. Please choose one of +, -, *, /."

# Main program execution
if __name__ == "__main__":
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    operation = input("Choose the operation (+, -, *, /): ").strip()

    result = calculate(num1, num2, operation)
    print(f"The result is {result}.")
