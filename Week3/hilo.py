import random
class Hilo:
    def __init__(self):
        self.value = random.randint(1, 13)
        self.points = 0

    def card_draw(self):
        if self.value == 

class Director:
    def __init__(self):
        
        self.score = 300
        self.total_score = 0
        self.cards = []
        self.is_playing = True
        self.card = Hilo()
        self.cards.append(self.card)
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_prompt()
            self.do_updates()


    def get_prompt(self):
        i = 0
        j = 1
        print(f"The card is: {self.card.value[i]}")
        card_guess = input("Higher or lower? [h/l] ")
        self.cards.append(self.card)
        print(f"Next card is: {self.card.value[j]}")
        print(self.total_score)
        run_again = input("Play again? [y/n]")
        if run_again == "y":
            i += 1
            j += 1
        self.is_playing = (run_again == "y")


    def do_updates(self):
        if not self.is_playing:
            return 
        
        card = self.cards[]
        card.card_draw()
        self.score += card.points 
        self.total_score += self.score

def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()