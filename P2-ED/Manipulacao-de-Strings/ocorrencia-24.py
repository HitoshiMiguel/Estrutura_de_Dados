text = input("Digite um texto: ")

letra_antiga = input("Digite a letra que deseja substituir: ")
letra_nova = input("Digite a nova letra: : ")

text_sub = text.replace(letra_antiga, letra_nova)
print(f"O texto após a substituição é: {text_sub}")
