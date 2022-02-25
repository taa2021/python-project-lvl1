from random import randint


BANNER = 'Answer "yes" if the number is even, otherwise answer "no".'


def round(gconf):
    num = randint(gconf.RAND_NUM_MIN, gconf.RAND_NUM_MAX)
    correct_answer = "yes" if (num % 2) == 0 else "no"

    return (str(num), correct_answer)
