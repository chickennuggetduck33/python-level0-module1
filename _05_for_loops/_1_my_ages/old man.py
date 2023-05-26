from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    age = simpledialog.askinteger(None, prompt="how old are you?")
    for i in range (age):
        messagebox.showinfo(message="you lived through ages "+str(i)+".")
