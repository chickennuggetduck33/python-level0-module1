from datetime import datetime
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    name = simpledialog.askstring(None, prompt="what is your name?")
    birthyear = simpledialog.askinteger(None, prompt="what year were you born?")
    birthmonth = simpledialog.askinteger(None, prompt="what month were you born?")
    birthday = simpledialog.askinteger(None, prompt="what day were you born?")
    if birthmonth == month:
        if birthday == day:
            messagebox.showinfo(message="HAPPY BURFDUY TU YU, HAPPY BURFDUY TU YU, HAPPY BURFDUY DEAR "+name+" HAPPY BURFDUY TU YU,")
        else:
            messagebox.showinfo(message="suuuuuuuuuuuuuuuuuuuuuuuuiiiiiiiiiiiiiiiiiii")
    else:
        messagebox.showinfo(message="suuuuuuuuuuuuuuuuuuuuuuuuiiiiiiiiiiiiiiiiiii")
