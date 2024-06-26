# multiplication_table.py

def multiplication_table():
    # Input from user
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print multiplication table
    for i in range(1, 11):  # iterate from 1 to 10
        result = number * i
        print(f"{number} * {i} = {result}")

# Run the multiplication table generator
if __name__ == "__main__":
    multiplication_table()
