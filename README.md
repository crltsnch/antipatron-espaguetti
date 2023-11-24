# antipatron-espaguetti
El link a mi repositorio es: [GitHub](https://github.com/crltsnch/antipatron-espaguetti.git)
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
