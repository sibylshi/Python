from turtle import Turtle


class PrintName(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()

    def print_name(self, name, xcor, ycor,):
        self.goto(xcor, ycor)
        self.write(name, move=False, align='center', font=('Arial', 20, 'normal'))
