import prompt
from random import randint


def run(username):
    RAND_NUM_MIN = 1
    RAND_NUM_MAX = 99
    CORRECT_TRIES = 3

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for round in range(CORRECT_TRIES):
        num = randint(RAND_NUM_MIN, RAND_NUM_MAX)

        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")

        correct_answer = "yes" if (num % 2) == 0 else "no"

        if correct_answer == answer.lower():
            print("Correct!")
        else:
            print(
                "".join(
                    [
                        f"'{answer}' is wrong answer ;(. ",
                        f"Correct answer was '{correct_answer}'.\n",
                        f"Let's try again, {username}!",
                    ]
                )
            )
            return

    print(f"Congratulations, {username}!")
