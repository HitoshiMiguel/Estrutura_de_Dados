def numeros_pares(n):
    return list(range(0, n+1, 2))

n = int(input("Digite um valor para n: "))
print(f"Os números pares entre 0 e {n} são: {numeros_pares(n)}")
