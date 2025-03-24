import turtle
import time

class ClockHands:
    def __init__(self):
        self.hour_hand = turtle.Turtle()
        self.minute_hand = turtle.Turtle()
        self.setup_hand(self.hour_hand)
        self.setup_hand(self.minute_hand)

        self.update()

    def setup_hand(self, hand):
        hand.speed(0)
        hand.hideturtle()
        hand.penup()
        hand.goto(0, 0)

    def update(self):
        now = time.localtime()
        hours = now.tm_hour % 12
        minutes = now.tm_min

        hour_angle = 30 * hours + 0.5 * minutes
        minute_angle = 6 * minutes

        self.draw_hand(self.hour_hand, hour_angle, 50)
        self.draw_hand(self.minute_hand, minute_angle, 70)

        turtle.ontimer(self.update, 60000)

    def draw_hand(self, hand, angle, length):
        hand.clear()
        hand.penup()
        hand.goto(0, 0)
        hand.pendown()
        hand.setheading(90 - angle)
        hand.forward(length)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Аналоговий годинник")

    hands = ClockHands()
    screen.mainloop()
