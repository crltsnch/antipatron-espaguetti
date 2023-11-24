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