import tkinter
from tkinter import *

#seleccion de bancos
def bancos():
    banco = var.get()
    return (banco)

#Cantidad del credito
def cantidad():

    dinero = e_texto.get()
    return (dinero)

#Seleccion tiempo
def cuotar():
    meses = var2.get()
    return (meses)

#calcular cuota
def calcular():
    if bancos() == "Banco Agrario":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.94
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Banco av villas":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.023
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Banco de occidente":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0185
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Bancolombia":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Bancoomeva":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 1.9
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Banco popular":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0135
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "BBVA":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0083
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Caja social":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Colpatria":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0105
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma
    elif bancos() == "Davivienda":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0170
        tasa = total*interes
        cuota = total/cuotas
        suma = '{:,.2f}'.format(round(cuota+tasa))
        return suma

#Suma de cuota
def calcularsuma():
    if bancos() == "Banco Agrario":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.94
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Banco av villas":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.023
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Banco de occidente":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0185
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Bancolombia":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Bancoomeva":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 1.9
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Banco popular":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0135
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "BBVA":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0083
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Caja social":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0128
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Colpatria":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0105
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final
    elif bancos() == "Davivienda":
        total = int(cantidad())
        cuotas = int(cuotar())
        interes= 0.0170
        tasa = total*interes
        cuota = total/cuotas
        suma = cuota+tasa
        final = '{:,.2f}'.format(round(suma*cuotas))
        return final

#Crear segunda pantalla

def Segunda_pestaña():

    self= tkinter.Toplevel(boton4)
    self.title("Calculadora de creditos")
    self.geometry("500x350")
    self.configure(background="#e3fae3")
    inicio = tkinter.Label(self, text= "Resultado", font=("Ink Free",18,'bold'),bg="#cfe4ff")
    inicio.grid(row= 0, column = 65, columnspan=7, padx=8, pady=8)

    texto_tarjeta = Label(self,text= "Tarjeta seleccionada: ",font=("Ink Free",11,'bold'), bg="#cfe4ff")
    texto_tarjeta.grid(row= 1, column= 5, columnspan=4, padx=18, pady=18)

    texto_banco = Label(self, text = "Valor de la cuota es: ",font=("Ink Free",11,'bold'), bg="#cfe4ff")
    texto_banco.grid(row= 2, column= 5, columnspan=4, padx=18, pady=18)
    texto_resultado = Label(self, text = "Valor total a pagar: ",font=("Ink Free",11,'bold'), bg="#cfe4ff")
    texto_resultado.grid(row= 3, column= 5, columnspan=4, padx=18, pady=18)
    signo =Label(self,text="$",font=("Ink Free",11,'bold'), bg="#cfe4ff")
    signo.grid(row=2, column=61,columnspan=4,padx=18,pady=18)
    banco = Label(self, text =bancos(),font=("Ink Free",11,'bold'), bg="#cfe4ff")
    banco.grid(row=1, column=65,columnspan=4,padx=18,pady=18)
    cuota = Label(self, text =calcular(),font=("Ink Free",11,'bold'), bg="#cfe4ff")
    cuota.grid(row=2, column=65,columnspan=4,padx=18,pady=18)
    valor = Label(self, text =calcularsuma(),font=("Ink Free",11,'bold'), bg="#cfe4ff")
    valor.grid(row=3, column=65,columnspan=4,padx=18,pady=18)

    boton_salir = tkinter.Button(self,text="Salir",command=self.destroy)
    boton_salir.grid(row=4, column=65,columnspan=4,padx=18,pady=18)


#Pantalla principal
ventana = Tk()
ventana.title("Calculadora de creditos")
ventana.geometry("650x300")
ventana.configure(background="#e3fae3")

inicio = tkinter.Label(ventana, text= "CALCULAR CREDITO", font=("Ink Free",18,'bold'),bg="#cfe4ff")
inicio.grid(row= 0, column=18,columnspan=7,padx=8,pady=8)
dato1 = tkinter.Label(ventana,text= "Seleccione su tarjerta",font=("Ink Free",11,'bold'), bg="#cfe4ff")
dato1.grid(row=1, column=2,columnspan=4,padx=18,pady=18)

var = tkinter.StringVar(ventana)
var.set('Seleccion')

opciones=['Banco Agrario','Banco av villas', 'Banco de occidente', 'Bancolombia','Bancoomeva' ,'Banco popular', 'BBVA', 'Caja social', 'Colpatria', 'Davivienda']
opciones = tkinter.OptionMenu(ventana,var,*opciones)
opciones.grid(row=1, column=20,columnspan=4,padx=18,pady=18)


dato2 = tkinter.Label(ventana, text= "Valor del credito \n (Sin usar signos de puntuacion)",font=("Ink Free",11,'bold'), bg="#cfe4ff")
dato2.grid(row=2, column=2,columnspan=4,padx=18,pady=18)
e_texto =  Entry(ventana,bg='#fadbff')
e_texto.grid(row= 2, column=20,columnspan=4,padx=18,pady=18)
e_texto.configure(font=("Sf Arch rival", 15))

dato3 = tkinter.Label(ventana, text= "Cantidad de Cuotas",font=("Ink Free",11,'bold'), bg="#cfe4ff")
dato3.grid(row=3, column=2,columnspan=4,padx=18,pady=18)


var2 = tkinter.StringVar(ventana)
var2.set('Seleccion')
porcentajes =['12','24','36','48','60','72']
porcentajes = tkinter.OptionMenu(ventana,var2,*porcentajes)
porcentajes.grid(row= 3, column=20,columnspan=4,padx=18,pady=18)


boton4 = tkinter.Button(ventana,text="Calcular",command=Segunda_pestaña)
boton4.grid(row=1, column=25,columnspan=4,padx=18,pady=18)

boton5 = tkinter.Button(ventana,text="Salir",command=ventana.destroy)
boton5.grid(row=3, column=25,columnspan=4,padx=18,pady=18)

ventana.mainloop()
#------------------------------------------------
