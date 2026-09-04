print("\nCALCULANDO O CUSTO DE ENERGIA DE UMA CASA\n")

print("Tarifa: R$ 0,80 / KWh\n")

print(80 * "-")

quantidade_tipos_utensilio = int(input("Quantos tipos de utensílio terão na casa? "))

print(80 * "-")

print()

custo_total_dia = 0
custo_total_mes = 0

for i in range(quantidade_tipos_utensilio):
    nome_utensilio = input(f"Qual o nome do {i + 1}º utensílio? ")
    print()
    quantidade_utensilio = int(input(f"Quantas unidades de {nome_utensilio} a casa terá? "))
    print()
    potencia_utensilio = int(input(f"Qual a potência em W do(a) {nome_utensilio}? "))
    print()
    quantidade_horas_uso = float(input(f"Qual o total da média de horas de uso por dia do(a) {nome_utensilio}? "))
    print()

    print(80 * "-")

    gasto_energia_dia = potencia_utensilio * (quantidade_horas_uso / 1000)
    gasto_energia_mes = potencia_utensilio * (quantidade_horas_uso / 1000) * 30
    custo_energia_dia = (potencia_utensilio * (quantidade_horas_uso / 1000)) * 0.8
    custo_energia_mes = ((potencia_utensilio * (quantidade_horas_uso / 1000)) * 0.8) * 30

    custo_total_dia += custo_energia_dia
    custo_total_mes += custo_energia_mes

    print()


    print(f"Utensílio: {nome_utensilio}")
    print()
    print(f"Quantidade: {quantidade_utensilio}")
    print()
    print(f"Gasto de energia por dia: {gasto_energia_dia} KW")
    print()
    print(f"Gasto de energia por mês: {gasto_energia_mes} KW")
    print()
    print(f"Custo por dia: R$ {custo_energia_dia:.2f}")
    print()
    print(f"Custo por mês: R$ {custo_energia_mes:.2f}")
    print()
    print(80 * "-")
    print()


print(f"Custo total em média de energia da casa por dia: R$ {custo_total_dia:.2f}")
print()
print(f"Custo total em média de energia da casa por mês: R$ {custo_total_mes:.2f}")
print()
print(80 * "-")