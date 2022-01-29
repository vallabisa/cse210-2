from game.hilo import Hilo
class Director:
    def __init__(self):
        
        self.is_playing = True
        
        self.total_score = 300
        
      
        

    def start_game(self):
        self.card = Hilo()
        while self.is_playing:
            
            self.previous_card = self.card.value
            print(f"\nThe card is: {self.previous_card}")
            self.do_updates()
            self.outputs()
            self.get_prompt()




    def do_updates(self):
        if not self.is_playing:
            return 
        
        guess = input("Higher or lower? [h/l] ")
        self.card = Hilo()
        next_card = self.card.value
        print(f"Next card is: {next_card}")
        
        if guess == "h" and (next_card >= self.previous_card):
            self.total_score += 100
        elif guess == "l" and (next_card <= self.previous_card):
            self.total_score += 100
        else:
            self.total_score -= 75

        
       
        
    def outputs(self):
        print(f"Your score is: {self.total_score}")

    def get_prompt(self):
        if self.total_score <= 0:
            self.is_playing = False
        else:
            run_again = input("Play again? [y/n] ")
            self.is_playing = (run_again == "y")

