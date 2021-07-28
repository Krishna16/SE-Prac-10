import turtle
import random

#function to convert rgb values
#to a hex value
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

shapes = ["Square", "Circle", "Rectangle", "Equilateral Triangle", "Regular Pentagon"]

#random_shape = random.choice(shapes)
random_shape = "Equilateral Triangle"

if (random_shape == "Square"):
    side = random.randint(50, 150)

    #go to the random position
    turtle.penup()
    turtle.goto(random.randint(-100, 0), random.randint(0, 100))
    turtle.pendown()

    #start filling the color of the shape
    turtle.fillcolor(rgb_to_hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
    turtle.begin_fill()

    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

    turtle.end_fill()

elif (random_shape == "Circle"):
    turtle.fillcolor(rgb_to_hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    turtle.penup()
    turtle.goto(random.randint(-100, 0), random.randint(0, 100))
    turtle.pendown()
    
    turtle.begin_fill()
    radius = random.randint(50, 150)
    turtle.circle(radius)
    turtle.end_fill()

elif (random_shape == "Rectangle"):
    n = random.randint(50, 150)

    width = 2 * n
    height = n

    turtle.penup()
    turtle.goto(random.randint(-100, 0), random.randint(0, 100))
    turtle.pendown()

    turtle.fillcolor(rgb_to_hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

    turtle.end_fill()

elif (random_shape == "Equilateral Triangle"):
    side = random.randint(50, 150)

    turtle.penup()
    turtle.goto(random.randint(-100, 0), random.randint(0, 100))
    turtle.pendown()

    turtle.begin_fill()

    turtle.fillcolor(rgb_to_hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)

    turtle.end_fill()

elif (random_shape == "Regular Pentagon"):
    side = random.randint(50, 150)

    turtle.penup()
    turtle.goto(random.randint(-100, 0), random.randint(0, 100))
    turtle.pendown()

    turtle.begin_fill()

    turtle.fillcolor(rgb_to_hex((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)

    turtle.end_fill()
