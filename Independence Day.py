import turtle
#from pygame import mixer

t = turtle.Turtle()

# whenever we are using any function from pygame we need to initialize first
#mixer.init()
#mixer.music.load('song_name.mp3')
#mixer.music.play()
#in my case pygame wasn't working so i just commented those codes

t.pensize(5)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# for ashok chakra
t.color('#050F88')
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
move(0,-80)
t.circle(80,360)    # 80 is the radius and 360 is the complete circle

# green
t.begin_fill()
t.color("green")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

# orange
t.color("orange")
move(-350,80)
t.begin_fill()
t.right(180)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()

turtle.done()
