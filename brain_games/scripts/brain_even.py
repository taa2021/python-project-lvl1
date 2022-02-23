#!/usr/bin/env python
from brain_games.cli import welcome_app, welcome_user
import brain_games.games.even as game_even


def main():
    welcome_app()
    username = welcome_user()
    game_even.run(username)


if __name__ == '__main__':
    main()
