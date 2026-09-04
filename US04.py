print("\nLISTAGEM DE CASAS\n")

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

#<Diferencial do US03>

    listagem_casas = []

#</Diferencial do US03>

    for i in range(quantidade_casas):
        nome_casa = input(f"\nDigite o nome do cadastro para a {i + 1}ª casa: ")
        print(f"\n{nome_casa} cadastrado(a) com sucesso!")

#<Diferencial do US03>

        listagem_casas.append(nome_casa)

    print("\nCasa(s) cadastrada(s):\n")

    for i in range(quantidade_casas):
        print(listagem_casas[i])

#</Diferencial do US03>