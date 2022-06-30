import random

def jogar(P_win, M_win):

    print("\n \n \n Escolha sua jogada: \n")
    jogada = int(input("1 - Pedra\n2 - Papel\n3 - Tesoura\n"))

    if jogada == 1:
        Player = "Pedra"
    elif jogada == 2:
        Player = "Papel"
    elif jogada == 3:
        Player = "Tesoura"
    else:
        print("Erro!")
    
        
    jogadas = ["Pedra", "Papel", "Tesoura"]
    Maquina = random.choice( jogadas )
    
    print( Player + " x " + Maquina )

    if ( Player == "Pedra" and Maquina == "Tesoura") or ( Player == "Papel" and Maquina == "Pedra") or ( Player == "Tesoura" and Maquina == "Papel"):
        P_win = P_win + 1
        print("\nPonto para o Jogador!")
        input("(presione enter para continuar)")
    elif ( Maquina == "Pedra" and Player == "Tesoura") or ( Maquina == "Papel" and Player == "Pedra") or ( Maquina == "Tesoura" and Player == "Papel"):
        M_win = M_win + 1
        print("\nPonto para a Maquina!")
        input("(presione enter para continuar)")
    else:
        print("\nEmpate!")
        input("(presione enter para continuar)")

    if P_win == 2:
        print("! ! ! V I T Ó R I A ! ! !\n \n \n \n")
        input("(presione enter para continuar)")
        menu()
    elif M_win == 2:
        print("* * * D E R R O T A * * *\n \n \n \n")
        input("(presione enter para continuar)")
        menu()
    else:
        jogar(P_win, M_win)

def menu():
    P_win = 0
    M_win = 0
    op = int(input("1 - JOGAR\n2 - SAIR \n"))

    if op == 1:
        jogar(P_win, M_win)
    elif op == 2:
        print("Até Logo!")
    else:
        print("Erro!")
        menu()

menu()