from turtle import Turtle,Screen
import turtle as t
from print_name import PrintName
import time
my_screen = Screen()
image = "blank_states_img.gif"
my_screen.addshape(image)
t.shape(image)
t.tracer(0)


# data process
import pandas
states = pandas.read_csv("50_states.csv")
names = states["state"].to_list()
print(names)

answered = []


game_on = True
score = 0
while game_on:

    time.sleep(0.1)
# pop ups
    input = my_screen.textinput(title="State Name", prompt="What is the name of the state?")
# check answer
# print name on the state
    if input == "exit":
        break
    # answered = [name for state in states if input.lower() in names ]
    for name in names:
# another method
    # if input.lower() in names:
        if name.lower() == input.lower():
            score += 1
            row = states[states.state == name]
            xcor = int(row.x)
            ycor = int(row.y)
            pn = PrintName()
            pn.print_name(name, xcor, ycor)
            answered.append(name)

# new_list = set(names)-set(answered)
new_list = [name for name in names if name not in answered]
print(new_list)
edu = pandas.DataFrame(new_list)
edu.to_csv("unanswered.csv")



