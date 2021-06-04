def factorial(number):
    if number <= 1:
        return number
    return number * factorial(number - 1)


result = factorial(4)
print("This factorial result:", result)
