def fibonacci(count):
    series = []
    first, second = 0, 1

    for _ in range(count):
        series.append(first)
        first, second = second, first + second

    return series


terms = int(input("How many terms do you want? "))

if terms < 0:
    print("Please enter a non-negative number.")
else:
    print("Fibonacci series:", fibonacci(terms))
