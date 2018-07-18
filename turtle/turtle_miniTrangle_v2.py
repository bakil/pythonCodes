import turtle
import time

def draw_semiRectangle(temp_t,length):
	for i in [1,2] :
		temp_t.forward(length)
		temp_t.left(45)
		temp_t.forward(length)
		temp_t.left(135)
def draw_flower():
	window = turtle.Screen()
	t = turtle.Turtle()
	t.speed(0)
	t.color("blue")
	SideLen = 50
	time.sleep(10)
	for angle in range(0,360,10):
		t.seth(angle)
		draw_semiRectangle(t,SideLen)
	t.seth(-90)
	t.forward(150)
	window.exitonclick()

draw_flower()

	    



