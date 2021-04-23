'''

Building a simple calculator.

'''

from tkinter import *
#from tkinter import image
expression = ""
# Function to update expression
def press(num):
  global expression
  # concatenation of string
  expression = expression + str(num)
  equation.set(expression)
# Function to evaluate the final expression
def equalpress():
#Try block for exceptions
  try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
#except block
  except:
    equation.set(" error ")
    expression = ""
# Function to clear the contents
def clear():
  global expression
  expression = ""
  equation.set("")
if __name__ == "__main__":
  # create a GUI window
    gui = Tk()
    gui.resizable(width=False, height=False)

    gui.configure(background="#99c2ff")

    # set the title
    gui.title("Simple Calculator")
    gui.geometry("532x465")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, width=40 ,borderwidth= 7)
    expression_field.grid(row=0 , column=0, columnspan=3, padx=10, pady=10)

    # create Buttons
    button1 = Button(gui, text=' 1 ',padx=40, pady=20,
              command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ',padx=40, pady=20,
              command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text=' 3 ',padx=40, pady=20,
              command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text=' 4 ',padx=40, pady=20,
              command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text=' 5 ', padx=40, pady=20,
              command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text=' 6 ', padx=40, pady=20,
              command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text=' 7 ', padx=40, pady=20,
              command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text=' 8 ', padx=40, pady=20,
              command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text=' 9 ', padx=40, pady=20,
              command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
    button0 = Button(gui, text=' 0 ', padx=40, pady=20,
              command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
    button1.grid(row=3, column=0)
    button2.grid(row=3, column=1)
    button3.grid(row=3, column=2)
    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)
    button0.grid(row=4, column=0)
    add = Button(gui, text=' + ', padx=40, pady=20,
            command=lambda: press("+"), height=1, width=7)
    add.grid(row=4, column=1)
    sub = Button(gui, text=' - ', padx=40, pady=20,
            command=lambda: press("-"), height=1, width=7)
    sub.grid(row=4, column=2)
    multiply = Button(gui, text=' * ', padx=40, pady=20,
              command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=5,column=0)
    divide = Button(gui, text=' / ', padx=40, pady=20,
              command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=1)
    equal = Button(gui, text=' = ', padx=40, pady=20,
            command=equalpress, height=1, width=15)
    equal.grid(row=6, column=0, columnspan=4)
    clear = Button(gui, text='Clear', padx=40, pady=20,
            command=clear, height=1, width=7)
    clear.grid(row=5, column=2, columnspan=2)
    gui.mainloop()
    root.iconbitmap('/Users/prashanttimilsena/Downloads/calculator.ico')
    root.mainloop()