import turtle
import time

class Dial:
    def __init__(self, t):
        self.smallHand = Hand()
        self.bigHand =  Hand()

        self.hours = 0
        self.minutes = 0
        self.digits = [Digit() for i in range (0, 11)]
        self.t = t

        while True:
            self.draw()
            time.sleep(t)

    def draw(self):
        self.draw()
        self.smallHand.draw(self.hours)
        self.bigHand.draw(self.minutes)
        for i in range(0, 11):
            self.digits[i].draw(i+1)
