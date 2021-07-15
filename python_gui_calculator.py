# GUI Calculator with tkinter :
# starter code
# importing required libraries
import tkinter as tk 
from tkinter import StringVar, ttk


# creating tkinter window with name win:
win = tk.Tk()                        
win.title('Calculator')
win.minsize(width=380, height=195)
win.maxsize(width=380, height=195)


# creating entry box : to take input and display the output
expression = ""
equation = StringVar()
input_entrybox = tk.Entry(win,width=50 ,textvariable = equation)
input_entrybox.grid(row=0, column=1, columnspan=4, rowspan=2)
input_entrybox.focus()


# creating variable for special memory : Like Accumulator Register
memory_expression = ""
memory_status_indicator = ""         # to indicate the status of our Memory/Accumulator Register
memory_equation = StringVar()
memory_window = tk.Entry(win, width=10,textvariable=memory_equation)
memory_window.grid(row=0, column=0,columnspan=1, rowspan=2)


# press function to add corresponding numbers and operators to the input field
def press(num):
    global expression
    expression = str(expression)
    expression += str(num)
    equation.set(expression)


# defining an action function which perform the actual caluculation task
def action():                

    # try and except blocks to catch and resolve the errors
    try:
        global expression
        userinput = equation.get()
        Ans = eval(userinput)
        equation.set(Ans)
        # this will automatically cleared the input field
        expression = ""
    
    except ZeroDivisionError:
        equation.set("Divide by zero!")
        expression =""

    except :
        equation.set("Please Enter Any Number First!")
        expression = ""


def clearAll():
	global expression
	expression = ""
	equation.set("")


def clear():
    global expression
    new_expression = list(expression)
    new_expression.pop()
    expression = "".join(new_expression)
    equation.set(expression)


def AddDoubleZero():
    global expression
    expression = expression + "00"
    equation.set(expression)


def squareroot():
        try:
            global expression
            new_expression = float(expression)
            expression = new_expression ** (1/2)
            equation.set(str(expression))
        except :
            equation.set("Please Enter Any Number First!")
            expression = ""


def cuberoot_new():
    try:
        global expression
        new_expression = float(expression)
        expression = new_expression ** (1/3)
        equation.set(str(expression))
    except :
        equation.set("Please Enter Any Number First!")
        expression = ""


def recipro():
    try:
        global expression
        new_expression = float(expression)
        expression = 1/(new_expression)
        equation.set(expression)
    except: 
        equation.set("Please don't press '=' sign before clicking on 1/x button")
        expression = ""


def my_squre():
    try:
        global expression
        new_expression = float(expression)
        expression = new_expression ** 2
        equation.set(expression)
    except :
        equation.set("Please Enter Any Number First!")
        expression = ""


def my_cube():
    try:
        global expression
        new_expression = float(expression)
        expression = new_expression ** 3
        equation.set(expression)
    except :
        equation.set("Please Enter Any Number First!")
        expression = ""


def facto():
    try:
        global expression
        new_expression = float(expression)
        
        if new_expression < 0:
            expression = "0"
            equation.set(expression)
        elif new_expression == 0 or new_expression == 1:
            expression = "1"
            equation.set(expression)
        else:
            fact = 1
            while(new_expression > 1):
                fact *= new_expression
                new_expression -= 1
            expression = fact
            equation.set(expression)    

    except :
        equation.set("Please Enter Any Number First!")
        expression = ""


def power_of_tenth():
    try:
        global expression
        new_expression = float(expression)
        expression = 10 ** new_expression
        equation.set(expression)
    except :
        equation.set("Please Enter Any Number First!")
        expression = ""


# special memory related functions :
def MemoryStore():
    global memory_expression
    global expression
    global memory_status_indicator
    memory_expression = expression
    expression = ""
    memory_status_indicator = "M"
    equation.set(expression)
    memory_equation.set(memory_status_indicator)

def MemoryRecall():
    global memory_expression
    global expression
    expression = memory_expression
    equation.set(expression)

def MemoryClear():
    global memory_expression
    global expression
    global memory_status_indicator
    memory_expression = ""
    expression = ""
    memory_status_indicator = ""
    memory_equation.set(memory_status_indicator)
    equation.set(expression)

def MemoryAdd():
    global memory_expression
    global expression
    expression =  int(memory_expression) + int(expression) 
    equation.set(expression)

def MemorySub():
    global memory_expression
    global expression
    expression = int(memory_expression) - int(expression)
    equation.set(expression)


# Creating Buttons :
ButtonMC = ttk.Button(win, text = 'MC', command= MemoryClear)
ButtonMC.grid(row=2, column=0) 

ButtonMR = ttk.Button(win, text = 'MR', command= MemoryRecall)
ButtonMR.grid(row=2, column=1) 

ButtonMS = ttk.Button(win, text = 'MS', command= MemoryStore)
ButtonMS.grid(row=2, column=2) 

ButtonMPlus = ttk.Button(win, text = 'M+', command= MemoryAdd)
ButtonMPlus.grid(row=2, column=3) 

ButtonMMinus = ttk.Button(win, text = 'M-', command= MemorySub)
ButtonMMinus.grid(row=2, column=4) 

Button4 = ttk.Button(win, text = '(', command= lambda : press("("))
Button4.grid(row=3, column=0)    

Button5 = ttk.Button(win, text = ')', command= lambda : press(")"))
Button5.grid(row=3, column=1) 

ButtonClear = ttk.Button(win, text = 'Clear', command=clear)
ButtonClear.grid(row=3, column=2)

ButtonClear = ttk.Button(win, text = 'AC', command=clearAll)
ButtonClear.grid(row=3, column=3) 

ButtonRecipro = ttk.Button(win, text = '1/x', command=recipro)
ButtonRecipro.grid(row=3, column=4)

Button1 = ttk.Button(win, text = '7', command= lambda : press(7))
Button1.grid(row=4, column=0) 

Button2 = ttk.Button(win, text = '8', command= lambda : press(8))
Button2.grid(row=4, column=1) 

Button3 = ttk.Button(win, text = '9', command= lambda : press(9))
Button3.grid(row=4, column=2) 

Button2Plus = ttk.Button(win, text = '/', command= lambda : press("/"))
Button2Plus.grid(row=4, column=3) 

ButtonModulus = ttk.Button(win, text = '%', command= lambda : press("%"))
ButtonModulus.grid(row=4, column=4) 

Button4 = ttk.Button(win, text = '4', command= lambda : press(4))
Button4.grid(row=5, column=0)    

Button5 = ttk.Button(win, text = '5', command= lambda : press(5))
Button5.grid(row=5, column=1) 

Button6 = ttk.Button(win, text = '6', command= lambda : press(6))
Button6.grid(row=5, column=2) 

ButtonMinus = ttk.Button(win, text = '*', command= lambda : press("*"))
ButtonMinus.grid(row=5, column=3) 

ButtonSqroot = ttk.Button(win, text = '√2', command=squareroot)
ButtonSqroot.grid(row=5, column=4) 

Button7 = ttk.Button(win, text = '1', command= lambda : press(1))
Button7.grid(row=6, column=0)    

Button8 = ttk.Button(win, text = '2', command= lambda : press(2))
Button8.grid(row=6, column=1) 

Button9 = ttk.Button(win, text = '3', command= lambda : press(3))
Button9.grid(row=6, column=2) 

ButtonMulti = ttk.Button(win, text = '-', command= lambda : press("-"))
ButtonMulti.grid(row=6, column=3) 

ButtonMulti = ttk.Button(win, text = '√3', command= cuberoot_new)
ButtonMulti.grid(row=6, column=4) 

Button0 = ttk.Button(win, text = '0', command= lambda : press(0))
Button0.grid(row=7, column=0)    

ButtonClear = ttk.Button(win, text = '00', command=AddDoubleZero)
ButtonClear.grid(row=7, column=1) 

ButtonDot = ttk.Button(win, text = '.', command= lambda : press("."))
ButtonDot.grid(row=7, column=2) 

ButtonDiv = ttk.Button(win, text = '+', command= lambda : press("+"))
ButtonDiv.grid(row=7, column=3) 

ButtonORB = ttk.Button(win, text = 'x^2', command= my_squre)
ButtonORB.grid(row=8, column=0) 

ButtonCRB = ttk.Button(win, text = 'x^3', command= my_cube)
ButtonCRB.grid(row=8, column=1) 

Buttonpoweroften = ttk.Button(win, text = '10^x', command=power_of_tenth)
Buttonpoweroften.grid(row=8, column=2)

Buttonfacto = ttk.Button(win, text = 'x!', command=facto)
Buttonfacto.grid(row=8, column=3) 

ButtonEquals = ttk.Button(win, text = '=', command=action)
ButtonEquals.grid(row=7, column=4, rowspan=2, ipady=13,sticky = tk.W) 

# to run the Tkinter event loop, untill the window is not open/not closed
win.mainloop()                       



