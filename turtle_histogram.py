import random
import turtle

def random_lowercase():
	list_characters = []
	for i in range(1000):
		lowercase = chr(random.randint(ord("a"), ord("z")))
		list_characters.append(lowercase)
	return list_characters

def count_letters():
	list_count = []
	for letter in range(ord("a"), ord("z") + 1):
		count = random_lowercase().count(chr(letter))
		list_count.append(count)
	return list_count

def print_turtle():
	turtle.shape("turtle")
	turtle.dot(6, "red")

	turtle.penup()
	x = -500
	y = -150
	turtle.goto(x, y)
	turtle.pendown()

	for i in count_letters():
		histogram_length = i * 2
		histogram_breadth = histogram_length // 5

		x += 10
		turtle.setx(x)

		turtle.left(90)
		turtle.forward(histogram_length)
		turtle.right(90)
		turtle.forward(histogram_breadth)
		turtle.right(90)
		turtle.forward(histogram_length)

	turtle.done()



def main():
	print_turtle()
main()