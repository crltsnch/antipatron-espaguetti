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

        self.result_label = tk.Label(root, text="Resultado:")
        self.result_label.pack()

        self.button_suma = tk.Button(root, text="Suma", command=self.suma)
        self.button_suma.pack()

        self.button_resta = tk.Button(root, text="Resta", command=self.resta)
        self.button_resta.pack()

        self.button_multiplicacion = tk.Button(root, text="Multiplicación", command=self.multiplicacion)
        self.button_multiplicacion.pack()

        self.button_division = tk.Button(root, text="División", command=self.division)
        self.button_division.pack()

        self.quit_button = tk.Button(root, text="Salir", command=root.destroy)
        self.quit_button.pack()