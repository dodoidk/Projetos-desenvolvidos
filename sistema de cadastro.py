usuarios = {}

def cadastrar():
    print("\n=== Cadastro ===")
    email = str(input("Digite seu email: "))
    
    if email in usuarios:
        print("Email já cadastrado!")
        return
    
    senha = str(input("Digite sua senha: "))
    usuarios[email] = senha
    print("Cadastro realizado com sucesso!")

def login():
    print("\n=== Login ===")
    email = str(input("Digite seu email: "))
    senha = str(input("Digite sua senha: "))
    
    if email in usuarios and usuarios[email] == senha:
        print("Login bem-sucedido!")
    else:
        print("Email ou senha incorretos!")

def resetar_senha():
    print("\n=== Resetar Senha ===")
    email = input("Digite seu email: ")
    
    if email in usuarios:
        nova_senha = input("Digite a nova senha: ")
        usuarios[email] = nova_senha
        print("Senha atualizada com sucesso!")
    else:
        print("Email não encontrado!")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Resetar senha")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            resetar_senha()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()