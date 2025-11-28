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
    """Genera los primeros N números perfectos."""
    perfectos = []
    num = 2
    while len(perfectos) < n:
        if es_perfecto(num):
            perfectos.append(num)
        num += 1
    return perfectos
