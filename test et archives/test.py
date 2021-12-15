import tkinter as tk

root = tk.Tk()

menuBar = tk.Menu(root)
menu1 = tk.Menu(root)
submenu = tk.Menu(root)
submenu.add_radiobutton(label="trace")
submenu.add_radiobutton(label="trace with details")
submenu.add_radiobutton(label="no trace")


menuBar.add_cascade(label="Parameters", menu=menu1)
menu1.add_cascade(label="Trace in terminal", menu=submenu)

root.config(menu=menuBar)
root.mainloop()