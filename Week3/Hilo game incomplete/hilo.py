import random
class Hilo:
    """
    A card that has a number on it

    Keeps track of cards and their values
        value: (int) The number on the card
    """
    def __init__(self):
        self.value = random.randint(1, 13)

class Director:
    """
    Runs the game 

    When total scord reaches 0 the game stops, if the player does not 
    want to play again the game stops 
    """
    def __init__(self):
        
        self.score = 300
        self.total_score = 0
        self.cards = []
        self.is_playing = True
        self.card = Hilo()
        self.cards.append(self.card)
        self.i = 0
        self.card_now = 0
        self.card_next = 0
        
    def start_game(self):
        """
        Starts the game by running the main game loop.
        """
        while self.is_playing:
            self.get_prompts()

    def do_updates(self, card_guess):
        """
        Updates game play, produces new scord and creates new cards
        """
        if not self.is_playing:
            return 
        self.cards.append(self.card)
        card = self.cards[self.i]
        self.card_now = card.value
        self.i += 1
        card = self.cards[self.i]
        self.card_next = card.value
        if card_guess == "h" and self.card_next > self.card_now:
            points = 100
        else:
            points = -75
        self.score += points 
        self.total_score += self.score

    def get_prompts(self):
        """
        Displays the game to the user
        Runs prompts
        """
        if not self.is_playing:
            return 
        card = self.cards[self.i]
        print(f"The card is: {card.value}")
        card_guess = input("Higher or lower? [h/l] ")
        self.do_updates(card_guess)
        print(f"Next card was: {card.value}")
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.total_score > 0)
        play_again = input("Play again? [y/n]")
        print("")
        if play_again == "n":
            self.is_playing == False
            return
        
def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()