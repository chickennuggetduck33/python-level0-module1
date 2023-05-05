
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(None, prompt="give me name(options: Luke, Wesley, and Sequoya). ")
    if name == "Luke":
        messagebox.showinfo(message="Luke is good at everything.")
    elif name == "Sequoya":
        messagebox.showinfo(message="Sequoya is a sycopath.")
    elif name == "Wesley":
        messagebox.showinfo(message="Wesley is good at Fortnite, but Luke can easily beat him.")
