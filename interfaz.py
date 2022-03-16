import tkinter
from  tkinter import *

#seleccion de bancos

def bancos():
    banco = StringVar()
    banco = var.get()
    return (banco)
def cantidad():
    dinero = float()
    dinero = e_texto.get()
    return (dinero)
def cuotar():
    meses = float()
    meses = var2.get()
    return (meses)
#BANCO AV VILLAS
def calcular():
    if bancos() == "Banco av villas":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.023
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Banco av villas":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.023
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#BANCO DE OCCIDENTE
def calcular():
    if bancos() == "Banco de occidente":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0227
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Banco de occidente":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0227
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#BANCOLOMBIA
def calcular():
    if bancos() == "Bancolombia":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Bancolombia":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#BANCO POPULAR
def calcular():
    if bancos() == "Banco popular":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Banco popular":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#BBVA
def calcular():
    if bancos() == "BBVA":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "BBVA":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#CAJA SOCIAL
def calcular():
    if bancos() == "Caja social":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Caja social":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#COLPATRIA
def calcular():
    if bancos() == "Colpatria":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0105
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Colpatria":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0105
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#DAVIVIENDA
def calcular():
    if bancos() == "Davivienda":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return suma
def calcularsuma():
    if bancos() == "Davivienda":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = suma*cuotas
        return final
#seleccion cantidad de dinero
class NewWindow(Toplevel):

    def __init__(self, master = None):

        super().__init__(master = master)
        self.title("Calculadora de creditos")
        self.geometry("600x300")
        banco = Label(self, text =bancos())
        banco.grid(row=1, column=2,columnspan=4,padx=18,pady=18)
        cuota = Label(self, text =calcular())
        cuota.grid(row=2, column=2,columnspan=4,padx=18,pady=18)
        valor = Label(self, text =calcularsuma())
        valor.grid(row=3, column=2,columnspan=4,padx=18,pady=18)

ventana = Tk()
ventana.title("Calculadora de creditos")
ventana.geometry("600x300")
ventana.configure(background="cyan")

inicio = tkinter.Label(ventana, text= "CALCULAR CREDITO", bg="spring green")
inicio.grid(row= 0, column=18,columnspan=7,padx=8,pady=8)
dato2 = tkinter.Label(ventana,text= "Seleccione su tarjera", bg="spring green")
dato2.grid(row=1, column=2,columnspan=4,padx=18,pady=18)

var = tkinter.StringVar(ventana)
var.set('Seleccion')

opciones=['Banco av villas', 'Banco de occidente', 'Bancolombia', 'Banco popular', 'BBVA', 'Caja social', 'Colpatria', 'Davivienda']
opciones = tkinter.OptionMenu(ventana,var,*opciones)
opciones.grid(row=1, column=20,columnspan=4,padx=18,pady=18)
boton0 = tkinter.Button(ventana,text="Guardar",command=bancos)
boton0.grid(row=1, column=25,columnspan=4,padx=18,pady=18)

dato1 = tkinter.Label(ventana, text= "Valor del credito \n (Sin usar signos de puntuacion)", bg="spring green")
dato1.grid(row=2, column=2,columnspan=4,padx=18,pady=18)
e_texto =  Entry(ventana)
e_texto.grid(row= 2, column=20,columnspan=4,padx=18,pady=18)
e_texto.configure(font=("Times new roman", 15, "italic"))

dato1 = tkinter.Label(ventana, text= "Cantidad de Cuotas", bg="spring green")
dato1.grid(row=3, column=2,columnspan=4,padx=18,pady=18)

boton1 = tkinter.Button(ventana,text="Guardar",command=cantidad)
boton1.grid(row=2, column=25,columnspan=4,padx=18,pady=18)
var2 = tkinter.StringVar(ventana)
var2.set('Seleccion')
porcentajes =['12','24','34','48','60','72']
porcentajes = tkinter.OptionMenu(ventana,var2,*porcentajes)
porcentajes.grid(row= 3, column=20,columnspan=4,padx=18,pady=18)
boton2 = tkinter.Button(ventana,text="Guardar",command=cuotar)
boton2.grid(row=3, column=25,columnspan=4,padx=18,pady=18)

boton4 = tkinter.Button(ventana,text="Calcular",command=NewWindow)
boton4.grid(row=4, column=25,columnspan=4,padx=18,pady=18)

ventana.mainloop()
#------------------------------------------------
