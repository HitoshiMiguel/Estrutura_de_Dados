nome_arquivo = input("Digite o nome do arquivo para abrir: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print(f"Erro! O arquivo '{nome_arquivo}' não foi encontrado.")