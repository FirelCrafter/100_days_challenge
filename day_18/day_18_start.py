from turtle import Turtle, Screen, colormode
from random import choice, randint

timmy_the_turtle = Turtle()
colormode(255)


# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

def set_color():
    return tuple([randint(0, 255) for _ in range(3)])


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(set_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


timmy_the_turtle.speed("fastest")


draw_spirograph(5)

# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)









# for _ in range(200):
#     timmy_the_turtle.color(set_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(choice(directions))




# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(choice(colors))
#     draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
