import operator as op
from random import randint


BANNER = "What is the result of the expression?"

OPS = [
    dict(func=op.add, str="+"),
    dict(func=op.sub, str="-"),
    dict(func=op.mul, str="*"),
]


def round(gconf):
    op_index = randint(0, len(OPS) - 1)
    arg0 = randint(gconf.RAND_NUM_MIN, gconf.RAND_NUM_MAX)
    arg1 = randint(gconf.RAND_NUM_MIN, gconf.RAND_NUM_MAX)

    value = OPS[op_index]["func"](arg0, arg1)
    op_str = OPS[op_index]["str"]

    question = f"{arg0} {op_str} {arg1}"
    correct_answer = str(value)

    return (question, correct_answer)
