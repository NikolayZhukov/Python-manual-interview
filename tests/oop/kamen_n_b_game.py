import random

class Player:
    """Абстрактный класс игрока."""
    def __init__(self, name):
        self.name = name

    def make_move(self):
        """Метод, который должен быть переопределён в подклассах."""
        raise NotImplementedError("Метод make_move() должен быть переопределён в подклассе")


class HumanPlayer(Player):
    """Игрок, который делает выбор вручную."""
    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]
        move = None
        while move not in moves:
            move = input(f"{self.name}, выбери (камень/ножницы/бумага): ").strip().lower()
        return move


class ComputerPlayer(Player):
    """Игрок, который делает случайный выбор."""
    def make_move(self):
        return random.choice(["камень", "ножницы", "бумага"])


class Game:
    """Класс, управляющий процессом игры."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self, move1, move2):
        if move1 == move2:
            return None  # Ничья
        rules = {
            "камень": "ножницы",
            "ножницы": "бумага",
            "бумага": "камень"
        }
        # Если move2 — это то, что проигрывает move1, значит player1 выиграл
        if rules[move1] == move2:
            return self.player1
        return self.player2

    def play_round(self):
        move1 = self.player1.make_move()
        move2 = self.player2.make_move()

        print(f"\n{self.player1.name} выбрал: {move1}")
        print(f"{self.player2.name} выбрал: {move2}")

        winner = self.determine_winner(move1, move2)
        if winner:
            print(f"🎉 Победитель: {winner.name}!\n")
        else:
            print("🤝 Ничья!\n")

    def start(self, rounds=3):
        print("=== Игра: Камень, ножницы, бумага ===")
        for i in range(rounds):
            print(f"Раунд {i+1}:")
            self.play_round()
        print("=== Игра окончена ===")


# --- Использование ---
if __name__ == "__main__":
    human = HumanPlayer("Игрок")
    computer = ComputerPlayer("Компьютер")
    game = Game(human, computer)
    game.start()
