try:
    first = int(input("Write first size: "))
    second = int(input("Write second size: "))
except ValueError:
    print("This is not a number")
else:
    result = ""
    for item in range(2 * first + 1):
        if item % 2 == 0:
            result += "+"
            for i in range(second):
                result += "---+"
            result += "\n"
        else:
            result += "|"
            for i in range(second):
                result += "   |"
            result += "\n"
    print(result)
