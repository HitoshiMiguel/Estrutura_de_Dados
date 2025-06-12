def remover_duplicados(lista):
    return list(set(lista))

lista_com_duplicados = [1, 2, 3, 4, 5, 2, 3, 6, 7, 5]
lista_sem_duplicados = remover_duplicados(lista_com_duplicados)

print(f"Lista original: {lista_com_duplicados}")
print(f"Lista sem duplicados: {lista_sem_duplicados}")
