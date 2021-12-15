import math
import tkinter as tk
from tkinter import ttk
import rules

values_chaining = ["Backward chaining", "Forward chaining (in deepth)", 'Forward chaining (in width)']
title = "Geometric shape recognition"
chaining_type = "type of chaining:"
goal = "goal :"
forms = ["nothing", "point", "trait", "square", "rectangle", 'triangle', "parallelogram", "equilateral triangle",
         "isosceles triangle", "rectangle triangle","quadrilateral"]
inf = "Start inference"
number_point = "number of point:"


def angle_between(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return (360 + ang if ang < 0 else ang) % 180


class Form(object):
    error_margin = 10

    def __init__(self):
        self.points = []
        self.sides = []
        self.angles = []
        self.close = False
        self.line_close = False

    def add_point(self, couple):
        if not self.close:
            x = couple[0]
            y = couple[1]
            for point in self.points:
                if x - Form.error_margin <= point[0] <= x + Form.error_margin:
                    if y - Form.error_margin <= point[1] <= y + Form.error_margin:
                        couple = (point[0], point[1])
                        self.close = True

            if self.close:
                if len(self.points) >= 3:
                    self.angles.append(angle_between(self.points[-2], self.points[-1], self.points[0]))
                    self.angles.append(angle_between(self.points[-1], self.points[0], self.points[1]))
                if len(self.points) >= 2:
                    self.sides.append(math.sqrt(
                        (self.points[-1][0] - self.points[0][0]) ** 2 + (self.points[-1][1] - self.points[0][1]) ** 2))
                return False
            else:
                self.points.append(couple)
                if len(self.points) >= 3:
                    self.angles.append(angle_between(self.points[-3], self.points[-2], self.points[-1]))
                if len(self.points) >= 2:
                    self.sides.append(math.sqrt((self.points[-1][0] - self.points[-2][0]) ** 2 + (
                            self.points[-1][1] - self.points[-2][1]) ** 2))

            return True
        return False

    def last_line(self):
        if len(self.points) >= 2 and not self.line_close:
            if self.close:
                self.line_close = True
                return self.points[-1], self.points[0]
            return self.points[-1], self.points[-2]
        else:
            return None, None

    def clear(self):
        self.points.clear()
        self.angles.clear()
        self.sides.clear()
        self.close = False
        self.line_close = False

    def to_facts(self):
        return {"sides": self.sides, "angles": self.angles, "points": self.points}


def painting_forms(event):
    if FORM.close:
        FORM.clear()
        canvas.delete("all")
    x = event.x
    y = event.y
    r = 5
    add = FORM.add_point((x, y))
    if add:
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="blue")
        label_nb_point.config(text=number_point+str(len(FORM.points)))
    p1, p2 = FORM.last_line()
    if p1 is not None and p2 is not None:
        canvas.create_line(p1[0], p1[1], p2[0], p2[1], width=2, fill="red")


def chaining_selection(event):
    global combo_box_forms, combo_box, button

    if combo_box.get() != values_chaining[0]:
        combo_box_forms.config(state="disabled")
    else:
        combo_box_forms.config(state="normal")


def execute():
    resp = ""
    if combo_box.get() == values_chaining[0]:
        resp = str(rules.RULES.backward_chaining([
            lambda var: var[combo_box_forms.get()]
        ], FORM.to_facts(), trace=trace, details=details))
    if combo_box.get() == values_chaining[1]:
        resp = str(rules.RULES.foward_chaining_deepth(FORM.to_facts(), trace=trace, details=details))
    if combo_box.get() == values_chaining[2]:
        resp = str(rules.RULES.forward_chaining_width(FORM.to_facts(), trace=trace, details=details))

    entry.delete(0, "end")
    entry.insert(0, resp)


# variables
FORM = Form()
trace = False
details = False

root = tk.Tk(className=title)
root.geometry("800x500")

# canvas for draw
label_nb_point = tk.Label(root, text=number_point + "0")
label_nb_point.pack(side=tk.TOP, anchor=tk.N)
canvas = tk.Canvas(root, background="grey")
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
canvas.bind("<Button-1>", painting_forms)

# entry for display result
entries_frame = tk.Frame(root)
entries_frame.pack(side=tk.TOP, fill=tk.X, pady=15, padx=10)
entry = tk.Entry(entries_frame, width=100)
entry.insert(0, "")
entry.pack(side=tk.TOP, pady=10)

# select chaining type
label_type = tk.Label(entries_frame, text=chaining_type)
label_type.pack(side=tk.LEFT)
combo_box = ttk.Combobox(entries_frame, values=values_chaining, width=25)
combo_box.bind("<<ComboboxSelected>>", chaining_selection)
combo_box.set(value=values_chaining[0])
# select goal
combo_box.pack(side=tk.LEFT, padx=(0, 10))
label_goal = tk.Label(entries_frame, text=goal)
label_goal.pack(side=tk.LEFT)
combo_box_forms = ttk.Combobox(entries_frame, values=forms, width=25)
combo_box_forms.pack(side=tk.LEFT)
combo_box_forms.set(value=forms[0])



# menu
def option_trace():
    global trace, details
    trace = True
    details = False
    return trace and details


def option_trace_with_details():
    global trace, details
    trace = True
    details = True
    return trace and details


def option_no_trace():
    global trace, details
    trace = False
    details = False
    return trace and details


menuBar = tk.Menu(root)
menu1 = tk.Menu(root)
submenu = tk.Menu(root)
submenu.add_radiobutton(label="trace", command=option_trace)
submenu.add_radiobutton(label="trace with details", command=option_trace_with_details)
submenu.add_radiobutton(label="no trace", command=option_no_trace)

menuBar.add_cascade(label="Parameters", menu=menu1)
menu1.add_cascade(label="Trace in terminal", menu=submenu)

root.config(menu=menuBar)

button = tk.Button(entries_frame, text=inf, command=execute)
button.pack(side=tk.LEFT, padx=10)

root.mainloop()
