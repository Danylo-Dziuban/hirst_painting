from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 30)
y = -200

screen = Screen()
screen.setup(width=1900, height=1000)
screen.colormode(255)

boy = Turtle()

boy.shape('circle')
boy.teleport(x=-200, y=y)

for _ in range(11):

    for _ in range(11):
        color = random.choice(colors).rgb

        boy.color(color)
        boy.dot(25)
        boy.up()
        boy.forward(50)
        boy.down()

    y += 50
    boy.teleport(x=-200, y=y)

screen.exitonclick()
