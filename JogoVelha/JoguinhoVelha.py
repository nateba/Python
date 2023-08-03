from random import randrange


def exibir_tabuleiro(tabuleiro):
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|", end="")
        for coluna in range(3):
            print("   " + str(tabuleiro[linha][coluna]) + "   ", end="|")
        print("\n" + "|       " * 3 + "|")
        print("+-------" * 3, "+", sep="")


def fazer_movimento(tabuleiro):
    ok = False
    while not ok:
        movimento = input("Digite a posição em que deseja jogar (1-9): ")
        ok = len(movimento) == 1 and movimento >= '1' and movimento <= '9'
        if not ok:
            print("Movimento inválido - digite novamente!")
            continue
        movimento = int(movimento) - 1
        linha = movimento // 3
        coluna = movimento % 3
        sinal = tabuleiro[linha][coluna]
        ok = sinal not in ['O', 'X']
        if not ok:
            print("Campo já ocupado - digite novamente!")
            continue
        tabuleiro[linha][coluna] = 'O'


def fazer_lista_de_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ['O', 'X']:
                livres.append((linha, coluna))
    return livres


def vitoria_para(tabuleiro, sgn):
    if sgn == "X":
        quem = 'eu'
    elif sgn == "O":
        quem = 'você'
    else:
        quem = None
    diagonal1 = diagonal2 = True
    for rc in range(3):
        if tabuleiro[rc][0] == sgn and tabuleiro[rc][1] == sgn and tabuleiro[rc][2] == sgn:
            return quem
        if tabuleiro[0][rc] == sgn and tabuleiro[1][rc] == sgn and tabuleiro[2][rc] == sgn:
            return quem
        if tabuleiro[rc][rc] != sgn:
            diagonal1 = False
        if tabuleiro[2 - rc][2 - rc] != sgn:
            diagonal2 = False
    if diagonal1 or diagonal2:
        return quem
    return None


def fazer_movimento_aleatorio(tabuleiro):
    livres = fazer_lista_de_campos_livres(tabuleiro)
    cnt = len(livres)
    if cnt > 0:
        indice = randrange(cnt)
        linha, coluna = livres[indice]
        tabuleiro[linha][coluna] = 'X'


tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = 'X'
livres = fazer_lista_de_campos_livres(tabuleiro)
vez_do_jogador = True
while len(livres):
    exibir_tabuleiro(tabuleiro)
    if vez_do_jogador:
        fazer_movimento(tabuleiro)
        vencedor = vitoria_para(tabuleiro, 'O')
    else:
        fazer_movimento_aleatorio(tabuleiro)
        vencedor = vitoria_para(tabuleiro, 'X')
    if vencedor is not None:
        break
    vez_do_jogador = not vez_do_jogador
    livres = fazer_lista_de_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == 'você':
    print("Você ganhou!")
elif vencedor == 'eu':
    print("Eu venci")
else:
    print("Empate!")