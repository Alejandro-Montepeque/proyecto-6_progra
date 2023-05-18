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
Label(index, image=logo).place(x=265, y=2)
#Boton de inicio
btn=Button(index,text="Inicio", width=10, bg="#000080", fg="white")
btn.place(x=275,y=200)


pantalla_raiz.mainloop()