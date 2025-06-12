def pessoa_mais_velha(lista_pessoas):
    pessoa_mais_velha = max(lista_pessoas, key=lambda pessoa: pessoa[1])
    return pessoa_mais_velha

lista_pessoas = [("Miguel", 20), ("Pedro", 25), ("Maria", 57), ("Antonio", 38)]
nome, idade = pessoa_mais_velha(lista_pessoas)
print(f"A pessoa mais velha é {nome}, com {idade} anos.")
