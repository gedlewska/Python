def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for item in range(2, n + 1):
            result = result * item
    return result


try:
    number = int(input("Give number:"))
except ValueError:
    print("This is not a number")
else:
    print(factorial(number))
