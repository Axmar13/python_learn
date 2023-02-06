from tkinter import *
from tkinter import messagebox

root = Tk()

def ventAcercade():
    messagebox.showinfo('Ventana emergente', 'Ventana emergente de acerca de...')

def ventDocu():
    messagebox.showwarning('Documentación', 'Texto de la documentación')

def ventSalida():
    #salir = messagebox.askquestion('Salir', 'Deseas salir de la aplicación?')
    salir = messagebox.askokcancel('Salir', 'Deseas salir de la aplicación?')
    #if salir=='yes':
    #    root.destroy()
    if salir==True:
        root.destroy()

def ventCerrarDocu():
    cerrar = messagebox.askretrycancel('Reintentar', 'No es posible cerrar. Documento bloqueado')
    if cerrar==False:
        root.destroy()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=500, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Abrir')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Guardar Como')
archivoMenu.add_separator()
archivoMenu.add_command(label='Cerrar', command=ventCerrarDocu)
archivoMenu.add_command(label='Salir', command=ventSalida)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Pegar ')

archivoSeleccion = Menu(barraMenu, tearoff=0)
archivoSeleccion.add_command(label='Seleccionar Todo')

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Documentación', command=ventDocu)
archivoAyuda.add_command(label='Acerca de...', command=ventAcercade)

barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
barraMenu.add_cascade(label='Edición', menu=archivoEdicion)
barraMenu.add_cascade(label='Selección', menu=archivoSeleccion)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)

root.mainloop()