import turtle

def draw_square(length):
	
	brad = turtle.Turtle()
	brad.color("blue")
	brad.speed(0)
	i=0
	while i<4 :
		brad.forward(100)
		brad.left(90)
		i+=1


window = turtle.Screen()
window.bgcolor("red")
draw_square(100)


window.exitonclick()