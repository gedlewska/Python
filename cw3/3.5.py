result = "| "
dots = ". . . . | "
number = input("How long measure do you want: ")
try:
    number = int(number)
except ValueError:
    print("This is not a number")
else:
    for item in range(number):
        result += dots
    result += "\n0"
    dotsLen = len(dots)
    for item in range(number):
        toAdd = ''.ljust(dotsLen - len(str(item + 1)), ' ') + str(item + 1)
        result += toAdd
    print(result)
