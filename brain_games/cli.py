import prompt


def welcome_app():
    print("Welcome to the Brain Games!")


def welcome_user():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')

    return username
