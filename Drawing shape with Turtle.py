#imports the turtle setup
import turtle

#asks for the number of sides from the user
numSides = int(input("How many sides would you like? "))

#asks for the length of the sides from the user
sideLength = int(input("How big would you like the sides to be? "))

#asks for the users color
usersColor = input("What color do you want the outside to be? ")

#asks for the color for the inside of the shape
fillColor = input("What color do you want the shape to be filled with? ")

#sets up the angle for the sides
angleOfShape = 360/numSides

#sets up the turtle
usersTurtle = turtle.Turtle()

#gives the turtle the outline color
usersTurtle.color(usersColor,fillColor)

#starts to fill in the color
usersTurtle.begin_fill()

#sets up the for loop to draw the shape
for x in range(numSides):
    usersTurtle.forward(sideLength)
    usersTurtle.left(angleOfShape)

#finishes to fill in the color
usersTurtle.end_fill()
