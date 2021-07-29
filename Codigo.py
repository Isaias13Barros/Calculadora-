from tkinter import *
from math import *
 

def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
 
def clear():
    global operador
    operador=("")
    input_text.set("0")
 
 
calcular=Tk()
calcular.title("CALCULADORA")
calcular.geometry("392x600")
calcular.configure(background="#555555")
color_boton=("#e7e7e7")
 
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
 
Salida=Entry(calcular,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=10,y=60)
 

Button(calcular,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=420)
Button(calcular,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=17,y=360)
Button(calcular,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=107,y=360)
Button(calcular,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=197,y=360)
Button(calcular,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=300)
Button(calcular,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=300)
Button(calcular,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=300)
Button(calcular,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=17,y=240)
Button(calcular,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=107,y=240)
Button(calcular,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=197,y=240)  
Button(calcular,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=197,y=480)
Button(calcular,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=17,y=420)
Button(calcular,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=287,y=360)
Button(calcular,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=287,y=300)
Button(calcular,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=287,y=180)
Button(calcular,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=240)
Button(calcular,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt(")).place(x=197,y=420)
Button(calcular,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
Button(calcular,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
Button(calcular,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=180)
Button(calcular,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log(")).place(x=287,y=480)
Button(calcular,text="AC",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=17,y=180)
Button(calcular,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=107,y=180)
Button(calcular,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=420)
clear()
 
calcular.mainloop()