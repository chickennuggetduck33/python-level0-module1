from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    egg = simpledialog.askstring(None, prompt="what is more useful when it is broken?")
    hole = simpledialog.askstring(None, prompt="The more you take away from we the bigger I get.  What am I?")
    name = simpledialog.askstring(None, prompt="What belongs to you but other people use it more than you?")
    if egg == "egg":
        score = score +1
    elif egg == "an egg":
        score = score + 1
    elif egg == "the egg":
        score = score + 1
    elif egg == "a egg":
        score = score + 1
    if hole == "hole":
        score = score + 1
    elif hole == "a hole":
        score = score + 1
    elif hole == "the hole":
        score = score + 1
    if name == "name":
        score = score + 1
    elif name == "a name":
        score = score + 1
    elif name == "your name":
        score = score + 1

    messagebox.showinfo(message="your score is "+str(score)+" out of 3.")

"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
