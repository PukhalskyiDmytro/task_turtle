import turtle

class Digit:
    def __init__(self, n):
        self.n = int(n)

    def __call__(self):
        def draw_segment(x, y, dx, dy, active):
            if active:
                turtle.width(15)
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x + dx, y + dy)
                turtle.penup()

        def draw_digit(digit, x_offset=0):
            segments = {
                '0': [1, 1, 1, 1, 1, 1, 0],
                '1': [0, 1, 1, 0, 0, 0, 0],
                '2': [1, 1, 0, 1, 1, 0, 1],
                '3': [1, 1, 1, 1, 0, 0, 1],
                '4': [0, 1, 1, 0, 0, 1, 1],
                '5': [1, 0, 1, 1, 0, 1, 1],
                '6': [1, 0, 1, 1, 1, 1, 1],
                '7': [1, 1, 1, 0, 0, 0, 0],
                '8': [1, 1, 1, 1, 1, 1, 1],
                '9': [1, 1, 1, 1, 0, 1, 1]
            }
            seg = segments[str(digit)]
            positions = [
                (x_offset, 0, 40, 0),
                (x_offset + 40, 0, 0, -50),
                (x_offset + 40, -50, 0, -50),
                (x_offset, -100, 40, 0),
                (x_offset, -50, 0, -50),
                (x_offset, 0, 0, -50),
                (x_offset, -50, 40, 0)
            ]
            for i in range(7):
                draw_segment(*positions[i], seg[i])

        turtle.speed(0)
        turtle.delay(0)

        if self.n > 9:
            draw_digit(self.n // 10)
            draw_digit(self.n % 10, 80)
        else:
            draw_digit(self.n)

        turtle.hideturtle()
        turtle.done()

if __name__ == '__main__':
        Digit(99)()
