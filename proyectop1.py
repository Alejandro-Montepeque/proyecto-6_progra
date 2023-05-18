from tkinter import *
pantalla_raiz=Tk()
#Ventana Index de la pnatalla de inicio
pantalla_raiz.title("Bienvenido al Banco del Caribe")
pantalla_raiz.iconbitmap("logo.ico")
#Index de color girs de la pnatalla de inicio
index=Frame()
index.pack(fill="both", expand="True", padx="50", pady="50")
index.config(bg="white", width="650", height="350")
index.config(bg="#B5B2B2")
logo=PhotoImage(file="banco.2.png")
#Label de la pnatalla de inicio
Label(index, text="Binevenido al Banco del Caribe ", fg="black", bg="#B5B2B2", font=("Tahoma",12)).place(x=215, y=125)
#Label de imagen
Label(index, image=logo).place(x=265, y=10)
#Boton de inicio
def sig():
    btn_modificacion=Button(index,text="Modificacion de Clientes",bg="#000080", fg="white").grid(row=0, column=0)
    btn_transaccion=Button(index,text="Agregar Transaccion", bg="#000080", fg="white").grid(row=0, column=1)
    btn_depositos=Button(index,text="Lista de Depositos",width=19, bg="#000080", fg="white").grid(row=1, column=0)
    btn_retiros=Button(index,text="Lista de Retiros",width=16, bg="#000080", fg="white").grid(row=1, column=1)
    btn_clientes=Button(index,text="Listado de Clientes",width=19, bg="#000080", fg="white").grid(row=2, column=0)
    btn_salir=Button(index,text="Salir",bg="#000080",width=16,fg="white", command="destroy .").grid(row=2, column=1)
btn=Button(index,text="Inicio", width=10, bg="#000080", fg="white", command=sig)
btn.place(x=275,y=200)
pantalla_raiz.mainloop()