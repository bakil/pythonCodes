import turtle

def draw_square(lenght,angle=0):
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(0)
	brad.seth(angle)
	i=0
	while i<4 :
		brad.forward(lenght)
		brad.left(90)
		i+=1


window = turtle.Screen()
window.bgcolor("red")
len = 100
for i in range(0,360,10):
	draw_square(len , i )
window.exitonclick()