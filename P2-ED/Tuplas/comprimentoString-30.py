def comprimento_strings(tupla_strings):
    return tuple(len(s) for s in tupla_strings)

tupla_strings = ("Arroz", "Carro", "Papel", "JavaScript")
comprimentos = comprimento_strings(tupla_strings)
print(f"Os comprimentos das strings são: {comprimentos}")
