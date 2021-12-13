from tkinter import Tk
from tkinter import ttk
from tkinter import *


def initEnglishTab(tab):
    textArea = Text(tab, width=80, height=20, font=("Arial", 14, "normal"))

    textArea.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    )

    playButton = Button(tab,
                        text="Play audio",
                        bg="#1ED760",
                        fg="#FFFFFF",
                        activebackground="#43E57D",
                        activeforeground="#FFFFFF",
                        cursor="hand2",
                        font=("Arial", 16, "bold"),
                        borderwidth=0)

    playButton.pack(fill="both", padx=10, pady=10)


def initSpanishTab(tab):
    textArea = Text(tab, width=80, height=20, font=("Arial", 14, "normal"))

    textArea.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    )

    playButton = Button(tab,
                        text="Reproducir audio",
                        bg="#1ED760",
                        fg="#FFFFFF",
                        activebackground="#43E57D",
                        activeforeground="#FFFFFF",
                        cursor="hand2",
                        font=("Arial", 16, "bold"),
                        borderwidth=0)

    playButton.pack(fill="both", padx=10, pady=10)


def main():

    root = Tk()
    root.title("Text to speech - GUI")
    root.geometry("800x600")

    tabs = ttk.Notebook(root)

    english_tab = ttk.Frame(tabs)
    spanish_tab = ttk.Frame(tabs)

    initEnglishTab(english_tab)
    initSpanishTab(spanish_tab)

    tabs.add(english_tab, text="English")
    tabs.add(spanish_tab, text="Español")

    tabs.pack(expand=10, fill="both")

    root.iconbitmap("src/Frame/resources/ico.ico")
    root.mainloop()