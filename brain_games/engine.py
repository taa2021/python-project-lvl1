def run(gconf, game):
    ui = gconf.ui
    username = gconf.username

    if game.BANNER:
        ui.message(game.BANNER)

    ok = True
    for round in range(gconf.GAME_ROUNDS):
        (question, correct_answer) = game.round(gconf)

        answer = ui.ask_question(f"Question: {question}")
        correct_answer = correct_answer.strip().lower()

        ok = ok and correct_answer == answer.strip().lower()

        msg = (
            "Correct!"
            if ok
            else "".join(
                [
                    f"'{answer}' is wrong answer ;(. ",
                    f"Correct answer was '{correct_answer}'.",
                ]
            )
        )

        ui.message(msg)
        if gconf.GAME_END_ON_ERR and not ok:
            break

    msg = ("Congratulations" if ok else "Let's try again") + f", {username}!"
    ui.message(msg)
