from tkinter import *
root = Tk()

frame = Frame(root, width=720, height=640)
frame.pack()

myName = StringVar()

ename = Entry(frame, textvariable=myName)
ename.grid(row=0, column=1, padx=10, pady=10)
ename.config(justify='left')
elname = Entry(frame)
elname.grid(row=1, column=1, padx=10, pady=10)
elname.config(justify='left')
epass = Entry(frame)
epass.grid(row=2, column=1, padx=10, pady=10)
epass.config(justify='left', show='*')
eaddr = Entry(frame)
eaddr.grid(row=3, column=1, padx=10, pady=10)
eaddr.config(justify='left')
txtcom = Text(frame, width=16, height=5)
txtcom.grid(row=4, column=1, padx=10, pady=10)
scrollv = Scrollbar(frame, command=txtcom.yview)
scrollv.grid(row=4, column=2, sticky='nsew')
txtcom.config(yscrollcommand=scrollv.set)

tx1 = Label(frame, text='Nombre:').grid(row=0, column=0, sticky='w', padx=10, pady=2)
tx2 = Label(frame, text='Apellido:').grid(row=1, column=0, sticky='w', padx=10, pady=2)
tx3 = Label(frame, text='Contraseña:').grid(row=2, column=0, sticky='w', padx=10, pady=2)
tx4 = Label(frame, text='Dirección:').grid(row=3, column=0, sticky='w', padx=10, pady=2)
tx5 = Label(frame, text='Comentarios:').grid(row=4, column=0, sticky='nw', padx=10, pady=2)

def buttonCode():
    myName.set('Axel')

buttonenv = Button(root, text='Enviar', command=buttonCode)
buttonenv.pack()

root.mainloop()