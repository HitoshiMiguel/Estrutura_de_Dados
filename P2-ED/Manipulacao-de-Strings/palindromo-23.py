palavra = input("Digite a palavra que deseja verificar: ")

if palavra == palavra[::-1]:
    print("A palavra é palíndromo!")
else:
    print("A palavra não é palíndromo!")