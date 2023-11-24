from calculadora import Calculadora
from tkinter import messagebox
import tkinter as tk

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.label1 = tk.Label(root, text="Ingrese el primer número:")
        self.label1.pack()

        self.entry1 = tk.Entry(root)
        self.entry1.pack()

        self.label2 = tk.Label(root, text="Ingrese el segundo número:")
        self.label2.pack()

        self.entry2 = tk.Entry(root)
        self.entry2.pack()

        