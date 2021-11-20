import os
import sys
from os import system, remove
from gtts import gTTS #pip install gTTS
from playsound import playsound #pip install playsound==1.2.2
from msvcrt import getch

ESC = 27
ENTER = 13

def off():
    system("cls")
    print("╔══════════════════════════════╗".center(127," "))
    print("║   [1] EXIT || [2] CONTINUE   ║".center(127," "))
    print("╚══════════════════════════════╝".center(127," "))

                


def title():
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

def writeEnglish():
    file = open("EnglishFile.txt", "w")
    print(" WRITE TEXT ".center(120, "║"))
    record = str(input(""))
    file.write(record)
    file.close()
    system("cls")

def voiceEnglish():
    with open("EnglishFile.txt", "r") as file:
        text = file.read()
    file = gTTS(text, lang = "en")
    filename = "English.mp3"
    file.save(filename)

def writeSpanish():
    file = open("SpanishFile.txt", "w")
    print(" WRITE TEXT ".center(120, "║"))
    record = str(input(""))
    file.write(record)
    file.close()
    system("cls")

def voiceSpanish():
    with open("SpanishFile.txt", "r") as file:
        text = file.read()
    file = gTTS(text, lang = "es")
    filename = "Spanish.mp3"
    file.save(filename)

def option():
    print("\n")
    print(" OPTION ".center(120, "║"))
    op = int(input(" -- > "))
    
    #English version
    if op == 1:
        writeEnglish()
    elif op == 2:
        voiceEnglish()
        audio = "English.mp3"
        playsound(audio)
        remove("English.mp3")
    #Spanish version
    elif op == 3:
        writeSpanish()
    elif op == 4:
        voiceSpanish()
        audio = "Spanish.mp3"
        playsound(audio)
        remove("Spanish.mp3")


def main():
    while True:
        title()
        option()
        off()
        print("".center(120, "║"))
        op = int(input(" -- > "))
        if op == 1: 
            exit(0)
        if op == 2:
            system("cls")
            continue
    
if __name__ == '__main__':
    main()
    


