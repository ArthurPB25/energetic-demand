import math
 
print("Iniciando o sistema e preparando os bancos de dados...\n")
 
# Criação dos datasets (US02, US03, US04)
arquivo_paineis = open("paineis.csv", "w")
arquivo_paineis.write("id,fabricante,modelo,potencia_Wp,eficiencia,preco\n")
arquivo_paineis.write("1,Canadian,HiKu6,550,21.3,850.00\n")
arquivo_paineis.write("2,Jinko,Tiger Pro,450,20.8,600.00\n")
arquivo_paineis.close()
 
arquivo_inversores = open("inversores.csv", "w")
arquivo_inversores.write("id,fabricante,modelo,potencia_kW,tipo,preco\n")
arquivo_inversores.write("1,Growatt,MIN 3000,3.0,Grid-Tie,3200.00\n")
arquivo_inversores.write("2,Fronius,Primo 5.0,5.0,Grid-Tie,5500.00\n")
arquivo_inversores.write("3,Deye,SUN-5K,5.0,Hibrido,7500.00\n")
arquivo_inversores.write("4,Deye,SUN-8K,8.0,Hibrido,10500.00\n")
arquivo_inversores.close()
 
arquivo_baterias = open("baterias.csv", "w")
arquivo_baterias.write("id,fabricante,modelo,tecnologia,capacidade_kWh,dod,tensao_V,preco\n")
arquivo_baterias.write("1,Pylontech,US2000,LiFePO4,2.4,0.8,48,4500.00\n")
arquivo_baterias.close()
 
# Sistema Legado (US06) e Demanda (US01)
print("--- INTEGRAÇÃO COM SISTEMA LEGADO (US06) ---")
consumo_mensal = float(input("Digite o consumo médio mensal da residência (kWh): "))
while consumo_mensal <= 0:
    consumo_mensal = float(input("Digite o consumo médio mensal da residência (kWh): "))
 
print("\n--- DIMENSIONAMENTO DA DEMANDA (US01) ---")
f = float(input("Digite o percentual de atendimento desejado (1 a 100): "))
hsp = float(input("Digite as Horas de Sol Pleno (HSP) da sua região: "))
rendimento_global = 0.78
 
energia_mensal_alvo = consumo_mensal * (f / 100)
potencia_requerida = energia_mensal_alvo / (hsp * 30 * rendimento_global)
 
# Cenário A
print("\n=========================================================")
print("CENÁRIO A - SIMULAÇÃO SEM BATERIAS (GRID-TIE)")
print("=========================================================\n")
 
arquivo_paineis = open("paineis.csv", "r")
linhas_paineis = arquivo_paineis.readlines()
arquivo_paineis.close()
 
menor_custo_painel_A = 9999999.99
for i in range(1, len(linhas_paineis)):
    dados = linhas_paineis[i].strip().split(",")
    potencia_kWp = float(dados[3]) / 1000
    preco = float(dados[5])
    qtd_modulos = math.ceil(potencia_requerida / potencia_kWp)
    custo_total = qtd_modulos * preco
    if custo_total < menor_custo_painel_A:
        menor_custo_painel_A = custo_total
        painel_fabricante_A, painel_modelo_A = dados[1], dados[2]
        qtd_paineis_A, potencia_instalada_A = qtd_modulos, qtd_modulos * potencia_kWp
 
arquivo_inversores = open("inversores.csv", "r")
linhas_inversores = arquivo_inversores.readlines()
arquivo_inversores.close()
 
menor_custo_inversor_A = 9999999.99
for i in range(1, len(linhas_inversores)):
    dados_inv = linhas_inversores[i].strip().split(",")
    if float(dados_inv[3]) >= (0.85 * potencia_instalada_A) and dados_inv[4] == "Grid-Tie":
        if float(dados_inv[5]) < menor_custo_inversor_A:
            menor_custo_inversor_A = float(dados_inv[5])
            inversor_fabricante_A, inversor_modelo_A = dados_inv[1], dados_inv[2]
 
custo_equipamentos_A = menor_custo_painel_A + menor_custo_inversor_A
custo_indireto_A = custo_equipamentos_A * 0.35
custo_total_A = custo_equipamentos_A + custo_indireto_A
 
print(f"Potência Instalada: {potencia_instalada_A:.2f} kWp")
print(f"Painéis: {qtd_paineis_A}x {painel_fabricante_A} {painel_modelo_A} (R$ {menor_custo_painel_A:.2f})")
print(f"Inversor: 1x {inversor_fabricante_A} {inversor_modelo_A} (R$ {menor_custo_inversor_A:.2f})")
print(f"VALOR TOTAL (Cenário A): R$ {custo_total_A:.2f}")
 
# Cenário B
print("\n=========================================================")
print("CENÁRIO B - SIMULAÇÃO COM BATERIAS (HÍBRIDO)")
print("=========================================================\n")
 
autonomia_B = float(input("Digite a autonomia desejada em horas (Cenário B): "))
if autonomia_B > 0:
    consumo_diario = consumo_mensal / 30
    energia_autonomia = consumo_diario * (autonomia_B / 24)
 
    arquivo_baterias = open("baterias.csv", "r")
    linhas_baterias = arquivo_baterias.readlines()
    arquivo_baterias.close()
 
    dados_bat = linhas_baterias[1].strip().split(",")
    qtd_baterias_B = math.ceil(energia_autonomia / (float(dados_bat[5]) * 0.95) / float(dados_bat[4]))
    custo_baterias_B = qtd_baterias_B * float(dados_bat[7])
 
    menor_custo_inversor_B = 9999999.99
    for i in range(1, len(linhas_inversores)):
        dados_inv = linhas_inversores[i].strip().split(",")
        if float(dados_inv[3]) >= (0.85 * potencia_instalada_A) and dados_inv[4] == "Hibrido":
            if float(dados_inv[5]) < menor_custo_inversor_B:
                menor_custo_inversor_B = float(dados_inv[5])
                inv_fab_B, inv_mod_B = dados_inv[1], dados_inv[2]
 
    custo_equipamentos_B = menor_custo_painel_A + menor_custo_inversor_B + custo_baterias_B
    custo_indireto_B = custo_equipamentos_B * 0.35
    custo_total_B = custo_equipamentos_B + custo_indireto_B
 
    print(f"Baterias: {qtd_baterias_B}x {dados_bat[1]} {dados_bat[2]} (R$ {custo_baterias_B:.2f})")
    print(f"VALOR TOTAL (Cenário B): R$ {custo_total_B:.2f}")
