num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador: "))

if num2 == 0:
    print("Erro! Não é possível realizar divisão com zero")
else:
    resultado = num1 / num2
    print(f"O resultado é: {resultado}")