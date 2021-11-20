from logging import root
import tkinter


window = tkinter.Tk() #Crear la ventana
window.geometry("400x200") #Dar tamaño
window.resizable(0,0) #Bloquear maximizar
label = tkinter.Label(window, text = "Text to Speech", bg = "white", font = "console 20") #Crear la etiqueta
label.pack(fill = tkinter.X) #Imprimir etiqueta

window.mainloop()