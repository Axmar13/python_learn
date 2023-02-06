from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

op = ''
result = 0

#-----------------------pantalla-----------------------

screennum = StringVar()

screen = Entry(frame, textvariable=screennum)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(bg='black', fg='white', justify='right')

#-----------------------pulsaciones teclado------------

def pulsedNumber(num):
    global op
    if op!='':
        screennum.set(num)
        op = ''
    else:
        screennum.set(screennum.get() + num)

def suma(num):
    global op
    global result
    op = 'suma'
    result += int(num)
    screennum.set(result)

def resta():
    global op
    op = 'resta'

def multiplicacion():
    global op
    op = 'multiplicacion'

def division():
    global op
    op = 'division'

def resultfun():
    global result
    screennum.set(result+int(screennum.get()))
    result = 0

#-----------------------teclas--------- ----------------

boton7 = Button(frame, text='7', width=3, command=lambda:pulsedNumber('7'))
boton7.grid(row=2, column=1)
boton8 = Button(frame, text='8', width=3, command=lambda:pulsedNumber('8'))
boton8.grid(row=2, column=2)
boton9 = Button(frame, text='9', width=3, command=lambda:pulsedNumber('9'))
boton9.grid(row=2, column=3)
botond = Button(frame, text='/', width=3)
botond.grid(row=2, column=4)
boton4 = Button(frame, text='4', width=3, command=lambda:pulsedNumber('4'))
boton4.grid(row=3, column=1)
boton5 = Button(frame, text='5', width=3, command=lambda:pulsedNumber('5'))
boton5.grid(row=3, column=2)
boton6 = Button(frame, text='6', width=3, command=lambda:pulsedNumber('6'))
boton6.grid(row=3, column=3)
botonm = Button(frame, text='x', width=3)
botonm.grid(row=3, column=4)
boton1 = Button(frame, text='1', width=3, command=lambda:pulsedNumber('1'))
boton1.grid(row=4, column=1)
boton2 = Button(frame, text='2', width=3, command=lambda:pulsedNumber('2'))
boton2.grid(row=4, column=2)
boton3 = Button(frame, text='3', width=3, command=lambda:pulsedNumber('3'))
boton3.grid(row=4, column=3)
botonr = Button(frame, text='-', width=3)
botonr.grid(row=4, column=4)
botons = Button(frame, text='0', width=3, command=lambda:pulsedNumber('0'))
botons.grid(row=5, column=1)
botons = Button(frame, text=',', width=3, command=lambda:pulsedNumber(','))
botons.grid(row=5, column=2)
botons = Button(frame, text='=', width=3, command=lambda:resultfun())
botons.grid(row=5, column=3)
botons = Button(frame, text='+', width=3, command=lambda:suma(screennum.get()))
botons.grid(row=5, column=4)



root.mainloop()