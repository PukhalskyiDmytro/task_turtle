import turtle

def draw_segment(x, y, dx, dy, active):
    if active:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x + dx, y + dy)
        turtle.penup()

def draw_digit(digit, x, y):
    segments = {
        '0': [1, 1, 1, 1, 1, 1, 0],
        '1': [0, 1, 1, 0, 0, 0, 0],
        '2': [1, 1, 0, 1, 1, 0, 1],
        '3': [1, 1, 1, 1, 0, 0, 1],
        '4': [0, 1, 1, 1, 0, 1, 1],
        '5': [1, 0, 1, 1, 0, 1, 1],
        '6': [1, 0, 1, 1, 1, 1, 1],
        '7': [1, 1, 1, 0, 0, 0, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1]
    }
    seg = segments[digit]
    positions = [
        (x, y, 40, 0), (x + 40, y, 0, -50), (x + 40, y - 50, 0, -50),
        (x, y - 100, 40, 0), (x, y - 50, 0, -50), (x, y, 0, -50),
        (x, y - 50, 40, 0)
    ]
    for i in range(7):
        draw_segment(*positions[i], seg[i])

def draw_colon(x, y):
    turtle.penup()
    turtle.goto(x + 10, y - 30)
    turtle.pendown()
    turtle.dot(7)
    turtle.penup()
    turtle.goto(x + 10, y - 70)
    turtle.pendown()
    turtle.dot(7)

def draw_time(time_str, start_x, start_y):
    x = start_x
    for char in time_str:
        if char == ':':
            draw_colon(x, start_y)
            x += 30
        else:
            draw_digit(char, x, start_y)
            x += 80

turtle.speed(3)
draw_time("456789", -200, 150)
turtle.hideturtle()
turtle.done()

