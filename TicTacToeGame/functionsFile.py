#functions to add: create the matrix from 0 to 8, another to pu the x or the the O in the right place
#one to shitch the players(true or false for x)

import os


matrix = [[0,1,2],[3,4,5],[6,7,8]]

def showMatriz(matrix):
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == 'X':
                print("\033[35m|X|\033[0m", end='')  # Pink for X
            elif matrix[i][j] == 'O':
                print("\033[34m|O|\033[0m", end='')  # Purple for O
            else:
                print(f"|{matrix[i][j]}|", end='')
        print()


def vitoriaDiagonais(matrix):

    if matrix[2][2] == matrix[1][1] == matrix[0][0]:
        if matrix[2][2] == 'X':
            print("\033[35mO jogador X venceu\033[0m")
            return 1
        elif matrix[2][2] == 'O':
            print("\033[34mO jogador O venceu\033[0m")
            return 1
    if matrix[2][0] == matrix[1][1] == matrix[0][2]:
        if matrix[2][0] == 'X':
            print("\033[35mO jogador X venceu\033[0m")
            return 1
        elif matrix[2][0] == 'O':
            print("\033[34mO jogador O venceu\033[0m")
            return 1
    return -1

def vitoriaColunas(matrix):
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] in ['X','O']:
            if matrix[0][i] == 'X':
                print("\033[35mO jogador X venceu\033[0m")
                return 1
            elif matrix[0][i] == 'O':
                print("\033[34mO jogador O venceu\033[0m")
                return 1
    return -1

def vitoriaLinhas(matrix):
    for j in matrix:
        if j[0] == j[1] == j[2] and j[0] in ['X', 'O']:
            if j[0] == 'X':
                print("\033[35mO jogador X venceu\033[0m")
                return 1
            elif j[0] == 'O':
                print("\033[34mO jogador O venceu\033[0m")
    return -1 # Se não houver vencedor


def verificarVencer(matrix):
    if vitoriaDiagonais(matrix) == 1 or vitoriaColunas(matrix) == 1 or vitoriaLinhas(matrix) == 1:
        return 1
    else:
        return -1

def verificarEmpate(matrix):
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] in [0,1,2,3,4,5,6,7,8]:
                return -1 #ainda exitem jogadas para fazer
    print("Empate!")
    return 1 #realmente deu empate pois nao existem mais jogadas avaliable


def updateMatrix(matrix, move, player):
    # Calculando a linha e a coluna
    l = move // 3
    c = move % 3

    # Verifica se o espaço ainda está disponível
    if matrix[l][c] == move:
        matrix[l][c] = player  # Atualiza com o símbolo do jogador (X ou O)
        return 1  # Jogada válida
    else:
        return -1  # Jogada inválida (espaço já ocupado)


def askUserIn(turn):
    move = ' '
    if turn % 2 != 0:
        move = int(input("\033[35mX's turn. Input move(0-8): \033[0m"))
        player = 'X'
    else:
         move = int(input("\033[34mO's turn. Input move(0-8): \033[0m"))
         player = 'O'
    turn += 1
    return move,player

def game():
    turn = 1
    while True:
        #os.system('cls')
        showMatriz(matrix)
        move, player = askUserIn(turn)

        if updateMatrix(matrix, move, player) == 1:
            # Verifica vitória ou empate após uma jogada válida
            if verificarVencer(matrix) == 1:
                showMatriz(matrix)  # Mostra a matriz final

                break
            elif verificarEmpate(matrix) == 1:
                showMatriz(matrix)  # Mostra a matriz final
                break

            turn += 1  # Incrementa o turno
        else:
            print("\033[31mEscolha outra jogada\033[m")












