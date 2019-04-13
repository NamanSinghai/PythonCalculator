from tkinter import *
import math
import parser

root_window = Tk()
root_window.resizable(0, 0)
root_window.title("Python Calculator")
operator = ""
text_Input = StringVar()

# Get the input from the user and place it in the text field
input_index = 0
def get_input(variable):
    global input_index
    input_value = len(input_field.get())
    if input_value:
        input_index = input_value
    input_field.insert(input_index, variable)
    input_index += 1

# return the value of input field
def get_value():
    return input_field.get()

# return the square root of the input field
def square_root():
    input_value = float(input_field.get())
    input_value = round(math.sqrt(input_value), 8)
    clear_all()
    input_field.insert(0, input_value)

# Clear the input screen
def clear_all():
    input_field.delete(0, END)

# Remove the last entered value
def backspace():
    input_value = input_field.get()
    if len(input_value):
        input_value = input_value[:-1]
        clear_all()
        input_field.insert(0, input_value)
    else:
        pass

# Return the square of the input value
def square():
    input_value = input_field.get()
    if len(input_value):
        input_value = round(float(input_value)**2, 8)
        clear_all()
        input_field.insert(0, str(input_value))
    else:
        pass

# Return the Reciprocal of the input value
def reciprocal():
    input_value = input_field.get()
    if len(input_value):
        input_value = round(1/float(input_value), 8)
        clear_all()
        input_field.insert(0, str(input_value))
    else:
        pass

def negate():
    input_value = input_field.get()
    if len(input_value):
        input_value = float(input_value) * -1
        clear_all()
        input_field.insert(0, str(input_value))
    else:
        pass

# Return the value for arthematic operations
def calculate():
    input_value = input_field.get()
    try:
        temp_value = parser.expr(input_value).compile()
        result = eval(temp_value)
        clear_all()
        input_field.insert(0, result)
    except Exception:
        clear_all()

# Add input field
input_field = Entry(root_window, bd=15, font=("arial", 30, "bold"), textvariable=text_Input, bg="grey90", justify=LEFT)
input_field.focus_set()
input_field.grid(columnspan=4)

# Add button in Row 1
button_percentage = Button(root_window, bd=1, bg="wheat1", text="%", font=("arial", 20, "bold"))
button_percentage.grid(row=1, column=0, sticky="nsew")
button_root = Button(root_window, bd=1, bg="wheat1", text=u"\u221A", font=("arial", 20, "bold"), command=square_root)
button_root.grid(row=1, column=1, sticky="nsew")
button_nine = Button(root_window, bd=1, bg="wheat1", text="x\u00b2", font=("arial", 20, "bold"), command=square)
button_nine.grid(row=1, column=2, sticky="nsew")
button_multiply = Button(root_window, bd=1, bg="wheat1", text="1/x", font=("arial", 20, "bold"), command=reciprocal)
button_multiply.grid(row=1, column=3, sticky="nsew")

# Add button in Row 2
button_seven = Button(root_window, bd=1, bg="wheat1", text="Pi", font=("arial", 20, "bold"), command=lambda: get_input(math.pi))
button_seven.grid(row=2, column=0, sticky="nsew")
button_eight = Button(root_window, bd=1, bg="wheat1", text="C", font=("arial", 20, "bold"), command=clear_all)
button_eight.grid(row=2, column=1, sticky="nsew")
button_nine = Button(root_window, bd=1, bg="wheat1", text="<", font=("arial", 20, "bold"), command=backspace)
button_nine.grid(row=2, column=2, sticky="nsew")
button_multiply = Button(root_window, bd=1, bg="wheat1", text="/", font=("arial", 20, "bold"), command=lambda: get_input("/"))
button_multiply.grid(row=2, column=3, sticky="nsew")

# Add button in Row 3
button_seven = Button(root_window, bd=1, bg="wheat1", text="7", font=("arial", 20, "bold"), command=lambda: get_input(7))
button_seven.grid(row=3, column=0, sticky="nsew")
button_eight = Button(root_window, bd=1, bg="wheat1", text="8", font=("arial", 20, "bold"), command=lambda: get_input(8))
button_eight.grid(row=3, column=1, sticky="nsew")
button_nine = Button(root_window, bd=1, bg="wheat1", text="9", font=("arial", 20, "bold"), command=lambda: get_input(9))
button_nine.grid(row=3, column=2, sticky="nsew")
button_multiply = Button(root_window, bd=1, bg="wheat1", text="X", font=("arial", 20, "bold"), command=lambda: get_input("*"))
button_multiply.grid(row=3, column=3, sticky="nsew")

# Add button in Row 4
button_four = Button(root_window, bd=1, bg="wheat1", text="4", font=("arial", 20, "bold"), command=lambda: get_input(4))
button_four.grid(row=4, column=0, sticky="nsew")
button_five = Button(root_window, bd=1, bg="wheat1", text="5", font=("arial", 20, "bold"), command=lambda: get_input(5))
button_five.grid(row=4, column=1, sticky="nsew")
button_six = Button(root_window, bd=1, bg="wheat1", text="6", font=("arial", 20, "bold"), command=lambda: get_input(6))
button_six.grid(row=4, column=2, sticky="nsew")
button_minus = Button(root_window, bd=1, bg="wheat1", text="-", font=("arial", 20, "bold"), command=lambda: get_input("-"))
button_minus.grid(row=4, column=3, sticky="nsew")

# Add button in Row 5
button_one = Button(root_window, bd=1, bg="wheat1", text="1", font=("arial", 20, "bold"), command=lambda: get_input(1))
button_one.grid(row=5, column=0, sticky="nsew")
button_two = Button(root_window, bd=1, bg="wheat1", text="2", font=("arial", 20, "bold"), command=lambda: get_input(2))
button_two.grid(row=5, column=1, sticky="nsew")
button_three = Button(root_window, bd=1, bg="wheat1", text="3", font=("arial", 20, "bold"), command=lambda: get_input(3))
button_three.grid(row=5, column=2, sticky="nsew")
button_plus = Button(root_window, bd=1, bg="wheat1", text="+", font=("arial", 20, "bold"), command=lambda: get_input("+"))
button_plus.grid(row=5, column=3, sticky="nsew")

# Add button in Row 6
button_negate = Button(root_window, bd=1, bg="wheat1", text="+/-", font=("arial", 20, "bold italic"), command=negate)
button_negate.grid(row=6, column=0, sticky="nsew")
button_zero = Button(root_window, bd=1, bg="wheat1", text="0", font=("arial", 20, "bold"), command=lambda: get_input(0))
button_zero.grid(row=6, column=1, sticky="nsew")
button_equal = Button(root_window, bd=1, bg="wheat1", text="=", font=("arial", 20, "bold"), command=calculate)
button_equal.grid(row=6, column=2, sticky="nsew")
button_decimal = Button(root_window, bd=1, bg="wheat1", text=".", font=("arial", 20, "bold"))
button_decimal.grid(row=6, column=3, sticky="nsew")

root_window.mainloop()