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
