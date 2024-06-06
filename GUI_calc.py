# Python's GUI Library 
from tkinter import *
from tkinter import ttk
import tkinter as tk


#Code for creating the GUI, This is where the buttons and the Screen will be placed
mainwindow = Tk()
mainwindow.title("GUI Calculator")
mainwindow.geometry("302x260")


# This Function handles button press events, It basically updates a text label on the GUI
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)



def equal():
    try:
         global equation_text
         total = str(eval(equation_text))
         equation_label.set(total)
         equation_text = total

#added an exception handle to prevent the program from crashing when a user divides a number by zero
    except ZeroDivisionError:
         equation_label.set("You can't divide by Zero Bud")
         equation_text = ''




def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

equation_text = ""
equation_label = StringVar()




frame = Frame(mainwindow)
screen = Label(mainwindow, textvariable = equation_label, font=('Arial', 14), bg = 'white', height=2, width=35)
screen.pack()


frame = Frame(mainwindow)
frame.pack()

#Code for Styling the Buttons
style = ttk.Style().configure("TButton", foreground="black", font=("Arial",14), padding=6 , relief="GROOVE", background="#ccc", width=5, height=5)

#buttons first row
Num6 = ttk.Button(frame, text = "7", command= lambda : button_press(7), style="TButton").grid(column = 0, row = 0, padx=0,pady=0) 
Num7 = ttk.Button(frame, text = "8", command= lambda : button_press(8), style="TButton").grid(column = 1, row = 0, padx=0,pady=0) 
Num8 = ttk.Button(frame, text = "9", command= lambda : button_press(9), style="TButton").grid(column = 2, row = 0, padx=0,pady=0) 
add = ttk.Button(frame, text = "+", command= lambda : button_press('+'), style="TButton").grid(column = 3, row = 0, padx=0,pady=0) 


#buttons Second row
Num4 = ttk.Button(frame, text = "4", command= lambda : button_press(4), style="TButton").grid(column = 0, row = 1, padx=0,pady=0) 
Num5 = ttk.Button(frame, text = "5", command= lambda : button_press(5), style="TButton").grid(column = 1, row = 1, padx=0,pady=0) 
Num6 = ttk.Button(frame, text = "6", command= lambda : button_press(6), style="TButton").grid(column = 2, row = 1, padx=0,pady=0) 
Subtract = ttk.Button(frame, text = "-", command= lambda : button_press('-'), style="TButton").grid(column = 3, row = 1, padx=0,pady=0) 

#buttons third row
Num1 = ttk.Button(frame, text = "1", command= lambda : button_press(1), style="TButton").grid(column = 0, row = 2, padx=0,pady=0) 
Num2 = ttk.Button(frame, text = "2", command= lambda : button_press(2), style="TButton").grid(column = 1, row = 2, padx=0,pady=0) 
Num3 = ttk.Button(frame, text = "3", command= lambda : button_press(3), style="TButton").grid(column = 2, row = 2, padx=0,pady=0) 
multiply = ttk.Button(frame, text = "X", command= lambda : button_press('*'), style="TButton").grid(column = 3, row = 2, padx=0,pady=0) 

#buttons fourth row (The last row)
Num10 = ttk.Button(frame, text = "0", command= lambda : button_press(0), style="TButton").grid(column = 0, row = 3, padx=0,pady=0) 
Num14 = ttk.Button(frame, text = ".", command= lambda : button_press('.'), style="TButton").grid(column = 1, row = 3, padx=0,pady=0) 
divide = ttk.Button(frame, text = "/", command= lambda : button_press('/'), style="TButton").grid(column = 2, row = 3, padx=0,pady=0) 
clean = ttk.Button(frame, text = "Clear", command= clear, style="TButton").grid(column = 3, row = 3, padx=0,pady=0)
equals = ttk.Button(frame, text = "=", command= equal, style="TButton").grid(column = 3, row = 4, padx=0,pady=0) 


mainwindow.mainloop() 