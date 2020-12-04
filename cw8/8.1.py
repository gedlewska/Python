def solve1(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Infinitely many solutions")
            else:
                print("No solutions")
        else:
            print("y =", -c / b)
    else:
        if b == 0:
            print("x =", -c / a)
        else:
            if c == 0:
                print("y = {0}x".format(str(-a / b)))
            else:
                print("y = {0}x + {1}".format(str(-a / b), str(-c / b)))


try:
    a = int(input("Write a: "))
    b = int(input("Write b: "))
    c = int(input("Write c: "))
except ValueError:
    print("Not a number")
else:
    print("Solution for equation {0}x + {1}y + {2} = 0:".format(str(a), str(b), str(c)))
    solve1(a, b, c)
