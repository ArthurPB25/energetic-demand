print("\nCADASTRO DE NOVO USUÁRIO\n")

print("Opções de acesso: Entrar / Cadastrar")

acesso = str(input("\nQual tipo de acesso vcê deseja? "))

while acesso == "Entrar":
    print("\nVocê não possui acesso! Tente novamente")
    acesso = str(input("\nQual tipo de acesso vcê deseja? "))

if acesso == "Cadastrar":
    nome = (input("\nDigite seu nome: ")) #Nome
    email = (input("Digite seu e-mail: ")) #usuario_cadastrado@email.com
    senha = (input("Digite uma senha segura: ")) #1234

    print(f"\nAcesso:\nNome: {nome} / E-mail: {email} / Senha: {senha}")
    print("\nCadastro concluido com sucesso e segurança!")