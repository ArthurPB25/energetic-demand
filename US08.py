print("\nCÁLCULO DE GASTO EM kWh\n")

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

    listagem_equipamento = []

#<Diferencial do US07>

    consumo_energia_total = 0

#</Diferencial do US07>

    for i in range(qntd_equipamento):
        equipamento = input(f"\nDigite o {i + 1}° equipamento: ")
        potencia = int(input(f"Digite a potência em W do(a) {equipamento}: "))
        uso_diario = int(input(f"Digite o uso diário em horas do(a) {equipamento}: "))

#<Diferencial do US07>

        consumo_energia = (potencia * uso_diario) / 1000
        print(f"\nConsumo de energia diário do equipamento: {consumo_energia:.2f}kWh")

#</Diferencial do US07>

        print(f"\n{equipamento} cadastrado(a) com sucesso!")

#<Diferencial do US07>

        consumo_energia_total += consumo_energia

#</Diferencial do US07>

        listagem_equipamento.append(equipamento)

    print(f"\nEquipamento(s) cadastrado(s):\n")

    for i in range(qntd_equipamento):
        print(listagem_equipamento[i])

#<Diferencial do US07>

    print(f"\nConsumo de energia total dos equipamentos por dia: {consumo_energia_total:.2f}kWh")

#</Diferencial do US07>

permicao_edicao = 1

while permicao_edicao == 1:

    edicao = input("\nDeseja fazer alguma alteração no cadastro dos esquipamentos (s/n)? ")

    if edicao == "s":
        print("\nCorreção no cadastro de equipamento(s):")

        qntd_equipamento = int(input("\nDigite quantos tipos diferentes de equipamento a(s) casa(s) terá(ão): "))

        listagem_equipamento = []

        consumo_energia_total = 0

        for i in range(qntd_equipamento):
            equipamento = input(f"\nDigite o {i + 1}° equipamento: ")
            potencia = int(input(f"Digite a potência em W do(a) {equipamento}: "))
            uso_diario = int(input(f"Digite o uso diário em horas do(a) {equipamento}: "))

#<Diferencial do US07>

            consumo_energia = (potencia * uso_diario) / 1000
            print(f"\nConsumo de energia diário do equipamento: {consumo_energia:.2f}kWh")

#</Diferencial do US07>

            print(f"\n{equipamento} cadastrado(a) com sucesso!")

#<Diferencial do US07>

            consumo_energia_total += consumo_energia

#</Diferencial do US07>

            listagem_equipamento.append(equipamento)

        print(f"\nEquipamento(s) cadastrado(s):\n")

        for i in range(qntd_equipamento):
            print(listagem_equipamento[i])

#<Diferencial do US07>

        print(f"\nConsumo de energia total dos equipamentos por dia: {consumo_energia_total:.2f}kWh")

#</Diferencial do US07>

        print("\nEquipamento(s) atualizado(s) com sucesso!")

    if edicao == "n":
        print("\nFim dos cadastros!")
        break