import sys

def sum_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <num1> <num2>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    result = sum_numbers(num1, num2)
    print("Sum:", result)
