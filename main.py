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
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            suma += i
            if i != num // i:
                suma += num // i
    return suma == num


def primeros_n_perfectos(n):
    """Genera una lista con los primeros N números perfectos."""
    perfectos = []
    num = 2
    while len(perfectos) < n:
        if es_perfecto(num):
            perfectos.append(num)
        num += 1
    return perfectos


#   MENÚ

def menu():
    while True:
        print("\n===== MENÚ  =====")
        print("1. Cálculo de Fibonacci")
        print("2. Cálculo del factorial")
        print("3. Determinar si un número es primo")
        print("4. Generar los primeros N números perfectos")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese el valor de n para Fibonacci: "))
            print(f"Fibonacci({n}) = {fibonacci(n)}")

        elif opcion == "2":
            n = int(input("Ingrese un número para obtener su factorial: "))
            resultado = factorial(n)
            if resultado is None:
                print("El factorial no existe para números negativos.")
            else:
                print(f"{n}! = {resultado}")

        elif opcion == "3":
            n = int(input("Ingrese un número para verificar si es primo: "))
            if es_primo(n):
                print(f"{n} ES un número primo.")
            else:
                print(f"{n} NO es un número primo.")

        elif opcion == "4":
            n = int(input("¿Cuántos números perfectos desea generar?: "))
            print("Números perfectos:", primeros_n_perfectos(n))

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    menu()
#### 