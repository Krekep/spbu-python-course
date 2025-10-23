class Card:
    """
    Represents a playing card with suit, rank and value.
    """
    
    def __init__(self, suit: str, rank: str, value: int) -> None:
        """
        Initializes a card with given suit, rank and value.

        Parameters:
            suit : str (Card suit like "Hearts", "Spades", etc.)
            rank : str (Card rank like "A", "2", "10", "K", etc.)
            value : int (Numerical value of the card)
        """
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def __str__(self) -> str:
        """
        Returns string representation of the card.

        Returns:
            str: String in format "rank of suit"
        """
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self) -> str:
        """
        Returns detailed string representation for debugging.

        Returns:
            str: String in format "Card('suit', 'rank', value)"
        """
        return f"Card('{self.suit}', '{self.rank}', {self.value})"
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two cards are equal by comparing suit, rank and value.

        Parameters:
            other : object (Another object to compare with)

        Returns:
            bool: True if cards are identical, False otherwise
        """
        if not isinstance(other, Card):
            return False
        return (self.suit == other.suit and 
                self.rank == other.rank and 
                self.value == other.value)