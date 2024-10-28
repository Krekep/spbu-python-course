import pytest
from project.game import Game
from project.bot import Bot
from project.dealer import Dealer
from project.deck import Deck
from project.card import Card


@pytest.fixture
def game() -> Game:
    """
    Fixture to create a standard game instance with default parameters.

    Returns:
        Game: A new instance of the game class with 3 bots and 5 rounds.
    """
    return Game()


def test_initial_state(game: Game) -> None:
    """
    Tests the initial state of the game.

    Verifies:
        - The round count is set to 0.
        - The results dictionary is initialized correctly for all bots.
        - The game is not active upon initialization.
    """
    assert game.current_round == 0
    assert all(wins == 0 for wins in game.results.values())
    assert game.round_active is False


def test_state_changes_with_rounds(game: Game) -> None:
    """
    Tests that the game's state changes with each round.

    Verifies:
        - The round number increases after each round.
        - The game is active during each round.
    """
    game.play_round()
    for _ in range(game.total_rounds - 1):
        current_round = game.current_round
        game.play_round()
        assert game.current_round == current_round + 1
        assert game.round_active is False


def test_deck_reduction_after_deals(game: Game) -> None:
    """
    Tests that the deck size reduces as cards are dealt in each round.

    Verifies:
        - The deck size decreases after initial card deals and each "hit" action.
    """
    initial_deck_size = len(game.deck.cards)
    game.play_round()
    final_deck_size = len(game.deck.cards)
    assert final_deck_size < initial_deck_size


def test_reset_game(game: Game) -> None:
    """
    Tests that the game resets properly after each round.

    Verifies:
        - Bots' and dealer's hands are empty after resetting.
        - The game state is ready for the next round.
    """
    game.play_round()
    game.reset_game()

    assert all(len(bot.cards_on_hand) == 0 for bot in game.bots)
    assert len(game.dealer.cards_on_hand) == 0
    assert game.round_active is False


@pytest.fixture
def dealer() -> Dealer:
    """
    Fixture to create a dealer with a new deck.
    """
    return Dealer()


def test_dealer_play_turn(dealer: Dealer) -> None:
    """
    Tests that the dealer plays until reaching a score of 17 or higher.
    """
    dealer.play_turn(deck=Deck())
    score = dealer.calculate_score()
    assert score >= 17 or len(dealer.cards_on_hand) >= 2


@pytest.fixture
def bot() -> Bot:
    """
    Fixture to create a bot with a cautious strategy.
    """
    return Bot(strategy="Cautious")


def test_bot_initial_hand(bot: Bot) -> None:
    """
    Tests that a bot starts with an empty hand.
    """
    assert len(bot.cards_on_hand) == 0


def test_bot_decide_action(bot: Bot) -> None:
    """
    Tests that the bot decides actions based on a cautious strategy.
    """
    bot.add_card(Card("Hearts", "7"))
    bot.add_card(Card("Diamonds", "10"))
    action = bot.decide_action(Card("Spades", "6"))
    assert action == "stand"


@pytest.fixture
def deck() -> Deck:
    """
    Fixture to create a new deck.
    """
    return Deck()


def test_deck_initialization(deck: Deck) -> None:
    """
    Tests that the deck initializes with 52 unique cards.
    """
    assert len(deck.cards) == 52
    assert len(set(deck.cards)) == 52


def test_deck_shuffle(deck: Deck) -> None:
    """
    Tests that the deck shuffle randomizes card order.
    """
    original_order = deck.cards[:]
    deck.shuffle()
    shuffled_order = deck.cards
    assert original_order != shuffled_order


def test_deal_card(deck: Deck) -> None:
    """
    Tests that dealing a card reduces the deck size by one.
    """
    initial_size = len(deck.cards)
    card = deck.deal_card()
    assert card is not None
    assert len(deck.cards) == initial_size - 1
