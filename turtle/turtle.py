import turtle

def draw_square(lenght):
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(0)
	i=0
	while i<4 :
		brad.forward(lenght)
		brad.left(90)
		i+=1

	

def draw_circle(radius):
	brad2 = turtle.Turtle()
	brad2.color("blue")
	brad2.circle(radius)



def draw_trangle(length):
	tom = turtle.Turtle()
	tom.color("blue")
	tom.forward(length)
	tom.left(120)
	tom.forward(length)
	tom.left(120)
	tom.forward(length)
	tom.left(120)
	

window = turtle.Screen()
window.bgcolor("red")
len = 100
draw_square(len)
draw_circle(len)
draw_trangle(len)


window.exitonclick()