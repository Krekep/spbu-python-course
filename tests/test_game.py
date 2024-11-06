import pytest
from project.game import Game
from project.bot import CautiousBot
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
    assert game._current_round == 0
    assert all(wins == 0 for wins in game._results.values())
    assert game._round_active is False


def test_state_changes_with_rounds(game: Game) -> None:
    """
    Tests that the game's state changes with each round.

    Verifies:
        - The round number increases after each round.
        - The game is active during each round.
    """
    game.play_round()
    for _ in range(game._total_rounds - 1):
        current_round = game._current_round
        game.play_round()
        assert game._current_round == current_round + 1
        assert game._round_active is False


def test_deck_reduction_after_deals(game: Game) -> None:
    """
    Tests that the deck size reduces as cards are dealt in each round.

    Verifies:
        - The deck size decreases after initial card deals and each "hit" action.
    """
    initial_deck_size = len(game._deck.cards)
    game.play_round()
    final_deck_size = len(game._deck.cards)
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

    assert all(len(bot.hand.cards) == 0 for bot in game._bots)
    assert len(game._dealer.hand.cards) == 0
    assert game._round_active is False


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
    score = dealer.hand.calculate_score()
    assert score >= 17


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


@pytest.fixture
def cautious_bot() -> CautiousBot:
    """Fixture to create a bot with a cautious strategy."""
    return CautiousBot()


def test_bot_initial_hand(cautious_bot: CautiousBot) -> None:
    """Tests that a cautious bot starts with an empty hand."""
    assert len(cautious_bot.hand.cards) == 0


def test_bot_cautious_does_not_draw_extra_card(
    cautious_bot: CautiousBot, deck: Deck
) -> None:
    """
    Tests that a cautious bot does not draw an extra card when it has a high score.
    """
    cautious_bot.hand.add_card(Card("Hearts", "7"))
    cautious_bot.hand.add_card(Card("Diamonds", "10"))

    initial_card_count = len(cautious_bot.hand.cards)

    cautious_bot.decide_action(Card("Spades", "6"), deck)

    assert len(cautious_bot.hand.cards) == initial_card_count
