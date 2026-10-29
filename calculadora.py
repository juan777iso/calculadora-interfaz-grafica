import tkinter as tk

ventana = tk.Tk()
ventana.title("calculadora")
ventana.geometry("350x400")
ventana.resizable(False,False)

pantalla=tk.Entry(ventana,font=("Arial", 20), justify=("right"))
pantalla.grid(row=0,columnspan=5)


def agregar_numero(numero):
    pantalla.insert(tk.END,numero)


boton7=tk.Button(ventana,text=7,command=lambda:agregar_numero(7))
boton7.grid(row=1,column=1, ipadx=8, ipady=8,rowspan=1,columnspan=1 )  

boton8=tk.Button(ventana,text=8,command=lambda:agregar_numero(8))
boton8.grid(row=1,column=2,ipadx=8,ipady=8,rowspan=1,columnspan=1)

boton9=tk.Button(ventana,text=9,command=lambda:agregar_numero(9))
boton9.grid(row=1,column=3,ipadx=8,ipady=8,rowspan=1,columnspan=1)

boton4=tk.Button(ventana,text=4,command=lambda:agregar_numero(4))
boton4.grid(row=2,column=1, ipadx=8, ipady=8,rowspan=1,columnspan=1)

boton5=tk.Button(ventana,text=5,command=lambda:agregar_numero(5))
boton5.grid(row=2,column=2, ipadx=8, ipady=8,rowspan=1,columnspan=1)

boton6=tk.Button(ventana,text=6,command=lambda:agregar_numero(6))
boton6.grid(row=2,column=3, ipadx=8, ipady=8,rowspan=1,columnspan=1)

boton1=tk.Button(ventana,text=1,command=lambda:agregar_numero(1))
boton1.grid(row=3,column=1, ipadx=8, ipady=8,rowspan=1,columnspan=1)

boton2=tk.Button(ventana,text=2,command=lambda:agregar_numero(2))
boton2.grid(row=3,column=2, ipadx=8, ipady=8,rowspan=1,columnspan=1)

boton3=tk.Button(ventana,text=3,command=lambda:agregar_numero(3))
boton3.grid(row=3,column=3, ipadx=8, ipady=8,rowspan=1,columnspan=1)

boton0=tk.Button(ventana,text=0,command=lambda:agregar_numero(0))
boton0.grid(row=4,column=1, ipadx=8, ipady=8,rowspan=1,columnspan=1)



def igual():
  try:
    operacion = pantalla.get()

    
    if "++" in operacion or "--" in operacion or "**" in operacion or "//" in operacion or "+-" in operacion:
      raise Exception("error, no es valido escribir dos operadores seguidos")

    resultado = eval(operacion)
    pantalla.delete(0, tk.END)
    pantalla.insert(0, resultado)

  except:
    pantalla.delete(0, tk.END)
    pantalla.insert(0, "Error")



botonigual=tk.Button(ventana,text="=",command=lambda:igual())
botonigual.grid(row=4,column=3, ipadx=8, ipady=8,rowspan=1,columnspan=1)
botonpunto=tk.Button(ventana,text=".", command=lambda:agregar_numero("."))
botonpunto.grid(row=4,column=2, ipadx=8, ipady=8,rowspan=1,columnspan=1)

botonmas=tk.Button(ventana,text="+", command=lambda:agregar_numero("+"))
botonmas.grid(row=1,column=4, ipadx=8, ipady=8,rowspan=1,columnspan=1)
botonmenos=tk.Button(ventana,text="-", command=lambda:agregar_numero("-"))
botonmenos.grid(row=2,column=4, ipadx=8, ipady=8,rowspan=1,columnspan=1)
botondivision=tk.Button(ventana,text="/", command=lambda:agregar_numero("/"))
botondivision.grid(row=3,column=4, ipadx=8, ipady=8,rowspan=1,columnspan=1)
botonmultiplicacion=tk.Button(ventana,text="X", command=lambda:agregar_numero("*"))
botonmultiplicacion.grid(row=4,column=4, ipadx=8, ipady=8,rowspan=1,columnspan=1)

def delete():
  texto_actual = pantalla.get()
  if len(texto_actual) > 0:

   
    nuevo_texto = texto_actual[:-1]
    pantalla.delete(0, tk.END)
    pantalla.insert(0, nuevo_texto)

botonAC=tk.Button(ventana,text="DLT", command=lambda:delete())
botonAC.grid(row=5,column=4, ipadx=8, ipady=8,rowspan=1,columnspan=1)



ventana.mainloop()