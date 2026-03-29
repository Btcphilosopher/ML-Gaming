class Game:
    def __init__(self):
        self.state = 'start'
        self.turn = 0

    def start_game(self):
        print("Game started! It is turn 1.")
        self.play_turn()

    def play_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}:")
        self.generate_events()
        self.player_choice()
        self.update_state()

        if self.turn < 5:
            self.play_turn()  # Continue playing until turn 5
        else:
            self.end_game()

    def generate_events(self):
        print("Events have been generated for this turn.")

    def player_choice(self):
        choice = input("Choose an action (1: Attack, 2: Defend, 3: Heal): ")
        print(f"Player chose action {choice}.")

    def update_state(self):
        print("Game state updated.")

    def end_game(self):
        print("Game Over. Thanks for playing!")


if __name__ == '__main__':
    game = Game()
    game.start_game()