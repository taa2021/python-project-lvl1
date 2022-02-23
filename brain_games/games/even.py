import prompt
from random import randint


def run(username):
    RAND_NUM_MIN = 1
    RAND_NUM_MAX = 99
    CORRECT_TRIES = 3

    print('Answer "yes" if the number is even, otherwise answer "no".')

    tries = 0
    while tries < CORRECT_TRIES:
        num = randint(RAND_NUM_MIN, RAND_NUM_MAX)

        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")

        correct_answer = "yes" if (num % 2) == 0 else "no"

        if correct_answer == answer.lower():
            tries += 1
            result = "Correct!"
        else:
            tries = 0
            result = "".join(
                [
                    f"'{answer}' is wrong answer ;(. ",
                    f"Correct answer was '{correct_answer}'.\n",
                    f"Let's try again, {username}!",
                ]
            )

        print(result)

    print(f"Congratulations, {username}!")
