import turtle

def draw_square(i):
	
	brad = turtle.Turtle()
	brad.left(i)
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(10000)
	#brad.speed(1)
	i=0
	while i<4 :
		brad.forward(100)
		brad.left(90)
		i+=1

	

def draw_circle(i):
	brad2 = turtle.Turtle()
	brad2.left(i)
	brad2.shape("turtle")
	brad2.color("blue")
	brad2.speed(20000)
	brad2.circle(100)



def draw_trangle(i):
	tom = turtle.Turtle()
	tom.speed(30000)
	tom.left(i)
	tom.shape("turtle")
	tom.color("blue")
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	tom.left(120)
	

window = turtle.Screen() ## class screen will create screen bord
window.bgcolor("red") ## method to change background color
window.title("my drawing board")
screenWidth = window.window_width()

t = turtle.Turtle() ## creat object from the class Turtle
t.speed(30000)
t.left(i)
t.shape("turtle")
t.color("blue")
t.pencolor("green")
t.width(5) ## width of line
t.forward(100)
t.setposition(100,0)
t.right(120)
t.reset() ## clear screen and return pointer to orginalposition
t.clear() ## clear what was drawn
t.begin_fill() ## to fill the shap before endfill
t.fillcolor("red") ## color to fill
t.end_fill()
t.penup()
t.pendown()
t.stamp() # draw stamp from pointer
t.circle()
t.seth()

window.exitonclick() ## method to close drawing board