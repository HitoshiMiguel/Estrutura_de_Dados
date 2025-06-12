l1 = float(input("Digite o comprimento do primeiro lado: "))
l2 = float(input("Digite o comprimento do segundo lado: "))
l3 = float(input("Digite o comprimento do terceiro lado: "))

if l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
