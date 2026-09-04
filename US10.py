print("\nRANKING DE CONSUMO\n")

#Nome = Nome
#E-mail = usuario_cadastrado@email.com
#Senha = 1234

nome_cadastrado = "Nome"
email_cadastrado = "usuario_cadastrado@email.com"
senha_cadastrada = "1234"

nome = input("Digite seu nome: ")
email = input("Digite o seu e-mail: ")
senha = input("Digite sua senha: ")

while nome_cadastrado != nome or email_cadastrado != email or senha_cadastrada != senha:
    print("\nDados de entrada incorretos! Tente novamente\n")
    nome = input("Digite seu nome: ")
    email = input("Digite o seu e-mail: ")
    senha = input("Digite sua senha: ")

if nome_cadastrado == nome and email_cadastrado == email and senha_cadastrada == senha:
    print("\nLogado com sucesso!")
    print("\nSistema de cadastro da casa:")

    quantidade_casas = int(input("\nDigite quantas casas deseja cadastrar: "))

    listagem_casas = []

    for i in range(quantidade_casas):
        nome_casa = input(f"\nDigite o nome do cadastro para a {i + 1}ª casa: ")
        print(f"\n{nome_casa} cadastrado(a) com sucesso!")
        listagem_casas.append(nome_casa)

    print("\nCasa(s) cadastrada(s):\n")

    for i in range(quantidade_casas):
        print(listagem_casas[i])

    print("\nCadastro de equipamento(s):")

    qntd_equipamento = int(input("\nDigite quantos tipos diferentes de equipamento a(s) casa(s) terá(ão): "))
    tarifa_energia = float(input("Digite a tarifa de energia da sua região: "))

    listagem_equipamento = []

#<Diferencial do US09>

    listagem_consumo = []

#</Diferencial do US09>

    consumo_energia_total = 0
    gasto_consumo_energia_total = 0

    for i in range(qntd_equipamento):
        equipamento = input(f"\nDigite o {i + 1}° equipamento: ")
        potencia = int(input(f"Digite a potência em W do(a) {equipamento}: "))
        uso_diario = int(input(f"Digite o uso diário em horas do(a) {equipamento}: "))
        consumo_energia = (potencia * uso_diario) / 1000
        gasto_consumo_energia = consumo_energia * tarifa_energia
        print(f"\nConsumo de energia diário do equipamento: {consumo_energia:.2f}kWh")
        print(f"\nGasto de energia diário do equipamento: R$ {gasto_consumo_energia:.2f}")
        print(f"\n{equipamento} cadastrado(a) com sucesso!")
        consumo_energia_total += consumo_energia
        gasto_consumo_energia_total += gasto_consumo_energia
        listagem_equipamento.append(equipamento)

#<Diferencial do US09>

        listagem_consumo.append(consumo_energia)

#</Diferencial do US09>

    print(f"\nEquipamento(s) cadastrado(s):\n")

    for i in range(qntd_equipamento):
        print(listagem_equipamento[i])

    print(f"\nConsumo de energia total dos equipamentos por dia: {consumo_energia_total:.2f}kWh")
    print(f"\nGasto de energia total dos equipamentos por dia: R$ {gasto_consumo_energia_total:.2f}")
    print(f"\nGasto de energia total dos esquipamentos por mês: R$ {gasto_consumo_energia_total * 30:.2f}")

#<Diferencial do US09>

    print("\nRanking de Consumo (Do maior para o menor):\n")

    for i in range(qntd_equipamento):
        for j in range(i + 1, qntd_equipamento):
            if listagem_consumo[i] < listagem_consumo[j]:
                aux_consumo = listagem_consumo[i]
                listagem_consumo[i] = listagem_consumo[j]
                listagem_consumo[j] = aux_consumo

                aux_equipamento = listagem_equipamento[i]
                listagem_equipamento[i] = listagem_equipamento[j]
                listagem_equipamento[j] = aux_equipamento

    for i in range(qntd_equipamento):
        print(f"{i + 1}º Lugar - {listagem_equipamento[i]}: {listagem_consumo[i]:.2f}kWh")

#</Diferencial do US09>

permicao_edicao = 1

while permicao_edicao == 1:

    edicao = input("\nDeseja fazer alguma alteração no cadastro dos esquipamentos (s/n)? ")

    if edicao == "s":
        print("\nCorreção no cadastro de equipamento(s):")

        qntd_equipamento = int(input("\nDigite quantos tipos diferentes de equipamento a(s) casa(s) terá(ão): "))
        tarifa_energia = float(input("Digite a tarifa de energia da sua região: "))

        listagem_equipamento = []

#<Diferencial do US09>

        listagem_consumo = []

#</Diferencial do US09>

        consumo_energia_total = 0
        gasto_consumo_energia_total = 0

        for i in range(qntd_equipamento):
            equipamento = input(f"\nDigite o {i + 1}° equipamento: ")
            potencia = int(input(f"Digite a potência em W do(a) {equipamento}: "))
            uso_diario = int(input(f"Digite o uso diário em horas do(a) {equipamento}: "))
            consumo_energia = (potencia * uso_diario) / 1000
            gasto_consumo_energia = consumo_energia * tarifa_energia
            print(f"\nConsumo de energia diário do equipamento: {consumo_energia:.2f}kWh")
            print(f"\nGasto de energia diário do equipamento: R$ {gasto_consumo_energia:.2f}")
            print(f"\n{equipamento} cadastrado(a) com sucesso!")
            consumo_energia_total += consumo_energia
            gasto_consumo_energia_total += gasto_consumo_energia
            listagem_equipamento.append(equipamento)

#<Diferencial do US09>

            listagem_consumo.append(consumo_energia)

#</Diferencial do US09>

        print(f"\nEquipamento(s) cadastrado(s):\n")

        for i in range(qntd_equipamento):
            print(listagem_equipamento[i])

        print(f"\nConsumo de energia total dos equipamentos por dia: {consumo_energia_total:.2f}kWh")
        print(f"\nGasto de energia total dos equipamentos por dia: R$ {gasto_consumo_energia_total:.2f}")
        print(f"\nGasto de energia total dos esquipamentos por mês: R$ {gasto_consumo_energia_total * 30:.2f}")

#<Diferencial do US09>

        print("\nRanking de Consumo (Do maior para o menor):\n")

        for i in range(qntd_equipamento):
            for j in range(i + 1, qntd_equipamento):
                if listagem_consumo[i] < listagem_consumo[j]:
                    aux_consumo = listagem_consumo[i]
                    listagem_consumo[i] = listagem_consumo[j]
                    listagem_consumo[j] = aux_consumo

                    aux_equipamento = listagem_equipamento[i]
                    listagem_equipamento[i] = listagem_equipamento[j]
                    listagem_equipamento[j] = aux_equipamento

        for i in range(qntd_equipamento):
            print(f"{i + 1}º Lugar - {listagem_equipamento[i]}: {listagem_consumo[i]:.2f}kWh")

#</Diferencial do US09>

        print("\nEquipamento(s) atualizado(s) com sucesso!")

    if edicao == "n":
        print("\nFim dos cadastros!")
        break