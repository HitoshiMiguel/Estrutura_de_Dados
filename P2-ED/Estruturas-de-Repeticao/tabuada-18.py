num = int(input("Digite o número desejado:"))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")