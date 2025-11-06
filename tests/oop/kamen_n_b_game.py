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
        self.count_player1 = 0
        self.count_player2 = 0
        self.round = 0

    def determine_winner(self, move1, move2):
        if move1 == move2:
            print('Ничья')
            return None  # Ничья
        rules = {
            "камень": "ножницы",
            "ножницы": "бумага",
            "бумага": "камень"
        }
        if rules[move1] == move2:
            self.count_player1 += 1
            print(f'{self.player1.name} набрал {self.count_player1} очко/очка')
        else:
            self.count_player2 += 1
            print(f'{self.player2.name} набрал {self.count_player2} очко/очка')

    def play_round(self):
        move1 = self.player1.make_move()
        move2 = self.player2.make_move()

        print(f"\n{self.player1.name} выбрал: {move1}")
        print(f"{self.player2.name} выбрал: {move2}")

        self.determine_winner(move1, move2)

    def start(self):
        while self.count_player1 < 2 and self.count_player2 < 2:
            self.round += 1
            print(f"=== Раунд {self.round} ===")
            self.play_round()

        if self.count_player1 == 2:
            print(f'{self.player1.name} победил, он набрал {self.count_player1} очка!')
            print("=== Игра окончена ===")
        if self.count_player2 == 2:
            print(f'{self.player2.name} победил, он набрал {self.count_player2} очка!')
            print("=== Игра окончена ===")



# --- Использование ---
if __name__ == "__main__":
    human = HumanPlayer("Человек")
    computer = ComputerPlayer("Компьютер")
    game = Game(human, computer)
    game.start()
