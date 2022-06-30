#Função para recolher as opções do usuario

def obtem_opcao_usuario(i):
    match i:
        case 1:
            opcao = int(input("Selecione o Tipo do pokemon: \n1-Água       2-Planta     3-Fogo  \n4-Pedra      5-Elétrico   6-Voador  \n7-Normal     8-Psíquico   9-Fantasma\n10-Terrestre 11-Aço       12-Venenoso\n13-Dragão    14-Fada      15-Noturno \n16-Lutador   17-Inseto    18-Gelo \n"))
            return(opcao)

        case 2:
            opcao = int(input("Selecione, caso tenha, o Tipo Secundario do pokemon: \n0- Puro\n1-Água       2-Planta     3-Fogo  \n4-Pedra      5-Elétrico   6-Voador  \n7-Normal     8-Psíquico   9-Fantasma\n10-Terrestre 11-Aço       12-Venenoso\n13-Dragão    14-Fada      15-Noturno \n16-Lutador   17-Inseto    18-Gelo \n"))
            return(opcao)

        case 3:
            opcao = int(input("Selecione o atributo a ser alterado: \n1-Nome      2-Tipagem   3-Tipagem Sec. \n4-Altura    5-Peso      6-Habilidade\n7-Evolucao\n"))
            return(opcao)

        case 4:
            opcao = int(input("1- SIM \n2- NÃO\n"))
            return(opcao)

        case 5: 
            opcao = int(input("1-Código    2-Pokemon   3-Tipo\n"))
            return(opcao)
        case 0:
            opcao = int(input("Selecione uma opção: \n1- Listar Pokedex \n2- Registrar Pokemon \n3- Alterar Pokemon\n4- Excluir Pokemon\n5- Buscar\n6- Sair\n"))
            return(opcao)


#Função para selecionar Tipagem

def selecionar_tipagem(i):

    op = obtem_opcao_usuario(i)
    if op >= 19:
        print("ERRO! Atributo não encontrado!")
        selecionar_tipagem(i) 

    match op:
        case 0:
            return "Puro"
        case 1:
            return "Água"
        case 2:
            return "Planta"
        case 3:
            return "Fogo"
        case 4:
            return "Pedra"
        case 5:
            return "Elétrico"
        case 6:
            return "Voador"
        case 7:
            return"Normal"
        case 8:
            return "Psíquico"
        case 9:
            return"Fantasma"
        case 10:
            return "Terrestre"
        case 11:
            return "Aço"
        case 12:
            return "Venenoso"
        case 13:
            return "Dragão"
        case 15:
            return "Fada"
        case 16:
            return "Lutador"
        case 17:
            return "Inseto"
        case 18:
            return "Gelo"


#Função para apresentar dados de apenas um pokemon

def aprensentar_dados (pokedex : list, i):
    registro = pokedex[i]
    (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao) = registro
    # código
    print("{:4d}".format(codigo), end="")

    # nome
    if len(nome) > 15:
        nome = nome[:15] + "..."
    else:
        nome = nome.ljust(15)
        print("  " + nome, end="")

    # tipagem1
    if len(tipagem1) > 13:
       tipagem1 = tipagem1[:13] + "..."
    else:
        tipagem1 = tipagem1.ljust(13)
        print(" " + tipagem1, end="")

    # tipagem2
    if len(tipagem2) > 13:
        tipagem2 = tipagem2[:13] + "..."
    else:
        tipagem2 = tipagem2.ljust(13)
        print(" " + tipagem2, end="")

    # altura
    if altura >= 100:
        print(" {:.1f}".format(altura), end="")
    elif altura >= 10:
        print(" {:.2f}".format(altura), end="")
    else:
        print(" {:.3f}".format(altura), end="")

    # peso
    if peso >= 100:
        print(" {:.1f}".format(peso), end="")
    elif peso >= 10:
        print(" {:.2f}".format(peso), end="")
    else:
        print(" {:.3f}".format(peso), end="")

    # habilidade
    if len(habilidade) > 15:
        habilidade = habilidade[:15] + "..."
    else:
        habilidade = habilidade.ljust(15)
        print("  " + habilidade, end="")

    # evolucao
    if evolucao == None:
        print("  Sem evolução\n")
    else:
        if len(evolucao) > 15:
            evolucao = evolucao[:15] + "..."
        else:
            evolucao = evolucao.ljust(15)
            print("  " + evolucao, end="\n")
    return


#Função para listar todos pokemon

def lista_dados(pokedex: list):
    print("Cód.  Nome            Tipagem Prim. Tipagem Secn. Alt.  Peso   Habilidade       Evolução       ")
    print("----  --------------- ------------- ------------- ----- -----  ---------------  ---------------")
    for i in range(len(pokedex)):
        (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao) = pokedex[i]
        # código
        print("{:4d}".format(codigo), end="")

        # nome
        if len(nome) > 15:
            nome = nome[:15] + "..."
        else:
            nome = nome.ljust(15)
        
        print("  " + nome, end="")

        # tipagem1
        if len(tipagem1) > 13:
            tipagem1 = tipagem1[:13] + "..."
        else:
            tipagem1 = tipagem1.ljust(13)
        print(" " + tipagem1, end="")

        # tipagem2
        if len(tipagem2) > 13:
            tipagem2 = tipagem2[:13] + "..."
        else:
            tipagem2 = tipagem2.ljust(13)
        print(" " + tipagem2, end="")

        # altura
        if altura >= 100:
            print(" {:.1f}".format(altura), end="")
        elif altura >= 10:
            print(" {:.2f}".format(altura), end="")
        else:
            print(" {:.3f}".format(altura), end="")

        # peso
        if peso >= 100:
            print(" {:.1f}".format(peso), end="")
        elif peso >= 10:
            print(" {:.2f}".format(peso), end="")
        else:
            print(" {:.3f}".format(peso), end="")

        # habilidade
        if len(habilidade) > 15:
            habilidade = habilidade[:15] + "..."
        else:
            habilidade = habilidade.ljust(15)
        print("  " + habilidade, end="")

        # evolucao
        if evolucao == None:
            print("  Sem evolução\n")
        else:
            if len(evolucao) > 15:
                evolucao = evolucao[:15] + "..."
            else:
                evolucao = evolucao.ljust(15)
            print("  " + evolucao, end="\n")

    input(print("\n \n \n \n(Presione ENTER para continuar)"))


#Função para adicionar pokemon

def novo_registro(pokedex : list): 


    codigo = int(input("Digite o código do pokemon na Pokedex: "))
    for i in range(len(pokedex)):
        registro = pokedex[i - 1]
        (cod,_,_,_,_,_,_,_) = registro
        if codigo == cod:
            print("Ops! Parece que você já encontrou esse pokemon...\nVocê pode editá-lo ou excluí-lo para registrar um novo pokemon.")
            return

    nome = input("Digite o nome do pokemon: ")

    j = 1
    tipagem1 = selecionar_tipagem(j)

    j = 2
    tipagem2 = selecionar_tipagem(j)

    altura = float(input("Digite a altura do pokemon: "))

    peso = float(input("Digite o peso do pokemon: "))

    habilidade = input("Digite a habilidade do pokemon: ")

    ev = input("O pokemon tem evolução? (s/n)")

    if ev == "s" or ev == "S":
        evolucao = input("Digite, caso tenha, a evolução do pokemon: ")
    elif ev == "n" or ev == "N":
        evolucao = None

    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
    pokedex.append(registro)
    print(" Pokemon adicionado a pokedex.")
    input(print("\n \n \n \n(Presione ENTER para continuar)"))
    list.sort(pokedex)


#Função para editar registros

def alterar_registro(pokedex :list):

    cod = int(input("Digite o código do Pokemon a ser modificado: "))

    for i in range(len(pokedex)):
        registro = pokedex[i]

        (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao) = registro 

        if codigo == cod:
            print(f"Deseja alterear o registro {nome}?")
            j=4
            op = obtem_opcao_usuario(j)
            if op == 2:
                input(print("\n \n \n \n(Presione ENTER para continuar)"))
                return menu()
            
            j=3
            op = obtem_opcao_usuario(j)
            if op == 0 or op >= 8:
                print("Ops! Atributo não encontrado!")
                alterar_registro(pokedex) 

            match op:
                case 1:
                    nome = input("Digite o nome do pokemon: ")
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
                case 2:
                    j = 1
                    tipagem1 = selecionar_tipagem(j)
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
                case 3:
                    j = 2
                    tipagem2 = selecionar_tipagem(j)
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
                case 4:
                    altura = float(input("Digite a altura do pokemon: "))
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
                case 5:
                    peso = float(input("Digite a altura do pokemon: "))
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
                case 6:
                    habilidade = input("Digite a habilidade do pokemon: ")
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
                case 7:
                    ev = input("O pokemon tem evolução? (s/n)")
                    if ev == "s" or ev == "S":
                        evolucao = input("Digite a evolução do pokemon: ")
                    elif ev == "n" or ev == "N":
                        evolucao = None
                    registro = (codigo, nome, tipagem1 , tipagem2 , altura, peso, habilidade, evolucao)
                    pokedex[i] = registro
                    print("Pokemon alterado com sucesso!")
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return
        
    print("Ops! Você ainda não encontrou este pokemon.")
    input(print("\n \n \n \n(Presione ENTER para continuar)"))
    return


#Função de exclusão de registros

def excluir_registro(pokedex : list):

    cod = int(input("Digite o código do Pokemon a ser excluido: "))
    for i in range(len(pokedex)):

        registro = pokedex[i]
        (codigo,nome,_,_,_,_,_,_) = registro 

        if codigo == cod:
            
            print(f"Deseja excluir o registro {nome}?")
            j=4
            op = obtem_opcao_usuario(j)
            
            if op == 2:
                input(print("\n \n \n \n(Presione ENTER para continuar)"))
                return menu()
            
            pokedex.remove(pokedex[i])
            print("Pokemon excluido com exito!")
            input(print("\n \n \n \n(Presione ENTER para continuar)"))
            return menu()
    print("Ops! Você ainda não encontrou este pokemon.")
    input(print("\n \n \n \n(Presione ENTER para continuar)"))
    return menu()


#Funções de busca 

def buscar(pokedex : list):

    print("Pelo que deseja procurar?")
    j = 5
    op = obtem_opcao_usuario(j)
    if op < 1 or op > 3:
        print("Ops! Opção não encontrada!")
        input(print("\n \n \n \n(Presione ENTER para continuar)"))
        return

    
    match op:
        case 1:
            cod = int(input("Digite o Código a ser buscado.\n"))
            for i in range(len(pokedex)):
                registro = pokedex[i]
                (codigo,nome,_,_,_,_,_,_) = registro 
                if codigo == cod:
                    print("Cód.  Nome            Tipagem Prim. Tipagem Secn. Alt.  Peso   Habilidade       Evolução       ")
                    print("----  --------------- ------------- ------------- ----- -----  ---------------  ---------------")
                    aprensentar_dados(pokedex, i)
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return

            print("Ops! Você ainda não encontrou este pokemon.")
            input(print("\n \n \n \n(Presione ENTER para continuar)"))
            return menu()
            
        case 2:
            nome_b = (input("Digite o Pokemon a ser buscado.\n"))
            print("Cód.  Nome            Tipagem Prim. Tipagem Secn. Alt.  Peso   Habilidade       Evolução       ")
            print("----  --------------- ------------- ------------- ----- -----  ---------------  ---------------")
            for i in range(len(pokedex)):
                registro = pokedex[i]
                (codigo,nome,_,_,_,_,_,ev) = registro 
                if nome_b == nome:                 
                    aprensentar_dados(pokedex, i)
                    input(print("\n \n \n \n(Presione ENTER para continuar)"))
                    return(menu)
        
                        
            print("Ops! Você ainda não encontrou este pokemon.")
            input(print("\n \n \n \n(Presione ENTER para continuar)"))
            return menu()
        case 3:
            tipo_b = (input("Digite o tipo a ser buscado.\n"))
            cont = 0
            print("Cód.  Nome            Tipagem Prim. Tipagem Secn. Alt.  Peso   Habilidade       Evolução       ")
            print("----  --------------- ------------- ------------- ----- -----  ---------------  ---------------")
            for i in range(len(pokedex)):
                registro = pokedex[i]
                (cod,_,tipo,tipos,_,_,_,_) = registro 
                if tipo_b == tipo or tipo_b == tipos:
                    aprensentar_dados(pokedex, i)
                    cont = cont + 1
            if cont == 0:
                print("Ops! Parece que você ainda não encontrou pokemons desse tipo.")
            input(print("\n \n \n \n(Presione ENTER para continuar)"))
            return


#Menu Principal
def menu():

    j = 0
    op = obtem_opcao_usuario(j)
    while op != 6:
        match op:
            case 1:
                lista_dados(Pokedex)
            case 2:
                novo_registro(Pokedex)
            case 3:
                alterar_registro(Pokedex)
            case 4:
                excluir_registro(Pokedex)
            case 5: 
                buscar(Pokedex)
            case 6:
                return
        op = obtem_opcao_usuario(j)
    print("\n\n Até logo!\n\n")



#Registros iniciais
Pokedex = [(1, "Bulbasaur", "Planta", "Puro", 0.7, 6.9, "Overgrow", "Ivysaur"),
            (2, "Ivysaur", "Planta", "Puro", 1.0, 13.00, "Overgrow", "Venusaur"),
            (3, "Venasaur", "Planta", "Puro", 2.0, 100.0, "Overgrow", None),
            (4, "Charmander", "Fogo", "Puro", 0.6, 8.5, "Blaze", "Charmeleon"),
            (5, "Charmeleon", "Fogo", "Puro", 1.1, 19.00, "Blaze", "Charizard"),
            (6, "Charizard", "Fogo", "Voador", 1.7, 90.5, "Blaze", None),
            (7, "Squirtle", "Água", "Puro", 0.5, 9.0, "Torrent", "Wartotle"),
            (8, "Wartotle", "Água", "Puro", 1.0, 22.5, "Torrent", "Blastoise"),
            (9, "Blastoise", "Água", "Puro", 1.6, 85.5, "Torrent", None)]

print("Olá, bem vindo a sua pokedex!\nAqui você encontra os dados dos pokemon que você encontrar durante sua jornada")
print("Já estão registrados os três iniciais, dos quais você escolheu seu primeiro pokemon...\n")
input(print("Boa sorte, na sua jornada!\n(Presione ENTER para continuar)"))
menu()
