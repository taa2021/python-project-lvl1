import prompt


def message(text):
    print(text)


def welcome_app():
    message("Welcome to the Brain Games!")


def welcome_user():
    username = prompt.string("May I have your name? ")
    message(f"Hello, {username}!")

    return username


def ask_question(question):
    message(question)
    return prompt.string("Your answer: ")
