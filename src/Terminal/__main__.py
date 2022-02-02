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
    
def writeSpeakableFile():
    print(" WRITE TEXT ".center(120, "║"))
    text = str(input())
    with open('output.txt', 'w+') as file:
        file.write(text)

def readSpeakableFile(language):
    with open('output.txt', 'r') as file:
        text = file.read()
        if language == 0:
            file = gTTS(text=text, lang='en')
        elif language == 1:
            file = gTTS(text=text, lang='es')
        file.save('output.mp3')
        playsound('output.mp3')
        remove('output.mp3')


def option(): #Menu de opciones | Menu options
    print(" OPTION ".center(120, "║"))
    op = int(input(" -- > "))

    if op == 1:
        writeSpeakableFile()
    elif op == 2:
        readSpeakableFile(0)
    elif op == 3:
        writeSpeakableFile()
    elif op == 4:
        readSpeakableFile(1)



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