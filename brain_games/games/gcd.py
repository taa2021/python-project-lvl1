from random import randint


BANNER = "Find the greatest common divisor of given numbers."


# print(gcd()) = 0
# print(gcd(0)) = 0
# print(gcd(140, 96)) = 4
# print(gcd(8, 24)) = 8
# print(gcd(78, 294, 570, 36)) = 6
# print(gcd(-231, -140)) = 7
# print(gcd(-585, 81, -189)) = 9

# https://skysmart.ru/articles/mathematic/naibolshij-obshchij-delitel
# http://www.cleverstudents.ru/divisibility/nod_finding.html#3_or_more

# Return the greatest common divisor of the specified integer arguments.
# If any of the arguments is nonzero,
# then the returned value is the largest positive integer
# that is a divisor of all arguments. If all arguments are zero,
# then the returned value is 0.
# gcd() without arguments returns 0.
def gcd(*ints):
    if len(ints) == 0 or all([i == 0 for i in ints]):
        return 0
    if any([i < 0 for i in ints]):
        args = [abs(i) for i in ints]
        return gcd(*args)
    if len(ints) == 1:
        return ints[0]

    n_etc = list(ints[2:])
    (n0, n1) = (ints[0], ints[1]) if ints[0] <= ints[1] else (ints[1], ints[0])

    while n1 % n0:
        n0, n1 = n1 % n0, n0
        # print(f'{n0} {n1}')

    n_etc.append(n0)

    return gcd(*n_etc)


def round(gconf):
    arg0 = randint(gconf.RAND_NUM_MIN, gconf.RAND_NUM_MAX)
    arg1 = randint(gconf.RAND_NUM_MIN, gconf.RAND_NUM_MAX)

    value = gcd(arg0, arg1)

    question = f"{arg0} {arg1}"
    correct_answer = str(value)

    return (question, correct_answer)
