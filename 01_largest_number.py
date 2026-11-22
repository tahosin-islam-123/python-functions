# Program 1: Find the largest of two numbers using a function

def find_largest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = find_largest(num1, num2)
print("Result:", result)
