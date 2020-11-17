import math


def reduce_frac(x, y):
    d = math.gcd(x, y)
    return [x // d, y // d]


def add_frac(frac1, frac2):
    return reduce_frac(frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1])


def sub_frac(frac1, frac2):
    return reduce_frac(frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1])


def mul_frac(frac1, frac2):
    return reduce_frac(frac1[0] * frac2[0], frac1[1] * frac2[1])


def div_frac(frac1, frac2):
    return reduce_frac(frac1[0] * frac2[1], frac1[1] * frac2[0])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    sub = sub_frac(frac1, frac2)
    if is_zero(sub):
        return 0
    elif is_positive(sub):
        return 1
    else:
        return -1


def frac2float(frac):
    return [float(frac[0]), float(frac[1])]
