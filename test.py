def fibonacci(n):
    if n == 0:
        print(0)
        return 0
    if n == 1:
        print
        return 1
    resultado = fibonacci(n-1) + fibonacci(n-2)
    print(resultado)
    return resultado

fibonacci(3)
