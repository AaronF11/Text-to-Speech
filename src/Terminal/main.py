from os import system, remove
from gtts import gTTS #pip install gTTS
from playsound import playsound #pip install playsound==1.2.2
from msvcrt import getch

ESC = 27
ENTER = 13

def off(): #Función para borrar y dar opción de salir | Function to delete and give option to exit
    system("cls")
    print("╔══════════════════════════════╗".center(127," "))
    print("║   [1] EXIT || [2] CONTINUE   ║".center(127," "))
    print("╚══════════════════════════════╝".center(127," "))

def title(): #Función de titulo | Title function
    print("\n\n\n\n\n")
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗".center(127," "))
    print("║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║".center(127," "))
    print("║  ╠══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╣  ║".center(127," "))
    print("║  ║                             TEXT-TO-SPEECH                            ║  ║".center(127," "))
    print("║  ╠═══════════════════════════════════╦═══════════════════════════════════╣  ║".center(127," "))
    print("║  ║              ENGLISH              ║              SPANISH              ║  ║".center(127," "))
    print("║  ╠═════════════════╦═════════════════╬═════════════════╦═════════════════╣  ║".center(127," "))
    print("║  ║      WRITE      ║      LISTEN     ║      WRITE      ║      LISTEN     ║  ║".center(127," "))
    print("║  ╠═════════════════╬═════════════════╬═════════════════╬═════════════════╣  ║".center(127," "))
    print("║  ║       [1]       ║       [2]       ║       [3]       ║       [4]       ║  ║".center(127," "))
    print("║  ╠══╦══╦══╦══╦══╦══╬══╦══╦══╦══╦══╦══╬══╦══╦══╦══╦══╦══╬══╦══╦══╦══╦══╦══╣  ║".center(127," "))
    print("║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║".center(127," "))
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝".center(127," "))

def writeEnglish(): #Función para crear y sobrescribir txt en inglés | Function to create and overwrite txt in English
    file = open("EnglishFile.txt", "w")
    print(" WRITE TEXT ".center(120, "║"))
    record = str(input(""))
    file.write(record)
    file.close()
    system("cls")

def voiceEnglish(): #Función para crear archivo de voz en inglés | Function to create voice file in Spanish
    with open("EnglishFile.txt", "r") as file:
        text = file.read()
    file = gTTS(text, lang = "en")
    filename = "English.mp3"
    file.save(filename)

def writeSpanish(): #Función para crear y sobrescribir txt en español | Function to create and overwrite txt in Spanish
    file = open("SpanishFile.txt", "w")
    print(" WRITE TEXT ".center(120, "║"))
    record = str(input(""))
    file.write(record)
    file.close()
    system("cls")

def voiceSpanish(): #Función para crear archivo de voz en español | Function to create voice file in Spanish
    with open("SpanishFile.txt", "r") as file:
        text = file.read()
    file = gTTS(text, lang = "es")
    filename = "Spanish.mp3"
    file.save(filename)

def option(): #Menu de opciones | Menu options
    print(" OPTION ".center(120, "║"))
    op = int(input(" -- > "))
    
    #Versión Inglés | English version
    if op == 1:
        writeEnglish()
    elif op == 2:
        voiceEnglish()
        audio = "English.mp3"
        playsound(audio)
        remove("English.mp3")
    #Versión Español | Spanish version
    elif op == 3:
        writeSpanish()
    elif op == 4:
        voiceSpanish()
        audio = "Spanish.mp3"
        playsound(audio)
        remove("Spanish.mp3")


def main(): #Función main para mandar a llamar las demas funciones | Main function to call the other functions
    while True:
        title()
        option()
        off()
        print("".center(120, "║"))
        op = int(input(" -- > ")) #Opción para salir o continuar | Option to exit or continue
        if op == 1: 
            exit(0)
        if op == 2:
            system("cls")
            continue
    
if __name__ == '__main__':
    main()