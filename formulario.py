def validar_nome(nome):   
    if nome.replace(" ", "").isalpha():
        return True
    return False 
print('Bem vindo a empresa Nexct! A seguir preencha as informações para concorrer a vaga, Boa sorte')
while True:
    nome = input('Digite seu nome completo sem abreviações: ')
    if validar_nome(nome):
        print("Nome válido e cadastrado com sucesso!")
        break
    else:
        print('Tente novamente, apenas letras')
while True:
    idade = str(input('Digite sua idade somente números: '))
    if idade.isdigit():
        break
    else:
        print('Tente novamente, apenas números.')
while True:
    cpf = str(input('Digite seu CPF completo, somente números: '))
    if cpf.isdigit():
        if len(cpf)!=11:
            print('Quantidade de números invalidos, tente novamente. ')
        else:
            print('CPF valido! ')        
            break
    else:
        print('Tente novamente, apenas números.')
        
dif = input('Qual seu diferencial que agregaria na vaga que está concorrendo?: ')
        
motivo = input('Porque deveriamos te contratar?: ')

experiencia = input('Fale breviamente sobre suas experiências profissionais ao longo de sua carreira no mercado de trabalho: ')
            
print('Obrigado por preencher as informações, aguarde o retorno da empresa via email! ')
