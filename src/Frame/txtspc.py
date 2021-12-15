from os import remove
from pathlib import Path
from gtts import gTTS
from playsound import playsound


def writeSpeakableFile(text):
    with open("output.txt", "w+") as file:
        file.write(text)


def readSpeakableFile(lenguage):
    with open("output.txt", "r") as file:
        text = file.read()
        if lenguage == 0:
            file = gTTS(text=text, lang="es")
        if lenguage == 1:
            file = gTTS(text=text, lang="en")
        fileName = "tts.mp3"
        file.save(fileName)
        playsound(fileName)
        remove(fileName)


def writeAndReadSpeakableFile(text, lenguage):
    writeSpeakableFile(text)
    readSpeakableFile(lenguage)
