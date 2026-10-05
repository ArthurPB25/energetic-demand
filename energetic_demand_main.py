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

#US03
print("\n--- SELEÇÃO DE INVERSOR (US03) ---")
arquivo_inversores = open("inversores.csv", "r")
linhas_inversores = arquivo_inversores.readlines()
arquivo_inversores.close()
 
menor_custo_inversor = 9999999.99
inversor_fabricante = ""
inversor_modelo = ""
inversor_tipo = ""
 
for i in range(1, len(linhas_inversores)):
    dados_inv = linhas_inversores[i].strip().split(",")
    fabricante_inv = dados_inv[1]
    modelo_inv = dados_inv[2]
    potencia_inv = float(dados_inv[3])
    tipo_inv = dados_inv[4]
    preco_inv = float(dados_inv[5])
 
    # Regra: Potencia nominal >= 0.85 * Pinstalada E tipo Grid-Tie
    if potencia_inv >= (0.85 * potencia_instalada) and tipo_inv == "Grid-Tie":
        if preco_inv < menor_custo_inversor:
            menor_custo_inversor = preco_inv
            inversor_fabricante = fabricante_inv
            inversor_modelo = modelo_inv
            inversor_tipo = tipo_inv
 
if menor_custo_inversor == 9999999.99:
    print("Erro: Nenhum inversor Grid-Tie compatível encontrado.")
else:
    print(f"Inversor Selecionado: 1x {inversor_fabricante} {inversor_modelo} ({inversor_tipo}) - R$ {menor_custo_inversor:.2f}")

#US04
print("\n--- DIMENSIONAMENTO DE BATERIAS (US04) ---")
autonomia_horas = float(input("Digite a autonomia desejada em horas (0 para sem baterias): "))
 
if autonomia_horas > 0:
    consumo_diario = consumo_mensal / 30
    energia_autonomia = consumo_diario * (autonomia_horas / 24)
 
    arquivo_baterias = open("baterias.csv", "r")
    linhas_baterias = arquivo_baterias.readlines()
    arquivo_baterias.close()
 
    dados_bat = linhas_baterias[1].strip().split(",")
    bateria_fabricante = dados_bat[1]
    bateria_modelo = dados_bat[2]
    capacidade_kWh = float(dados_bat[4])
    dod = float(dados_bat[5])
    preco_bat = float(dados_bat[7])
    eficiencia_bateria = 0.95
    capacidade_requerida = energia_autonomia / (dod * eficiencia_bateria)
    qtd_baterias = math.ceil(capacidade_requerida / capacidade_kWh)
    custo_baterias = qtd_baterias * preco_bat
 
    print(f"Banco de Baterias: {qtd_baterias}x {bateria_fabricante} {bateria_modelo} - R$ {custo_baterias:.2f}")
else:
    print("Nenhuma bateria adicionada ao projeto.")