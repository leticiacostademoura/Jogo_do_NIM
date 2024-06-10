def partida ():
    n = int(input("\nQuantas peças?"))
    m = int(input("\nLimite de peças por jogada?"))
    jogador_venceu = 0
    computador_venceu = 0

    if (n % (m + 1) == 0):
        print("\nVocê começa!")
        while(n > 0):
            n -= usuario_escolhe_jogada(n, m)
            if(n > 0):
                if(n > m):
                    print ("\nAgora restam", n, "peças no tabuleiro")
                else:
                    print ("\nAgora resta apenas", n, "peça no tabuleiro")
            else:
                print("\nFim do jogo! Você ganhou!")
                jogador_venceu += 1
                break
    

            n-= computador_escolhe_jogada(n, m)
            if(n > 0):
                if(n > m):
                    print ("\nAgora restam", n, "peças no tabuleiro")
                else:
                    print ("\nAgora resta apenas", n, "peça no tabuleiro")
            else:
                print("\nFim do jogo! O computador ganhou!")
                computador_venceu += 1
                break               

        
    else:
        print("\nComputador começa!")
        while(n > 0):
            n -= computador_escolhe_jogada(n, m) 
            if(n > 0):
                if(n > m):
                    print ("\nAgora restam", n, "peças no tabuleiro")
                else:
                    print ("\nAgora resta apenas", n, "peça no tabuleiro")
            else:
                print("\nFim do jogo! O computador ganhou!")
                computador_venceu += 1
                break               
            
            n -= usuario_escolhe_jogada(n, m)
            if(n > 0):
                if(n > m):
                    print ("\nAgora restam", n, "peças no tabuleiro")
                else:
                    print ("\nAgora resta apenas", n, "peça no tabuleiro")
            else:
                print("\nFim do jogo! Você ganhou!")
                jogador_venceu += 1
                break  

    return jogador_venceu, computador_venceu   

def campeonato():
    rodada = 0
    jogador_total_vitorias = 0
    computador_total_vitorias = 0

    while(rodada < 3):
        print("\n **** Rodada", (rodada + 1), "****")
        jogador_venceu, computador_venceu = partida()
        jogador_total_vitorias += jogador_venceu
        computador_total_vitorias += computador_venceu
        rodada += 1

    print("\n **** Final do campeonato! ****")
    print("\nPlacar: Você ", jogador_total_vitorias, "X", computador_total_vitorias, "Computador")
    
def computador_escolhe_jogada (n, m):
    if (n > m):
        jogada = m
    else:
        jogada = n
    if jogada > 1:
        print("\nO computador tirou", jogada, "peças")
    else:
        print("\nO computador tirou", jogada, "peça")
    return jogada

def usuario_escolhe_jogada (n, m):
    while True:
        pecas_tiradas = int(input("\nQuantas peças você vai tirar?"))
        if (pecas_tiradas > m):
            print("\nOops! Jogada inválida! Tente de novo.")
        else: 
            if (pecas_tiradas == 1):
                print("\nVocê tirou ", pecas_tiradas, "peça")
            else:
                print("\nVocê tirou ", pecas_tiradas, "peças") 
            return pecas_tiradas


opcao = int(input("Bem vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))

if (opcao == 1):
    print("\nVocê escolheu uma partida isolada!")
    partida()
elif(opcao == 2):
    print("\nVocê escolheu um campeonato!")
    campeonato()
else:
    print("\nOpção inválida, tente novamente")







