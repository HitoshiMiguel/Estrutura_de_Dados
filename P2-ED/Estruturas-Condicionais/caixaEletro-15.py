saldo = float(input("Digite o saldo atual em conta:"))
saque = float(input("Digite o valor desejado para sacar:"))

if saldo < saque:
    print("Saldo indisponível para saque")
else:
    print("Saque disponível, por favor aguarde")