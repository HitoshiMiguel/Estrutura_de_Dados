while True:
    N = int(input("Digite um número inteiro maior ou igual a 2: "))
    
    if N >= 2:
        break
    print("Digite um número maior ou igual a 2: ")

fibo = [0, 1]

for i in range(2, N):
    proximo = fibo[i - 1] + fibo[i - 2]
    print(f"fibo[{i-2}] + fibo[{i-1}] = {fibo[i-2]} + {fibo[i-1]} = {proximo}")
    fibo.append(proximo)
    
print("Sequência de Fibonacci completa:", fibo)