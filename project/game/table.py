from project.game.players import Bot, Croupier


class RouletteTable:
    def __init__(self):
        self.croupier = Croupier()

    def play_game(self, bot: Bot) -> None:
        print(f"The player {bot.name} starts the game with a balance {bot.balance}.")
        bot.play(self.croupier)
        winning_number, winning_color = self.croupier.spin_wheel()
        print(f"The number dropped out: {winning_number} ({winning_color})")
