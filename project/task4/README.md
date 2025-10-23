# Blackjack Game

A comprehensive Python implementation of the classic Blackjack (21) card game with multiple AI strategies, human players, and extensive testing.

## 🎮 Game Overview

This Blackjack implementation features:

- **Multiple player types**: Human players and AI bots with different strategies
- **Realistic game flow**: Betting, card dealing, player decisions, dealer rules
- **Three AI strategies**: Conservative, Aggressive, and Basic mathematical strategy
- **Comprehensive game state tracking**: Round history, player statistics, game reports
- **Full test coverage**: Unit tests, integration tests, and type checking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```
git clone <repository-url>
cd spbu-python-course
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## 🎯 How to Play

### Basic Rules

- Card Values: 2-10 face value, J/Q/K = 10, A = 1 or 11
- Goal: Get closer to 21 than the dealer without going over
- Blackjack: Ace + 10-value card = automatic 3:2 payout
- Dealer Rules: Must hit on 16 or less, stand on 17 or more

### Game Flow

- Betting Phase: All players place their bets
- Initial Deal: Two cards each to players and dealer (one dealer card hidden)
- Player Turns: Each player decides to Hit, Stand, or Double
- Dealer Turn: Dealer reveals hidden card and plays according to rules
- Payouts: Winners get paid, losers lose their bets

## 🎮 Usage Examples

### Run Main Game (Human vs Bots)
```
cd project/task4
python3 main.py
```

This starts an interactive game where you play against three AI bots with different strategies.

### Run Strategy Comparison
```
cd project/task4/examples
python3 strategy_comparison.py
```

Compares the performance of different AI strategies over multiple games.

### Run Basic Example
```
cd project/task4/examples
python basic_example.py
```

Demonstrates a short game with detailed state tracking.

### Run Dealer Blackjack Example
```
cd project/task4/examples
python dealer_blackjack_example.py
```

Shows special handling when dealer gets blackjack.

### Run Full Game Example
```
cd project/task4/examples
python full_game_example.py
```

Plays a complete game with automatic round reports.

## 🧪 Testing

### Run All Tests
```
make test
```

### Run Unit Tests Only
```
make test-unit
```

### Run Integration Tests
```
make test-integration
```

### Run with Coverage
```
make coverage
```

### Check Code Quality
```
make check-imports
```

### Clean Build Artifacts
```
make clean
```

## 🔧 Development Commands

### Full CI Pipeline
```
make ci
```

Runs:

- Import checking
- Unit tests
- Integration tests
- Format checking

### Type Checking
```
mypy project
```

## 🎲 Game Features

### Player Types

- HumanPlayer: Interactive player with console input
- Bot: AI player using configurable strategies
- Dealer: Automated dealer following casino rules

### AI Strategies

- Conservative: Cautious play, stands on relatively low values
- Aggressive: Risk-taking, hits on higher values
- Basic: Mathematical optimal strategy considering dealer's card

### Game Features

- Multiple decks: Configurable number of decks (default: 6)
- Round limits: Configurable maximum rounds
- Bankruptcy detection: Players automatically sit out when out of chips
- Detailed reporting: Round-by-round game state tracking
- Game history: Complete record of all played rounds

## 📊 Example Output
```
♠♣♥♦ НАЧАЛО ИГРЫ В BLACKJACK ♠♣♥♦
Игроки: ['Игрок', 'Консервативный Бот', 'Агрессивный Бот', 'Тактический Бот']
Максимум раундов: 20

=== РАУНД 1 ===

--- Ставки ---
--- Ставка Игрок ---
Доступно фишек: 1000
Введите размер ставки: 100
Ставка 100 принята!
🤖 Консервативный Бот ставит 75 фишек
🤖 Агрессивный Бот ставит 214 фишек
🤖 Тактический Бот ставит 150 фишек
```

## 📈 Performance Notes

- The Basic strategy is mathematically optimal for long-term play
- Conservative strategy has lower variance but smaller potential wins
- Aggressive strategy can produce big wins but higher risk of losses
- Game automatically handles deck reshuffling when needed

## 📄 License

This project is part of the SPBU Python course assignments.

### Enjoy playing Blackjack! 🎰♠️♣️♥️♦️
