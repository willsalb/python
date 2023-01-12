import turtle as ttl
import time
import random

delay = 0.1
score = 0
high_score = 0

windowScreen = ttl.Screen()
windowScreen.title('Snake Game')
windowScreen.bgcolor('black')

windowScreen.setup(width=720, height=600)
windowScreen.tracer(0)

head = ttl.Turtle()
head.shape("square")
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'Stop'

food = ttl.Turtle()
colors = random.choice(['red', 'green', 'pink'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = ttl.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 High Score: 0", align="center", font=("times new roman", 22, "bold"))




windowScreen.mainloop()