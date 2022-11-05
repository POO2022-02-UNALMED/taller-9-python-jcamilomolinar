from tkinter import Tk, Button, Entry, END

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry()

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=0)

#Funcionalidades
def operarNumero():
    operacion = pantalla.get()

    for i in ["+", "-", "*", "/"]:
        if i in operacion: operador = i

    nums = [float(x) for x in operacion.split(operador)]

    if operador == "+":
        resultado = nums[0] + nums[1]
    elif operador == "-":
        resultado = nums[0] - nums[1]
    elif operador == "*":
        resultado = nums[0] * nums[1]
    else:
        resultado = nums[0] / nums[1]
    
    pantalla.delete(0, END)
    pantalla.insert(0, resultado)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", 
        command=lambda: pantalla.insert(END, "1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "9")).grid(row=3, column=2, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",
        command=operarNumero).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,
        command=lambda: pantalla.insert(END, ".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",
        command=lambda: pantalla.insert(END, "/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()