from project.game.players import Bot, Croupier


class RouletteTable:
    """
    The RouletteTable class represents a roulette table where the game is played.
    It manages the croupier and facilitates the gameplay for a bot.

    Attributes:
        croupier (Croupier): The croupier handling the roulette wheel.

    Methods:
        __init__(): Initializes the roulette table with a croupier.
        play_game(bot: Bot) -> None: Simulates a game of roulette with the given bot.
    """

    def __init__(self):
        """
        The RouletteTable class represents a roulette table where the game is played.
        It manages the croupier and facilitates the gameplay for a bot.

        Attributes:
            croupier (Croupier): The croupier handling the roulette wheel.

        Methods:
            __init__(): Initializes the roulette table with a croupier.
            play_game(bot: Bot) -> None: Simulates a game of roulette with the given bot.
        """
        self.croupier = Croupier()

    def play_game(self, bot: Bot) -> None:
        """
        Simulates a game of roulette with the given bot.

        Args:
            bot (Bot): The bot playing the game.
        """
        print(f"The player {bot.name} starts the game with a balance {bot.balance}.")
        bot.play(self.croupier)
        winning_number, winning_color = self.croupier.spin_wheel()
        print(f"The number dropped out: {winning_number} ({winning_color})")
