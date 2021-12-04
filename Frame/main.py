from logging import root
from gtts import gTTS
from playsound import playsound
from tkinter import *

window = Tk() #Crear la ventana
window.title("Text-to-Speech") #Titulo de la ventana
window.iconbitmap("src\ico\ico.ico") #Icono de la ventana
#window.geometry("400x200") #Dar tamaño
window.resizable(0,0) #Bloquear maximizar

frame = Frame()
frame.pack()
frame.config(bg="white", borderwidth=2, relief="ridge")

labelEnglish = Label(frame, text="ENGLISH", width=20, height=3, borderwidth=1, relief="sunken", bg="white", padx="3", pady="3")
labelEnglish.grid(row=0, column=0)
labelSpanish = Label(frame, text="SPANISH", width=20, height=3, borderwidth=1, relief="sunken", bg ="white", padx="3", pady="3")
labelSpanish.grid(row=0, column=1)

space = Label(frame, width=20)
space.grid(row=1, column=0)
space = Label(frame, width=20)
space.grid(row=1, column=1)

buttonWriteEnglish = Button(frame,text="WRITE", width=20, height=1, borderwidth=2, relief="raised", bg ="white", padx="1", pady="1")
buttonWriteEnglish.grid(row=2, column=0)
space = Label(frame, width=20)
space.grid(row=3, column=0)
buttonListenEnglish = Button(frame,text="LISTEN", width=20, height=1, borderwidth=2, relief="raised", bg ="white", padx="1", pady="1")
buttonListenEnglish.grid(row=4, column=0)

buttonWriteSpanish = Button(frame,text="WRITE", width=20, height=1, borderwidth=2, relief="raised", bg ="white", padx="1", pady="1")
buttonWriteSpanish.grid(row=2, column=1)
space = Label(frame, width=20)
space.grid(row=3, column=1)
buttonListenSpanish = Button(frame,text="LISTEN", width=20, height=1, borderwidth=2, relief="raised", bg ="white", padx="1", pady="1")
buttonListenSpanish.grid(row=4, column=1)

window.mainloop()    