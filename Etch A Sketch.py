import turtle
from turtle import *
my_turtle = Turtle()
screen = Screen()
screen.setup(width=1200, height=700)
comment1 = Turtle()
comment2 = Turtle()

def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def turn_left():
    new_heading = my_turtle.heading()+10
    my_turtle.setheading(new_heading)


def turn_right():
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)


def clear_reset():
    my_turtle.clear()
    my_turtle.reset()


screen.listen()
comment2.penup()
comment2.hideturtle()
comment2.goto(0, 320)
comment2.write("Etch A Sketch", False, align="center", font=("Courier", 20, "bold"))
comment1.penup()
comment1.hideturtle()
comment1.goto(0, 220)
comment1.write("Press:\n'f' to move forward \n'b' to move backward\n'l' to turn left \n'r' to "
              "turn right \n'c' to "
              "clear screen ", False, align="center", font=("Courier", 10, "bold"))
screen.onkey(key="f", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="c", fun=clear_reset)

screen.exitonclick()
