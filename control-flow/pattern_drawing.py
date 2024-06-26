# pattern_drawing.py

def draw_square_pattern(size):
    # Outer while loop for rows
    row = 0
    while row < size:
        # Inner for loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

if __name__ == "__main__":
    size = int(input("Enter the size of the pattern: "))
    draw_square_pattern(size)
