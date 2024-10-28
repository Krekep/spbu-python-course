class Card:
    """
    Represents a single card in a deck for a blackjack game.

    Attributes:
        suit (str): The suit of the card.
        value (str): The face value of the card.
        points (int): The points associated with the card.
    """

    SUITS: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES: dict[str, int] = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    def __init__(self, suit: str, value: str) -> None:
        """
        Initializes a card instance.

        Args:
            suit (str): The suit of the card.
            value (str): The face value of the card.

        Raises:
            ValueError: If suit or value is invalid.
        """
        if suit not in Card.SUITS or value not in Card.VALUES:
            raise ValueError("Invalid card suit or value")
        self.suit: str = suit
        self.value: str = value
        self.points: int = Card.VALUES[value]

    def __repr__(self) -> str:
        """
        Returns a string representation of the card.

        Returns:
            str: A string in the format 'value of suit'.
        """
        return f"{self.value} of {self.suit}"
