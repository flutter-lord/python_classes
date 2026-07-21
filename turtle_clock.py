import turtle

def draw_clock(radius):
	turtle.shape("turtle")
	turtle.penup()
	turtle.sety(radius)
	turtle.pendown()
	turtle.pensize(15)
	turtle.setheading(180)
	turtle.circle(radius)


def write_number(rad):
	turtle.penup()
	turtle.goto(-10,rad - 40)
	turtle.pendown()
	turtle.write("12", font=("Arial", 20, "bold"))
	for i in range(11, 0, -1):
		turtle.penup()
		turtle.circle(radius= rad - 25, extent=30)
		turtle.pendown()
		turtle.write(i, font= ("Arial", 24, "bold"))

def show_hand(r, color):
	import random
	for i in range(1, 4):
		turtle.penup()
		turtle.home()
		turtle.pendown()
		turtle.dot(15, "red")
		turtle.left(i * (random.randint(50, 120)))
		turtle.pensize(i * 2)
		turtle.color(color)
		turtle.forward(r - 40)


def main():
	r = int(input("Enter the radius of your clock: "))
	c = input("Enter the color of clock\'s hand: ")
	draw_clock(r)
	write_number(r)
	show_hand(r, c)
	turtle.done()

main()