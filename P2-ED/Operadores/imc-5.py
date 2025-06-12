peso = float(input("Digite o peso atual: "))
altura = float(input("Digite a altura atual: "))

alturaQuadrado = altura * altura

imc = peso / alturaQuadrado

print(f"O IMC é de: {imc}")
