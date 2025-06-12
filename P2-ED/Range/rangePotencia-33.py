def potencias_de_2(expoente):
    return [2**i for i in range(expoente+1)]

expoente = int(input("Digite o expoente máximo: "))
print(f"As potências de 2 até o expoente {expoente} são: {potencias_de_2(expoente)}")
