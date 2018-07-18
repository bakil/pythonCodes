import turtle

def draw_trangle(temp_t,length):
	temp_t.begin_fill()
	temp_t.fillcolor("green")
	for i in range(3):
		temp_t.forward(length)
		temp_t.left(120)
	temp_t.end_fill()

def draw_threeTrangle(temp_t,length):
	
	draw_trangle(temp_t,length)
	temp_t.forward(length)
	draw_trangle(t,length)
	temp_t.left(120)
	temp_t.forward(length)
	temp_t.left(-120)
	draw_trangle(t,length)

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.color("blue")
trangleSideLen = 20
for trangle in range(4):
	t.penup()
	t.setposition(0,0)
	t.forward(trangle*2*trangleSideLen)
	t.pendown()
	draw_threeTrangle(t,trangleSideLen)
for trangle in range(3):
	t.penup()
	t.setposition(0,0)
	t.left(60)
	t.forward(trangle*2*trangleSideLen)
	t.left(-60)
	t.pendown()
	draw_threeTrangle(t,trangleSideLen)

for trangle in range(1,4):
	t.penup()
	t.setposition(0,0)
	t.forward(8*trangleSideLen)
	t.left(120)
	t.forward(trangle*2*trangleSideLen)
	t.left(60)
	t.forward(2*trangleSideLen)
	t.left(180)
	t.pendown()
	draw_threeTrangle(t,trangleSideLen)

window.exitonclick()