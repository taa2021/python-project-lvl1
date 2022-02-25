import brain_games.cli as ui
import brain_games.engine as engine
import brain_games.gconf as gconf


def script_main(games):
    ui.welcome_app()

    gconf.ui = ui
    gconf.username = ui.welcome_user()

    for game in games:
        engine.run(gconf, game)
