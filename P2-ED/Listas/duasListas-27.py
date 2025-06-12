def elementos_comuns(lista1, lista2):
    return [elemento for elemento in lista1 if elemento in lista2]

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 9, 5, 21, 57]

resultado = elementos_comuns(lista1, lista2)
print(f"Elementos comuns entre as listas: {resultado}")
