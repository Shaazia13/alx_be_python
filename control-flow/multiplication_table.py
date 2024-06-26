# multiplication_table.py

def generate_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    number = int(input("Enter a number to see its multiplication table: "))
    generate_multiplication_table(number)
