from idlelib.colorizer import prog_group_name_to_tag

print("\nCálculo Energético\n")

chuveiro = int(input("Quantos chuveiros serão instalados? "))

while chuveiro <= 0:
    print("\nDigite um valor válido\n")
    chuveiro = int(input("Quantos chuveiros serão instalados? "))

print()

potencia_chuveiro = int(input("Qual a potência do(s) chuveiro(s)? "))

while potencia_chuveiro <= 0:
    print("\nDigite um valor válido\n")
    potencia_chuveiro = int(input("Qual a potência do(s) chuveiro(s)? "))

print()

media_horas_chuveiro = float(input("Qual a média de horas usadas do chuveiro por dia? "))

while media_horas_chuveiro <= 0:
    print("\nDigite um valor válido\n")
    media_horas_chuveiro = float(input("Qual a média de horas usadas do(s) chuveiro(s) por dia? "))

print()

ar_condicionado = int(input("Quantos ar-condicionados serão instalados? "))

while ar_condicionado <= 0:
    print("\nDigite um valor válido\n")
    ar_condicionado = int(input("Quantos ar-condicionados serão instalados? "))

print()

potencia_ar_condicionado = int(input("Qual a potência do(s) ar-condicionado(s)? "))

while potencia_ar_condicionado <= 0:
    print("\nDigite um valor válido\n")
    potencia_ar_condicionado = int(input("Qual a potência do(s) ar-condicionado(s)? "))

print()

media_horas_ar_condicionado = float(input("Qual a média de horas usadas do(s) ar_condicionado(s) por dia? "))

while media_horas_ar_condicionado <= 0:
    print("\nDigite um valor válido\n")
    media_horas_ar_condicionado = float(input("Qual a média de horas usadas do(s) ar_condicionado(s) por dia? "))

print()

geladeira = int(input("Quantas geladeiras serão instaladas? "))

while geladeira <= 0:
    print("\nDigite um valor válido\n")
    geladeira = int(input("Quantas geladeiras serão instaladas? "))

print()

potencia_geladeira = int(input("Qual a potência da(s) geladeira(s)? "))

while potencia_geladeira <= 0:
    print("\nDigite um valor válido\n")
    potencia_geladeira = int(input("Qual a potência da(s) geladeira(s)? "))

print()

media_horas_geladeira = float(input("Qual a média de horas usadas da(s) geladeira(s) por dia? "))

while media_horas_geladeira <= 0:
    print("\nDigite um valor válido\n")
    media_horas_geladeira = float(input("Qual a média de horas usadas da(s) geladeira(s) por dia? "))

print()

micro_ondas = int(input("Quantos micro-ondas serão instalados? "))

while micro_ondas <= 0:
    print("\nDigite um valor válido\n")
    micro_ondas = int(input("Quantos micro-ondas serão instalados? "))

print()

potencia_micro_ondas = int(input("Qual a potência do(s) micro_ondas? "))

while potencia_micro_ondas <= 0:
    print("\nDigite um valor válido\n")
    potencia_micro_ondas = int(input("Qual a potência do(s) micro_ondas? "))

print()

media_horas_micro_ondas = float(input("Qual a média de horas usadas do(s) micro-ondas por dia? "))

while media_horas_micro_ondas <= 0:
    print("\nDigite um valor válido\n")
    media_horas_micro_ondas = float(input("Qual a média de horas usadas do(s) micro-ondas por dia? "))

print()

fogao = int(input("Quantos fogões serão instalados? "))

while fogao <= 0:
    print("\nDigite um valor válido\n")
    fogao = int(input("Quantos fogões serão instalados? "))

print()

potencia_fogao = int(input("Qual a potência do(s) fogão(ões)? "))

while potencia_fogao <= 0:
    print("\nDigite um valor válido\n")
    potencia_fogao = int(input("Qual a potência do(s) fogão(ões)? "))

print()

media_horas_fogao = float(input("Qual a média de horas usadas do(s) fogão(ões) por dia? "))

while media_horas_fogao <= 0:
    print("\nDigite um valor válido\n")
    media_horas_fogao = float(input("Qual a média de horas usadas do(s) fogão(ões) por dia? "))

print()

maquina_lavar = int(input("Quantas máquinas de lavar serão instaladas? "))

while maquina_lavar <= 0:
    print("\nDigite um valor válido\n")
    maquina_lavar = int(input("Quantas máquinas de lavar serão instaladas? "))

print()

potencia_maquina_lavar = int(input("Qual a potência da(s) máquina(s) de lavar? "))

while potencia_maquina_lavar <= 0:
    print("\nDigite um valor válido\n")
    potencia_maquina_lavar = int(input("Qual a potência da(s) máquina(s) de lavar? "))

print()

media_horas_maquina_lavar = float(input("Qual a média de horas usadas da(s) máquina(s) de lavar por dia? "))

while media_horas_maquina_lavar <= 0:
    print("\nDigite um valor válido\n")
    media_horas_maquina_lavar = float(input("Qual a média de horas usadas da(s) máquina(s) de lavar por dia? "))

print()

televisao = int(input("Quantas televisões serão instaladas? "))

while televisao <= 0:
    print("\nDigite um valor válido\n")
    televisao = int(input("Quantas televisões serão instaladas? "))

print()

potencia_televisao = int(input("Qual a potência da(s) televisão(ões)? "))

while potencia_televisao <= 0:
    print("\nDigite um valor válido\n")
    potencia_televisao = int(input("Qual a potência da(s) televisão(ões)? "))

print()

media_horas_televisao = float(input("Qual a média de horas usadas da(s) televisão(ões) por dia? "))

while media_horas_televisao <= 0:
    print("\nDigite um valor válido\n")
    media_horas_televisao = float(input("Qual a média de horas usadas da(s) televisão(ões) por dia? "))

print()

computador = int(input("Quantos computadores serão instalados? "))

while computador <= 0:
    print("\nDigite um valor válido\n")
    computador = int(input("Quantos computadores serão instalados? "))

print()

potencia_computador = int(input("Qual a potência do(s) computador(es)? "))

while potencia_computador <= 0:
    print("\nDigite um valor válido\n")
    potencia_computador = int(input("Qual a potência do(s) computador(es)? "))

print()

media_horas_computador = float(input("Qual a média de horas usadas do(s) computador(res) por dia? "))

while media_horas_computador <= 0:
    print("\nDigite um valor válido\n")
    media_horas_computador = float(input("Qual a média de horas usadas do(s) computador(res) por dia? "))

print()

lampadas = int(input("Quantas lâmpadas serão instaladas? "))

while lampadas <= 0:
    print("\nDigite um valor válido\n")
    lampadas = int(input("Quantas lâmpadas serão instaladas? "))

print()

potencia_lampadas = int(input("Qual a potência da(s) lâmpadas(s)? "))

while potencia_lampadas <= 0:
    print("\nDigite um valor válido\n")
    potencia_lampadas = int(input("Qual a potência da(s) lâmpadas(s)? "))

print()

media_horas_lampadas = float(input("Qual a média de horas usadas da(s) lâmpada(s) por dia? "))

while media_horas_lampadas <= 0:
    print("\nDigite um valor válido\n")
    media_horas_lampadas = float(input("Qual a média de horas usadas da(s) lâmpada(s) por dia? "))

potencia_geral_chuveiro = (potencia_chuveiro / 1000) * media_horas_chuveiro

potencia_geral_ar_condicionado = (potencia_ar_condicionado / 1000) * media_horas_ar_condicionado

potencia_geral_geladeira = (potencia_geladeira / 1000) * media_horas_geladeira

potencia_geral_micro_ondas = (potencia_micro_ondas / 1000) * media_horas_micro_ondas

potencia_geral_fogao = (potencia_fogao / 1000) * media_horas_fogao

potencia_geral_maquina_lavar = maquina_lavar * (potencia_maquina_lavar / 1000) * media_horas_maquina_lavar

potencia_geral_televisao = (potencia_televisao / 1000) * media_horas_televisao

potencia_geral_computador = (potencia_computador / 1000) * media_horas_computador

potencia_geral_lampadas = (potencia_lampadas / 1000) * media_horas_lampadas

print(50 * "-")

print("RELATÓRIO")

print(50 * "-")

print("\nChuveiro:\n")

print(f"Quantidade: {chuveiro}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_chuveiro}")
print()
print(f"Por mês: {potencia_geral_chuveiro * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_chuveiro * 0.8}")
print()
print(f"Por mês: R${potencia_geral_chuveiro * 0.8 * 30}")

print(50 * "-")

print("\nAr-condicionado:\n")

print(f"Quantidade: {ar_condicionado}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_ar_condicionado}")
print()
print(f"Por mês: {potencia_geral_ar_condicionado * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_ar_condicionado * 0.8}")
print()
print(f"Por mês: R${potencia_geral_ar_condicionado * 0.8 * 30}")

print(50 * "-")

print("\nGeladeira:\n")

print(f"Quantidade: {geladeira}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_geladeira}")
print()
print(f"Por mês: {potencia_geral_geladeira * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_geladeira * 0.8}")
print()
print(f"Por mês: R${potencia_geral_geladeira * 0.8 * 30}")

print(50 * "-")

print("\nMicro-ondas:\n")

print(f"Quantidade: {micro_ondas}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_micro_ondas}")
print()
print(f"Por mês: {potencia_geral_micro_ondas * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_micro_ondas * 0.8}")
print()
print(f"Por mês: R${potencia_geral_micro_ondas * 0.8 * 30}")

print(50 * "-")

print("\nFogão:\n")

print(f"Quantidade: {fogao}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_fogao}")
print()
print(f"Por mês: {potencia_geral_fogao * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_fogao * 0.8}")
print()
print(f"Por mês: R${potencia_geral_fogao * 0.8 * 30}")

print(50 * "-")

print("\nMáquina de lavar:\n")

print(f"Quantidade: {maquina_lavar}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_maquina_lavar}")
print()
print(f"Por mês: {potencia_geral_maquina_lavar * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_maquina_lavar * 0.8}")
print()
print(f"Por mês: R${potencia_geral_maquina_lavar * 0.8 * 30}")

print(50 * "-")

print("\nTelevisão:\n")

print(f"Quantidade: {televisao}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_televisao}")
print()
print(f"Por mês: {potencia_geral_televisao * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_televisao * 0.8}")
print()
print(f"Por mês: R${potencia_geral_televisao * 0.8 * 30}")

print(50 * "-")

print("\nComputador:\n")

print(f"Quantidade: {computador}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_computador}")
print()
print(f"Por mês: {potencia_geral_computador * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_computador * 0.8}")
print()
print(f"Por mês: R${potencia_geral_computador * 0.8 * 30}")

print(50 * "-")

print("\nLampadas:\n")

print(f"Quantidade: {lampadas}")
print()
print(f"Média de energia em KWh gasta por dia: {potencia_geral_lampadas}")
print()
print(f"Por mês: {potencia_geral_lampadas * 30}")
print()
print(f"Custo por dia: R$ {potencia_geral_lampadas * 0.8}")
print()
print(f"Por mês: R${potencia_geral_lampadas * 0.8 * 30}")