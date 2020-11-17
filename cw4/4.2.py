def draw_ruler():
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
        dots_len = len(dots)
        for item in range(number):
            to_add = ''.ljust(dots_len - len(str(item + 1)), ' ') + str(item + 1)
            result += to_add
        return result


def draw_net():
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
        return result


print(draw_ruler())
print(draw_net())
