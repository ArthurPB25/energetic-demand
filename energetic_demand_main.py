import math
 
print("\n--- DIMENSIONAMENTO DA DEMANDA E POTÊNCIA SOLAR (US01) ---")
 
consumo_mensal = float(input("Digite o consumo médio mensal da residência (kWh): "))
 
while consumo_mensal <= 0:
    print("Erro: Consumo mensal inválido. Deve ser maior que zero.")
    consumo_mensal = float(input("Digite o consumo médio mensal da residência (kWh): "))
 
f = float(input("Digite o percentual de atendimento desejado (1 a 100): "))
 
while f < 1 or f > 100:
    print("Valor inválido! O percentual deve ser entre 1 e 100.")
    f = float(input("Digite o percentual de atendimento desejado (1 a 100): "))
 
hsp = float(input("Digite as Horas de Sol Pleno (HSP) da sua região: "))
rendimento_global = 0.78  # Padrão de 78%
 
energia_mensal_alvo = consumo_mensal * (f / 100)
potencia_requerida = energia_mensal_alvo / (hsp * 30 * rendimento_global)
 
print(f"\nEnergia mensal alvo (EFV): {energia_mensal_alvo:.2f} kWh/mês")
print(f"Potência requerida (PFV): {potencia_requerida:.2f} kWp")

#US02

print("\n--- SELEÇÃO DE MÓDULOS FOTOVOLTAICOS (US02) ---")
arquivo_paineis = open("paineis.csv", "r")
linhas_paineis = arquivo_paineis.readlines()
arquivo_paineis.close()
 
menor_custo_painel = 9999999.99
painel_fabricante = ""
painel_modelo = ""
qtd_paineis = 0
potencia_instalada = 0.0
 
for i in range(1, len(linhas_paineis)):
    dados = linhas_paineis[i].strip().split(",")
    fabricante = dados[1]
    modelo = dados[2]
    potencia_Wp = float(dados[3])
    preco = float(dados[5])
 
    potencia_kWp = potencia_Wp / 1000
    qtd_modulos = math.ceil(potencia_requerida / potencia_kWp)
    custo_total = qtd_modulos * preco
 
    if custo_total < menor_custo_painel:
        menor_custo_painel = custo_total
        painel_fabricante = fabricante
        painel_modelo = modelo
        qtd_paineis = qtd_modulos
        potencia_instalada = qtd_modulos * potencia_kWp
 
print(f"Potência Efetiva Instalada: {potencia_instalada:.2f} kWp")
print(f"Painéis Selecionados: {qtd_paineis}x {painel_fabricante} {painel_modelo} - R$ {menor_custo_painel:.2f}")

