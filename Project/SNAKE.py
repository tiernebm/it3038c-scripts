# SNAKE GAME
# BRETT TIERNEY
import turtle
import time
import random

delay = 0.1

#Set Up screen
window =turtle.Screen()
window.title("Snake Game by BRETT TIERNEY")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

#SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "right"

#FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
 
#body
segments = []

#Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)                

def goUp():
    head.direction = "up"

def goDown():
    head.direction = "down"

def goLeft():
    head.direction = "left"

def goRight():
    head.direction = "right"

#KeyBINDING
window.listen()
window.onkeypress(goUp, "w")
window.onkeypress(goDown, "s")
window.onkeypress(goLeft, "a")
window.onkeypress(goRight, "d")


#GAME LOOp
while True:
    window.update()

    #colison check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()


    #check for food eat
    if head.distance(food)<20:
        # move food to random spot
     x = random.randint(-290,290)
     y = random.randint(-290,290)
     food.goto(x,y)
     newSegment = turtle.Turtle()
     newSegment.speed(0)
     newSegment.shape("square")
     newSegment.color('grey')
     newSegment.penup()
     segments.append(newSegment)

    #ove end segment first

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        

    #move segment 0

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    move()
    time.sleep(delay)

window.mainloop()
