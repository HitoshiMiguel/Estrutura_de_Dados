lista = []

while True:
    qtde = int(input("Digite um número inteiro: "))

    if qtde == 0:
        break

    posicao = 0
    while posicao < len(lista) and lista[posicao] < qtde:
        posicao += 1

    lista.insert(posicao, qtde)

    print("Lista:", lista)
