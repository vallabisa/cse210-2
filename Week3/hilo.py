class hilo:
    def __init__(self):
        self.value = 0
        self.points = 0

    

class director:
    def __init__(self):
        
        self.score = 300
        self.total_score = 0
        self.cards = []
        self.is_playing = True
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_prompt()
            self.do_updates()


    def get_prompt(self):
        print(f"The card is: {self.cards}")
        card_guess = input("Higher or lower? [h/1] ")
        print(f"Next card is: {self.cards}")
        print(self.total_score)
        run_again = input("Play again? [y/n]")
        self.is_playing = (run_again == "y")


    def do_updates(self):
        if not self.is_playing:
            return 
    
def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()