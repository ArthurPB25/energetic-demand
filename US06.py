print("\nLISTAGEM DE EQUIPAMENTOS DA CASA\n")

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

#<Diferencial do US05>

    listagem_equipamento = []

#</Diferencial do US05>

    for i in range(qntd_equipamento):
        equipamento = input(f"\nDigite o {i + 1}° equipamento: ")
        potencia = int(input(f"Digite a potência em W do(a) {equipamento}: "))
        uso_diario = int(input(f"Digite o uso diário em horas do(a) {equipamento}: "))
        print(f"\n{equipamento} cadastrado(a) com sucesso!")

#<Diferencial do US05>

        listagem_equipamento.append(equipamento)

    print(f"\nEquipamento(s) cadastrado(s):\n")

    for i in range(qntd_equipamento):
        print(listagem_equipamento[i])

#</Diferencial do US05>