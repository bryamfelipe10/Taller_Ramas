def factorial(n):
    """Numero Factorial de n."""
    if n < 0:
        return None 
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado