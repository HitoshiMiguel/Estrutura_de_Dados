def aplicar_funcao(lista, func):
    return [func(x) for x in lista]

lista = [13, 42, 3, 34, 15]
funcao = lambda x: x ** 2

resultado = aplicar_funcao(lista, funcao)
print(f"Resultado após aplicar a função: {resultado}")
