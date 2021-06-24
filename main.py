from tkinter import *

calc = Tk()
calc.title("CERY CALCULATOR v.1.0.0")
calc.resizable(width=False, height=False)
CalcFrame = Frame(calc, bd=5, pady=2, relief=RIDGE).grid()


class Calc:
    def __init__(self):
        self.total = 0
        self.current = 0
        self.input = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def InputValue(self, num):
        self.result = False
        num1 = OutputTray.get()
        num2 = str(num)
        if self.input:
            self.current = num2
            self.input = False
        else:
            if num2 == '.':
                if num2 in num1:
                    return
            self.current = num1 + num2
        self.display(self.current)

    def display(self, value):
        OutputTray.delete(0, END)
        OutputTray.insert(0, value)

    def overalltotal(self):
        self.result = True
        try:
            self.current = float(self.current)
            if self.check_sum == True:
                self.validFunction()
            else:
                self.total = float(OutputTray.get())
        except:
            self.Clear()
            self.display(0)

    def validFunction(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'subtract':
            self.total -= self.current
        if self.op == 'multiply':
            self.total *= self.current
        if self.op == 'divide':
            self.total /= self.current
        self.input = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.validFunction()
        elif not self.result:
            self.total = self.current
            self.input = True
        self.check_sum = True
        self.op = op
        self.result = False

    def dlt(self):
        nmbrs = len(OutputTray.get())
        OutputTray.delete(nmbrs - 1, 'end')
        if nmbrs == 1:
            OutputTray.insert(0, '0')

    def Clear(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input = True

    def ClearAll(self):
        self.Clear()
        self.total = 0


pressedBtn = Calc()
OutputTray = Entry(CalcFrame, font=('century gothic', 32, 'bold'), bg='light yellow', bd=15, width=17, justify='right')
OutputTray.grid(row=0, column=0, columnspan=4, pady=1)
OutputTray.insert(0, '0')

# numbers
numpad = '789456123'
x = 0
nb = []
for y in range(3, 6):
    for z in range(3):
        nb.append(Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10,
                         text=numpad[x]))
        nb[x].grid(row=y, column=z, pady=1)
        nb[x]['command'] = lambda i=numpad[x]: pressedBtn.InputValue(i)
        x += 1

n0 = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='0',
            command=lambda: pressedBtn.InputValue(0)).grid(row=6, column=1, pady=1)

DotBtn = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='.',
                command=lambda: pressedBtn.InputValue('.')).grid(row=6, column=0, pady=1)

# Functions
EqlsBtn = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='cyan', bd=10, text='=',
                 command=pressedBtn.overalltotal).grid(row=6, column=2, pady=1)

CLearAllBtn = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='black', fg='white', bd=10,
                     text='CE', command=pressedBtn.ClearAll).grid(row=1, column=0, pady=1)

ClearBtn = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bd=10, text='C',
                  command=pressedBtn.Clear).grid(row=1, column=1, pady=1)

DelBtn = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='yellow', bd=10, text='',
                command=pressedBtn.dlt).grid(row=1, column=2, pady=1)

# Operands
divide = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='green', fg='white', bd=10,
                text='/', command=lambda: pressedBtn.operation('divide')).grid(row=1, column=3, pady=1)

multiply = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='green', fg='white', bd=10,
                  text='x', command=lambda: pressedBtn.operation('multiply')).grid(row=3, column=3, pady=1)

minus = Button(CalcFrame, width=4, height=1, font=('century gothic', 24, 'bold'), bg='green', fg='white', bd=10,
               text='-', command=lambda: pressedBtn.operation('subtract')).grid(row=4, column=3, pady=1)

plus = Button(CalcFrame, width=4, height=3, font=('century gothic', 24, 'bold'), bg='red', fg='white', bd=10, text='+',
              command=lambda: pressedBtn.operation('add')).grid(row=5, column=3, rowspan=2, pady=1)

calc.mainloop()