import random
class Hilo:
    def __init__(self):
        self.value = random.randint(1,13)
        self.points = 0

    def card_draw(self):
        self.value = random.randint(1,13)
        self.points = 0