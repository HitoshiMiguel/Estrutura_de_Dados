salBase = 500
comissao = 0.06
mes = float(input("Digite o total faturado pelo funcionário durante o mês: R$"))

C = mes * comissao
FT = salBase + C

print(f"O faturamento do funcionário é de:R${FT:.2f}")