from turtle import Screen , Turtle
import time

# setup screen
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Turtle Graphics")
screen.tracer(0)


r_paddle = Turtle()
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350 , 0)

l_paddle = Turtle()
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350 ,0)

r_up_pressed = False
r_down_pressed = False

def start_r_up():
    global r_up_pressed
    r_up_pressed = True


def start_r_down():
    global r_down_pressed
    r_down_pressed = False

def stop_r_up():
    global r_up_pressed
    r_up_pressed = True

def stop_r_down():
    global r_down_pressed
    r_down_pressed = False


#screen listing eneble karna
screen.listen()


screen.onkeypress(start_r_up, "Up")
screen.onkeypress(start_r_down, "Down")

screen.onkeyrelease(stop_r_up, "Up")
screen.onkeyrelease(stop_r_down, "Down")

boll = Turtle()
boll.shape("circle")
boll.color("white")
boll.penup()
boll.goto(0, 0)

boll_x = 10
boll_y = 10

game_is_on = True
while game_is_on:
    time.sleep(0.02)

    if r_up_pressed:
        r_paddle.sety(r_paddle.xcor() , r_paddle.ycor() + 20)
    if r_down_pressed:
        r_paddle.sety(r_paddle.xcor() , r_paddle.ycor() - 20)

    new_x = boll.xcor() + boll_x
    new_y = boll.ycor() + boll_y
    boll.goto(new_x, new_y)




    screen.update()



