from tkinter import *

root = Tk()
root.title('checkbuttons')

amaterasu = IntVar()
tsukuyomi = IntVar()
susanoo = IntVar()
kamui = IntVar()
kotoamatsukami = IntVar()
izanami = IntVar()
izanagi = IntVar()

def jutsus():
    opcionEscogida = ''
    if amaterasu.get()==1:
        opcionEscogida += 'Amaterasu '
    if tsukuyomi.get()==1:
        opcionEscogida += 'Tsukuyomi '
    if susanoo.get()==1:
        opcionEscogida += 'Susanoo '
    if kamui.get()==1:
        opcionEscogida += 'Kamui '
    if kotoamatsukami.get()==1:
        opcionEscogida += 'Kotoamatsukami '
    if izanami.get()==1:
        opcionEscogida += 'Izanami '
    if izanagi.get()==1:
        opcionEscogida += 'Izanagi '

    textoFinal.config(text=opcionEscogida)


foto = PhotoImage(file='C:\\Users\\axeld\\Documents\\Python\\interfazgrafica\\mgkshr.png')
Label(root, image=foto).pack()
frame = Frame(root)
frame.pack()
Label(frame, text='¿Que jutsus permite hacer este sharingan?').pack()
Checkbutton(frame, text='Amaterasu', variable=amaterasu, onvalue=1, offvalue=0, command=jutsus).pack()
Checkbutton(frame, text='Tsukuyomi', variable=tsukuyomi, onvalue=1, offvalue=0, command=jutsus).pack()
Checkbutton(frame, text='Susanoo', variable=susanoo, onvalue=1, offvalue=0, command=jutsus).pack()
Checkbutton(frame, text='Kamui', variable=kamui, onvalue=1, offvalue=0, command=jutsus).pack()
Checkbutton(frame, text='Kotoamatsukami', variable=kotoamatsukami, onvalue=1, offvalue=0, command=jutsus).pack()
Checkbutton(frame, text='Izanami', variable=izanami, onvalue=1, offvalue=0, command=jutsus).pack()
Checkbutton(frame, text='Izanagi', variable=izanagi, onvalue=1, offvalue=0, command=jutsus).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()