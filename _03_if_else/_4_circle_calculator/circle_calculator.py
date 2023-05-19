import math
from tkinter import messagebox, simpledialog, Tk
# Write a Python program that asks the user for the radius of a circle.
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    radius = simpledialog.askinteger(title=None, prompt="What is your radius?")
# Next, ask the user if they would like to calculate the area or circumference of a circle.
    whichone = simpledialog.askstring(title=None, prompt="area or circumference?")
# If they choose area, display the area of the circle using the radius.
    if whichone == "area":
        area = math.pi*(radius**2)
        messagebox.showinfo(message="the area is "+str(area)+".")
    elif whichone == "circumfrence":
        circumfrence = math.pi*(radius*2)
        messagebox.showinfo(message="the circumfrence is "+str(circumfrence)+".")
    else:
        messagebox.showinfo(message="THAT WASN'T EVEN AN OPTION!!!!!!!!!")
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 
