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