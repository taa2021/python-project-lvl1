from random import randint


BANNER = "What number is missing in the progression?"

SEQ_LEN_MIN = 5
SEQ_LEN_MAX = 10
SEQ_STEP_MIN = 2
SEQ_STEP_MAX = 9

def progression(el0_min, el0_max):
    step = randint(SEQ_STEP_MIN, SEQ_STEP_MAX)
    length = randint(SEQ_LEN_MIN, SEQ_LEN_MAX)

    el_min = randint(el0_min, el0_max)

    return list([ str(el_min + i*step) for i in range(length)])


def round(gconf):
    pr = progression(gconf.RAND_NUM_MIN, gconf.RAND_NUM_MAX)
    missing_element = randint(0, len(pr)-1)

    pr_with_missing_el = list()
    pr_with_missing_el.extend(pr[0:missing_element])
    pr_with_missing_el.append('..')
    pr_with_missing_el.extend(pr[missing_element+1:])

    question = ' '.join(pr_with_missing_el)
    correct_answer = pr[missing_element]

    return (question, correct_answer)
