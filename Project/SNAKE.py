# SNAKE GAME
# BRETT TIERNEY
import turtle
import time
import random

screenChangex =100
screenChangey =100
delay = 0.1
speed = 15
#Set Up screen
window =turtle.Screen()
window.title("Snake Game by BRETT TIERNEY")
window.bgcolor("green")
window.setup(width=600, height=600, startx=screenChangex, starty =screenChangey)
window.tracer(0)

#import image for food and poison and snake
foodImage = "manzana_.gif"
poisonImage = "radiation.gif"
snakeHEADUP = "snakeup.gif"
snakeHEADDOWN = "snakedown.gif"
snakeHEADLEFT = "snakeLeft.gif"
snakeHEADRight = "snakeright.gif"
snakeSIDE = "snakeside.gif"
snakeVERT = "snakeTOPBOTTOM.gif"
window.addshape(foodImage)
window.addshape(poisonImage)
window.addshape(snakeHEADUP)
window.addshape(snakeHEADDOWN)
window.addshape(snakeHEADLEFT)
window.addshape(snakeHEADRight)
window.addshape(snakeSIDE)
window.addshape(snakeVERT)



#SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape(snakeHEADUP)
head.penup()
head.goto(0,0)
head.direction = "right"



#FOOD
food = turtle.Turtle()
food.speed(0)
#make food turtle apple image

food.shape(foodImage)
food.penup()
food.goto(0,0)

#POISON
#Poison is a new adition that ends game when contacted
poison = turtle.Turtle()
poison.speed(0)
poison.shape(poisonImage)
poison.penup()
poison.goto(100,100)
 
#body
segments = []

#Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)
        head.shape(snakeHEADUP)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)
        head.shape(snakeHEADDOWN)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)
        head.shape(snakeHEADLEFT)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)  
        head.shape(snakeHEADRight)              

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
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "up"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()


    #check for food eat
    if head.distance(food)<20:
     # move food to random spot
     x = random.randint(-280,280)
     y = random.randint(-280,280)
     food.goto(x,y)
     newSegment = turtle.Turtle()
     newSegment.speed(0)
     newSegment.shape(snakeSIDE)
     newSegment.penup()
     segments.append(newSegment)
     screenChangex = 500
     screenChangey = 500
     # move poison to random spot
     x = random.randint(-280,280)
     y = random.randint(-280,280)
     poison.goto(x,y)
     # increase speed
     speed = speed + 1

    #check for poison eat NEW ADDITION
    if head.distance(poison)<20:
        turtle.Screen().bye()
        print("You ate the Poison, YOU LOSE!")
        
    #move end segment first

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
