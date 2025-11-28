import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,500)
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle= 360/(num_sides)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()

#Triangle
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
board.forward(100)

board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(90)
board.forward(100)

board.right(12)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()


#Rectangle

turtle.Screen().bgcolor("Aquamarine")
board = turtle.Turtle()

board.forward(100)
board.right(90)
board.forward(100)
board.right(90)

board.forward(150)

board.forward(100)
board.right(90)
board.forward(100)
board.right(90)
board.forward(100)
board.right(90)
board.right(90)
board.right(90)
board.right(90)
board.forward(100)


board.penup()
board.right(100)

board.forward(90)
board.right(100)

board.penup()
board.right(100)






turtle.done()

#NEW CODE


secret_number = 10
results ={}

while True:
    guess = int(input("Try and find the number the judge has picked"))
    if guess == secret_number:
        print("You got it.")
    else:
        print("WRONG")

results['final_number'] = secret_number

print(f"You got it! The was {results['final_number']}")



