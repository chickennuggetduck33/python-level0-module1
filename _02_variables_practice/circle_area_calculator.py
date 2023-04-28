import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    number = simpledialog.askinteger(None, prompt="give me number")
    # Make a new turtle
    bob = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    bob.circle(radius=number)
    # Call the turtle .penup() method
    bob.penup()
    # Move your turtle to a new x,y position using .goto()
    bob.goto(5, 3)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi*(number**2)
    # Write the area of your circle using the turtle .write() method

    bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial',12,'normal'))

    # Hide your turtle
    bob.hideturtle()
    # Call turtle.done()
    turtle.done()
