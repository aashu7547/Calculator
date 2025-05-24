from tkinter import *
from tkinter.messagebox import *
import math as m

# some useful variables
font = ('Verdana', 20, 'bold')

# important functions
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

def all_clear():
    textField.delete(0, END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            anser = eval(ex)
            textField.delete(0, END)
            textField.insert(0, anser)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)

# creating a window
window = Tk()
window.title('My Calculator')
window.geometry('510x550')

# heading label
heading = Label(window, text='My Calculator', font=font, underline=0)
heading.pack(side=TOP)

# text field
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

# buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='orange',
                   activeforeground='white')
divideBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='<--', font=font, width=11, relief='ridge', activebackground='orange',
                  activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='orange',
                     activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all btns
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textField.bind('<Return>', enterClick)

window.mainloop()