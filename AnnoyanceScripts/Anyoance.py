import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tile import *
import webbrowser



root = tk.Tk()
root.withdraw()
style = ttk.Style(root)
style.theme_use("classic")


root.iconbitmap("toomish_front.ico")
def thebois():
    import random
    list_of_windows = []

    def close_window(tw):
        i = list_of_windows.index(tw)
        list_of_windows[i].destroy()
        del list_of_windows[i]
        if len(list_of_windows) == 0:
            root.destroy()
            print("root destroyed!")

    for i in range(200):

        x = tk.Toplevel(root)
        x.title("BOIS.tom")
        x.geometry(f"230x100+{random.randint(-5, 2080)}+{random.randint(-5, 2080)}")
        x.resizable(False, False)
        ttk.Label(x, text="FRATPARTY").pack()
        ttk.Button(x, text=" OK ", command=lambda tw=x: close_window(tw)).pack(side=tk.BOTTOM)
        x.protocol("WM_DELETE_WINDOW", lambda tw=x: close_window(tw))
        list_of_windows.append(x)
        x.iconbitmap("toomish_front.ico")



for i in range(1):
    computerown = messagebox.askyesno('FREEROBUXGENERATOR.EXE', 'TOOMISHE OWNS YOUR COMPUTER', icon="error")
    print(computerown)



    if computerown == True:

        print("yes")
        messagebox.showinfo("TOOMISHE.TOM", "Ok Then ill Make this my home and Invite THE BOIS")
        time.sleep(1)
        thebois()
        for i in range(5):
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=CIiiMj0B4vA")
    elif computerown == False:
        messagebox.showinfo("TOOMISHE.TOM", "Dosent Matter")
        messagebox.showinfo("TOOMISHE.TOM", "Invite THE BOIS")
        time.sleep(1)
        thebois()
        thebois()
        thebois()
        for i in range(5):
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=CIiiMj0B4vA")










root.mainloop()
