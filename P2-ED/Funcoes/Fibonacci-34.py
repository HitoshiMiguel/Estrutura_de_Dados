def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Digite o valor de n para calcular o n-ésimo termo de Fibonacci: "))
print(f"O {n}-ésimo termo da sequência de Fibonacci é: {fibonacci(n)}")
