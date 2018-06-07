#Cal
from tkinter import *
import sys, numbers
import cmath, math
e=()
filler=""
def egrab(text):
    text=e.get()
    retrun (text)
def on_changecal(filler):
    args = sys.argv[1:]
    if len(args) < 1:
        expr = text
    else:
        expr = " ".join(args[:])
        expr = expr.replace("[", "(").replace("]", ")")

    def log2(x):
        """Return the base-2 logarithm of x."""
        return cmath.log(x, 2)

    # the smallest number such that 1+eps != 1
    # (this is approximate)
    epsilon = sys.float_info.epsilon

    env = math.__dict__
    env.update(cmath.__dict__)
    for k in [k for k in env if k.startswith("__")]:
        env.pop(k)
    env["eps"] = epsilon
    env["log2"] = log2
    env["inf"] = float("inf")
    env["nan"] = float("nan")

    res = eval(expr, env)

    # throw away small imaginary parts, they're probably just due to imprecision
    if (isinstance(res, numbers.Number)
        and res != 0
        and abs(res.imag)/abs(res) < 10*epsilon):
        res = res.real
    print(str(res).replace("(", "[").replace(")", "]"))
    

root = Tk()
root.title("Cal")
root.geometry("250x122")
root.configure(bg="black")
root.resizable(False, False)

"""root.c=Canvas(root,width=250,height=122)
root.c.config(bg="white",highlightthickness=0)
root.c.place(x = 125, y = 0, anchor = N)
root.rectangle=root.c.create_rectangle(0,122,250,0,fill="white")"""
def Calculator(root):
    content=StringVar()
    e = Entry(root,width=250)
    e.place(x = 10, y = 10, anchor = N)
    e.bind("<Return>",egrabcal)
    e.pack()
Calculator(root)
