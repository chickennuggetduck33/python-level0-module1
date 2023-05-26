"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

from tkinter import *
import tkinter as tk

root = tk.Tk()
x = 100
y = 45

canvas = tk.Canvas(root, width=200, height=200, bg="#FF00FF");
canvas.grid()
for i in range(4):

    if i >=3:
        canvas.create_text(x, y, text="banana", font=("Arial", 16))

    else:
        canvas.create_text(x, y, text="ice cream", font=("Arial", 16))
    y = y + 45
'''
Text Rendering Example:
                    x    y                                                       

'''
# Put your code below


root.mainloop()
