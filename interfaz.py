import tkinter
from  tkinter import *

ventana = Tk()
ventana.title("Calculadora de creditos")
ventana.geometry("500x300")
ventana.configure(background="cyan")
inicio = tkinter.Label(ventana, text= "CALCULAR CREDITO", bg="spring green")
inicio.grid(row= 0, column=18,columnspan=7,padx=8,pady=8)
dato2 = tkinter.Label(ventana,text= "Seleccione su tarjera", bg="spring green")
dato2.grid(row=1, column=2,columnspan=4,padx=18,pady=18)
var = tkinter.StringVar(ventana)
var.set('Seleccion')
opciones=['falabella','bbva','codensa','av villas','banco popular','davivienda']
opciones = tkinter.OptionMenu(ventana,var,*opciones)
opciones.grid(row=1, column=20,columnspan=4,padx=18,pady=18)
dato1 = tkinter.Label(ventana, text= "Valor del credito", bg="spring green")
dato1.grid(row=2, column=2,columnspan=4,padx=18,pady=18)
e_texto =  Entry(ventana)
e_texto.grid(row= 2, column=20,columnspan=4,padx=18,pady=18)
e_texto.configure(font=("Times new roman", 15, "italic"))
dato1 = tkinter.Label(ventana, text= "Cantidad de Cuotas", bg="spring green")
dato1.grid(row=3, column=2,columnspan=4,padx=18,pady=18)
boton1 = tkinter.Button(ventana,text="Guardar")
boton1.grid(row=2, column=25,columnspan=4,padx=18,pady=18)
e_texto =  Entry(ventana)
e_texto.grid(row= 3, column=20,columnspan=4,padx=18,pady=18)
e_texto.configure(font=("Times new roman", 15, "italic"))
boton2 = tkinter.Button(ventana,text="Guardar")
boton2.grid(row=3, column=25,columnspan=4,padx=18,pady=18)



hola mundo






ventana.mainloop()
#------------------------------------------------
