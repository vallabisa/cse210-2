import random
class Hilo:
    """
    A card that has a number on it

    Keeps track of cards and their values
        value: (int) The number on the card
    """
    def __init__(self):
        self.value = 0
        
    def set_value(self):
        """
        Set the card value
        """
        self.value = random.randint(1, 13)

class Director:
    """
    Runs the game 

    When the score reaches 0 the game stops, if the player does not 
    want to play again the game stops 
    """
    def __init__(self):    
        self.score = 300
        self.cards = []
        self.is_playing = True
        self.card = Hilo()
        self.card.set_value()
        self.cards.append(self.card)
        self.i = 0
        self.card_now = 0
        self.card_next = 0
        
    def start_game(self):
        """
        Starts the game by running the main game loop.
        """
        while self.is_playing == True:
            self.get_prompts()

    def do_updates(self, card_guess):
        """
        Updates game play, produces new scord and creates new cards
        """
        if not self.is_playing:
            return 
        card = self.cards[self.i]
        self.card_now = card.value
        self.cards.append(self.card)
        self.i += 1
        card = self.cards[self.i]
        card.set_value()
        self.card_next = card.value
        if card_guess == "h" and self.card_next > self.card_now:
            self.score += 100
        elif card_guess == "l" and self.card_next < self.card_now:
            self.score += 100
        else:
            self.score -= 75

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
        print(f"Next card was: {self.card_next}")
        print(f"Your score is: {self.score}")
        if self.score < 0:
            self.is_playing == False
            return
        play_again = input("Play again? [y/n]")
        print("")
        self.is_playing = (play_again == "y")


        
def main():
    """
    Call the director class to run the game.
    """
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()