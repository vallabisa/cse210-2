class hilo:
    pass

class director:
    def __init__(self):
        
        self.score = 300
        self.cards = []
        self.is_playing = True
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_updates()
            self.get_prompt()

    def get_prompt(self):
        print(f"The card is: {self.cards}")
        card_guess = input("Higher or lower? [h/1] ")

    def do_updates(self):
        if not self.is_playing:
            return 
    
def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()