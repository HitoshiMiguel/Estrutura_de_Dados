num = input("digite um número: ")

try:
    num1 = int(num)
    print("Sucesso! a conversão deu certo!")
except ValueError:
    print("Erro! digite apenas algarismos")
