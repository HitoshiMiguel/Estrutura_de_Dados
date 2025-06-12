def soma_numeros_naturais(n):
    return sum(range(1, n+1))

n = int(input("Digite um valor para n: "))
print(f"A soma dos primeiros {n} números naturais é: {soma_numeros_naturais(n)}")
