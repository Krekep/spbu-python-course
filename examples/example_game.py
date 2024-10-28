from project.game import Game


def main():
    """Starts the Blackjack game and displays the status for each round."""
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
