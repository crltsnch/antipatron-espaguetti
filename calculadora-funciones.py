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


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("No se puede dividir entre cero.")

def main():
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 5:
        print("Gracias por usar la calculadora.")
        return
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if opcion == 1:
        print("El resultado de la suma es: ", suma(num1, num2))
    elif opcion == 2:
        print("El resultado de la resta es: ", resta(num1, num2))
    elif opcion == 3:
        print("El resultado de la multiplicación es: ", multiplicacion(num1, num2))
    elif opcion == 4:
        try:
            print("El resultado de la división es: ", division(num1, num2))
        except ValueError as e:
            print(e)
    else:
        print("Opción no soportada.")
    
if __name__ == '__main__':
    main()
