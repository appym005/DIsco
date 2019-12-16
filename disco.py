import turtle as tt
import random
import time

wm = tt.Screen()
wm.title("Disco Lights")
wm.bgcolor('green')
wm.setup(width = 2000, height = 1024)

wm.tracer(0)
delay = 0.05

colors = ['#0FC0FC', '#7B1DAF', '#FF2FB9', '#D4FF47', '#1B3649' ]

#pen
pen2 = tt.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,400)
pen2.write("Current delay = {} \n Press 'd' to change".format(delay),align = "center", font = ("Courier", 24, "normal"))

#drawer
a1 = 1
a2 = 10
a3 = 10
a4 = 0
paddle_b = tt.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color(colors[random.randint(0,4)])
paddle_b.penup()
paddle_b.goto(0,0)
paddle_b.shapesize(stretch_wid = 5, stretch_len = 5)


shapes = ["circle","square","triangle"]


def change_delay():
	global delay
	delay = wm.numinput("Delay","Give delay in milli-seconds") / 100
	wm.listen()

def end():
	wm.bye()

#keyboard binding
wm.listen()
wm.onkeypress(change_delay,'d')
wm.onkeypress(change_delay,'D')
wm.onkeypress(end,"Escape")

while True:
	wm.update()
	wm.bgcolor(colors[random.randint(0,4)])
	time.sleep(delay)
	pen2.clear()
	pen2.write("Current delay = {}".format(delay),align = "center", font = ("Courier", 24, "normal"))
	
	
	paddle_b.shape(shapes[random.randint(0,2)])
	paddle_b.color(colors[random.randint(0,4)])
	paddle_b.shapetransform(a1, a2, a3,0)
	
	if a2 <= 100:
		a1 += 1
		a2 += 10
		a3 += 10
	else:
		a1 = 1
		a2 = 10
		a3 = 10

