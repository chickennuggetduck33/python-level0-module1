from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    sum = 0
    minus = 0
    times = 0
    divide = 0
    number1 = simpledialog.askinteger(title=None, prompt="give me a number")
    number2 = simpledialog.askinteger(title=None, prompt="give me another number")
    whichone = simpledialog.askstring(None, prompt="add subtract multiply or divide?")
    if whichone == "add":
        sum = number1 + number2
        messagebox.showinfo(message="your sum is "+str(sum)+".")
    elif whichone == "subtract":
        minus = number1 - number2
        messagebox.showinfo(message="your answer is "+str(minus)+".")
    elif whichone == "multiply":
        times = number1 * number2
        messagebox.showinfo(message="your answer is "+str(times)+".")
    elif whichone == "divide":
        divide = number1 / number2
        messagebox.showinfo(message="your answer is "+str(divide)+".")
    else:
        messagebox.showinfo(message="try again")




"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
