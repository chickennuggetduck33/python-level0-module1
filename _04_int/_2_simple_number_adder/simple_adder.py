from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    number1 = simpledialog.askinteger(title=None, prompt="give me a number")
    number2 = simpledialog.askinteger(title=None, prompt="give me another number")
    sum = 0
    sum = number1 + number2
    messagebox.showinfo(message="your total is "+str(sum)+".")


"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
