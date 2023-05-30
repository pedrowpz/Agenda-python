def menu():
    voltarMenuPrencipal = 's'
    while voltarMenuPrencipal in 's':

        opcao = input('''
        =========================================================
                            PROJETO AGENDA EM PYTHON
        MENU:
        
        [1]CADASTRAR CONTATO
        [2]LISTAR CONTATO
        [3]DELETAR CONTATO
        [4]BUSCAR CONTATO PELO NOME
        [5]ATUALIZAR CONTATO
        [6]SAIR 
        =========================================================
        ESCOLHA UMA OPÇÃO ACIMA: 
        ''')
        if opcao =="1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao =="3":
            deletarContato()
        elif opcao =="4":
            buscarContatoPeloNome()
        elif opcao =="5":
            atualizarContato()
        elif opcao =="6":
            sair()
        else:
            print('Opção Inválida')
        voltarMenuPrencipal = input("Deseja volta ao menu principal? (s/n) ").lower()


def cadastrarContato():
    idContato = input("Escolha o Id do seu contato: ")
    nome = input("Escolha o nome do seu contato: ")
    telefone = input("Escolha o telefone do seu contato: ")
    email = input("Escreva o email do contato: ")
    try:
        agenda = open("agenda.txt" , "a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso !!!!!')
    except:
        print("Erro na gravação do contato")


def listarContato():
    try:   
        agenda = open("agenda.txt","r")
        for contato in agenda:
            print(contato)
    finally:
        agenda.close()

def deletarContato():
    nomeDeletato = input("Digite o nome para ser deletado:").lower()
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletato not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt","w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listarContato()
    
        

def buscarContatoPeloNome():
    nome = input("Escolha o nome que busca: ").upper
    agenda = open("agenda.txt","r")
    for contato in agenda:
        if nome in contato.split(";")[1]:   
            print(contato)
        if nome not in contato.split(";")[1].upper:
            print("Contato inexistente")
        break
    agenda.close()


def atualizarContato():
    nomeDeletado = input("Digite o nome para ser atualizado: ").lower()
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt","w")
    for i in aux2:
        agenda.write(i)
    idContato = input("Escolha o Id do seu contato atualizado: ")
    nome = input("Escolha o nome do seu contato atualizado: ")
    telefone = input("Escolha o telefone do seu contato atualizado: ")
    email = input("Escreva o email do contato atualizado: ")
    try:
        agenda = open("agenda.txt" , "a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato atualizado com sucesso !!!!!')
    except:
        print("Erro na gravação do contato")



def sair():
    print('Saindo do programa')
    exit()


def main():
    menu()

main()
