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

    def get_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar números.")
            return None
        return num1, num2   
    
    def mostrar_resultado(self, resultado):
        self.result_label.config(text=f"Resultado: {resultado}")
    
    def suma(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            calculadora = Calculadora(num1, num2)
            result = calculadora.suma()
            self.mostrar_resultado(result)
    
    def resta(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            calculadora = Calculadora(num1, num2)
            result = calculadora.resta()
            self.mostrar_resultado(result)

    def multiplicacion(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            calculadora = Calculadora(num1, num2)
            result = calculadora.multiplicacion()
            self.mostrar_resultado(result)
    
    def division(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            calculadora = Calculadora(num1, num2)
            try:
                result = calculadora.division()
                self.mostrar_resultado(result)
            except ValueError as e:
                messagebox.showerror("Error, no se puede dividir entre 0", e)
                return None

def main():
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()

if __name__ == '__main__':
    main()