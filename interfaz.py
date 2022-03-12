import textwrap
import tkinter
from  tkinter import *

ventana = Tk()
ventana.title("Calculadora de creditos")
ventana.geometry("500x300")
inicio = tkinter.Label(ventana, text= "CALCULAR CREDITO")
inicio.grid(row= 0, column=0,columnspan=7,padx=8,pady=8)
dato1 = tkinter.Label(ventana, text= "Valor del credito")
dato1.grid(row=1, column=2,columnspan=4,padx=18,pady=18)
e_texto =  Entry(ventana)
e_texto.grid(row= 1, column=20,columnspan=4,padx=18,pady=18)
e_texto.configure(font=("Times new roman", 15, "italic"))







ventana.mainloop()
#------------------------------------------------