from tkinter import *

root = Tk() #Se crea la raíz llamando a la clase Tk

root.title("Ventana de pruebas") #Cambia el titulo de la ventana
root.resizable(1, 1) #Argumentos: ancho, alto ; Esta función permite bloquear el redimensionado de la ventana (no se puede agrandar ni achicar en caso de (0, 0))
root.iconphoto(1, PhotoImage(file="C:\\Users\\axeld\\Documents\\Python\\interfazgrafica\\mgkshr.png"))
#root.geometry('720x600') Modifica el tamaño por defecto, sin embargo el tamaño hay que darselo al frame, ya que, la raiz siempre se va a adaptar el contenedor interno
root.config(bg='red') #Cambia el color de fondo

frame = Frame(root, width=500, height=400, bg='white') #Se especifíca que el frame va a estar en la raíz

frame.pack(side='left', anchor='n') #Se empaqueta el frame dentro de la raiz, y se acomoda a gusto dentro de ésta, anchor utiliza los puntos cardinales
#frame.pack(fill='x'), (fill='y', expand='True'), (fill='both', expand='True') rellenarán el frame en el eje correspondiente si se dimensiona la ventana
frame.config(bd=35, relief='groove') #Cambia el tamaño y el tipo del borde del frame respectivamente 
frame.config(cursor='hand2') #Cambia el aspecto del cursor cuando pasa sobre el frame

imagen = PhotoImage(file='C:\\Users\\axeld\\Documents\\Python\\interfazgrafica\\tsukuyomi-infinito.png')
Label(frame, image=imagen).place(x=100, y=50)
#Crea un label que permite mostrar un texto o imagen y lo posicióna dentro de la raíz mediante coordenadas dads en píxeles, empaquetandolo en el frame.

#Label(frame, text='Tsukuyomi Infinito', fg='red', font=('Comic Sans MS', 18)).place(x=100, y=150)
#Se crea el texto y se posiciona mediante coordenadas dentro de la raíz, no se empaqueta dentro del frame porque el tamaño de la ventana se adapta al texto

Entry(frame).place(x=150, y=280)

root.mainloop() #Se utiliza el método mainloop porque para que una ventana permanezca abierta debe estar dentro de un bucle infinito