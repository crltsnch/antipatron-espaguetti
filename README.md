# antipatron-espaguetti
El link a mi repositorio es: [GitHub](https://github.com/crltsnch/antipatron-espaguetti.git)

### Ejercicio
Un antipatrón de programación es un patrón que puede ser considerado una mala práctica. "Spaghetti Code" es un antipatrón que se refiere a código con una estructura de control compleja, difícil de leer y seguir, generalmente debido a múltiples saltos de control, como instrucciones GOTO, ciclos y excepciones. Dada esta porción de código Python escrita en estilo "Spaghetti Code", se pide identificar las principales características de este antipatrón y refactorizar el código para mejorar su legibilidad y mantenibilidad.

```
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
```
Este código presenta dificultades para su comprensión y seguimiento, ya que carece de una estructura lógica clara. Resulta confuso entender su propósito debido a la falta de claridad en las variables y a decisiones que parecen arbitrarias. Características del "Spaghetti Code":

- El uso de cadenas de texto para controlar la lógica del programa puede ser confuso y propenso a errores. En lugar de utilizar un enfoque basado en cadenas, sería más claro utilizar estructuras de control más directas y así tener una estructura de control de flujo más comprensible.

- La función calcular realiza múltiples tareas, incluyendo la verificación de la operación, la realización de la operación y el manejo de errores. Esto va en contra del principio de responsabilidad única. Cada función debería tener una tarea específica.

- El manejo de errores podría mejorarse para proporcionar mensajes de error más útiles y para no imprimir mensajes directamente desde la función.

### Solución
Este anti-patrón a menudo se asocia con la falta de estructura y organización en el código, lo que puede hacer que sea difícil de mantener y depurar y que el tiempo de desarrollo sea más largo. La manera de abordar este problema es llevar a cabo una refactorización del código, buscando establecer una estructura lógica más clara y facilitar su comprensión. Este proceso incluye la creación de funciones sumar, restar, multiplicar y dvividir y clases Calcularosa para encapsular la funcionalidad, mejorar la nomenclatura de las variables, y elimianr porciones de código redundantes o innecesarias.

#### calculadora.py
```
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            raise ValueError("No se puede dividir entre cero.")
```

#### main.py
En este fichero he impmlementado un menu y una función main haciendo uso de la clase calculadora para poder hacer calculos por consola.
```
from calculadora import Calculadora

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    calculadora = Calculadora(num1, num2)

    while True:
        menu()
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 5:
            print("Gracias por usar la calculadora.")
            break

        if opcion in [1, 2, 3, 4]:
            if opcion == 1:
                resultado = calculadora.suma()
            elif opcion == 2:
                resultado = calculadora.resta()
            elif opcion == 3:
                resultado = calculadora.multiplicacion()
            elif opcion == 4:
                try:
                    resultado = calculadora.division()
                except ValueError as e:
                    print(e)
                    continue
        else:
            print("Opción no soportada.")
            continue

        print(f"El resultado de la operación es: {resultado}")


if __name__ == '__main__':
    main()
```
#### interfaz.py
Luego hemos usado la libreria Tkinter para crear una interfaz gráfica en la que poder ingresar numeros enteros o decimales y hacer sumas, restas, multiplicaciones o divisiones.

```
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
```
