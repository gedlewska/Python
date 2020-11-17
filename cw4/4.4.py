def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        prev = 1
        result = 1
        for item in range(2, n):
            temp = result
            result += prev
            prev = temp
        return result


try:
    number = int(input("Give number:"))
except ValueError:
    print("This is not a number")
else:
    print(fibonacci(number))
