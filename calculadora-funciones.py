'''def calcular(operacion, num1, num2):
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
        print("Operación no soportada.")'''

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def set_nums(self):
        self.num1 = input("Introduce el primer número: ")
        self.num2 = input("Introduce el segundo número: ")

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




def calcular(self, operacion):
        if operacion == 'suma':
            return self.suma()
        if operacion == 'resta':
            return self.resta()
        if operacion == 'multiplicacion':
            return self.multiplicacion()
        if operacion == 'division':
            return self.division()
        else:
            raise ValueError("Operación no soportada.")

