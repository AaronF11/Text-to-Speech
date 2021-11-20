from logging import root
from gtts import gTTS
from playsound import playsound
import tkinter



window = tkinter.Tk() #Crear la ventana
window.geometry("400x200") #Dar tamaño
window.resizable(0,0) #Bloquear maximizar

label = tkinter.Label(window, text = "Text to Speech", bg = "white", font = "console 20") #Crear la etiqueta
label.pack(fill = tkinter.X) #Imprimir etiqueta

def WriteText():
    text = TextBox.get()
    file = open("file.txt", "w")
    file.write(text)
    file.close()
    with open("file.txt", "r") as file:
        text = file.read()
    file = gTTS(text=text,lang="ES")
    filename = "voice.mp3"
    file.save(filename)
    audio = "voice.mp3"
    playsound(audio)


button = tkinter.Button(window, text = "Español", command= WriteText)
button.pack()

TextBox = tkinter.Entry(window)
TextBox.pack()





window.mainloop()

    