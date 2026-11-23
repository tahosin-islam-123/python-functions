def factorial(n):
    if n < 0:
        return None

    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


number = int(input("Enter a non-negative integer: "))
answer = factorial(number)

if answer is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", answer)
