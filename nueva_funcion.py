#nueva funcion Pull Request#

# ============================
#      FUNCIONES DEL SISTEMA
# ============================

def fibonacci(n):
    """Retorna el n-ésimo número Fibonacci."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factorial(n):
    """Retorna el factorial de n."""
    if n < 0:
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def es_primo(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def es_perfecto(num):
    """Verifica si un número es perfecto."""
    if num < 2:
        return False

    suma = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            suma += i
            if i != num // i:
                suma += num // i

    return suma == num


def primeros_n_perfectos(n):
    """Genera los primeros N números perfectos."""
    perfectos = []
    num = 2
    while len(perfectos) < n:
        if es_perfecto(num):
            perfectos.append(num)
        num += 1
    return perfectos


# ============================
#          MENÚ MEJORADO
# ============================

class Color:
    RESET = "\033[0m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"


def input_entero(mensaje):
    """Solicita un número entero con validación."""
    while True:
        try:
            return int(input(Color.YELLOW + mensaje + Color.RESET))
        except ValueError:
            print(Color.RED + "❌ Error: debe ingresar un número entero válido." + Color.RESET)


def menu():
    while True:
        print(Color.CYAN + "\n========== MENÚ PRINCIPAL ==========" + Color.RESET)
        print(Color.BLUE + "1." + Color.RESET, "Cálculo de Fibonacci")
        print(Color.BLUE + "2." + Color.RESET, "Cálculo del factorial")
        print(Color.BLUE + "3." + Color.RESET, "Determinar si un número es primo")
        print(Color.BLUE + "4." + Color.RESET, "Generar los primeros N números perfectos")
        print(Color.BLUE + "5." + Color.RESET, "Salir")
        print(Color.CYAN + "====================================" + Color.RESET)

        opcion = input(Color.YELLOW + "\nSeleccione una opción: " + Color.RESET)

        if opcion == "1":
            n = input_entero("Ingrese el valor de n para Fibonacci: ")
            print(Color.GREEN + f"➡ Fibonacci({n}) = {fibonacci(n)}" + Color.RESET)

        elif opcion == "2":
            n = input_entero("Ingrese un número para obtener su factorial: ")
            resultado = factorial(n)
            if resultado is None:
                print(Color.RED + "❌ El factorial no existe para números negativos." + Color.RESET)
            else:
                print(Color.GREEN + f"➡ {n}! = {resultado}" + Color.RESET)

        elif opcion == "3":
            n = input_entero("Ingrese un número para verificar si es primo: ")
            if es_primo(n):
                print(Color.GREEN + f"✔ {n} ES un número primo." + Color.RESET)
            else:
                print(Color.RED + f"✖ {n} NO es un número primo." + Color.RESET)

        elif opcion == "4":
            n = input_entero("¿Cuántos números perfectos desea generar?: ")
            lista = primeros_n_perfectos(n)
            print(Color.MAGENTA + "➡ Números perfectos:" + Color.RESET, lista)

        elif opcion == "5":
            print(Color.CYAN + "\n👋 Saliendo del programa... ¡Hasta luego!" + Color.RESET)
            break

        else:
            print(Color.RED + "❌ Opción inválida. Intente nuevamente." + Color.RESET)


# ============================
#       PUNTO DE ENTRADA
# ============================

if __name__ == "__main__":
    menu()
