from main import *
import os
import time

montar_baralho()
RODADA = 1

while RODADA <= 3:  # Ajustado para 2 rodadas
    print(f'Iniciando rodada {RODADA}')
    montar_decks()
    while len(P1_Deck) != 0 and len(P2_Deck) != 0:
        limpar_tela()
        mostrar_mesa()
        escolher_cartas_P1()
        limpar_tela()
        mostrar_mesa()
        escolher_cartas_P2()
        limpar_tela()
        mostrar_mesa()
        passar_decks()

# Após a conclusão da rodada, exibe uma mensagem e aguarda o usuário pressionar uma tecla
limpar_tela()
print(f'Rodada {RODADA} concluída.\nPressione Enter para continuar para a próxima rodada...')
input()  # Aguarda o usuário pressionar Enter
    
RODADA += 1

# Após todas as rodadas, você pode querer calcular a pontuação final
limpar_tela()
print('Hora de contar as cartas e calcular os pontos.')
contagem_P1 = contar_cartas(Mesa_P1)
contagem_P2 = contar_cartas(Mesa_P2)
exibir_contagem(contagem_P1, 1)
exibir_contagem(contagem_P2, 2)

# Calcular a pontuação final
pontos_P1, _ = calcular_pontuacao(contagem_P1, contagem_P2['Maki rolls'])
pontos_P2, _ = calcular_pontuacao(contagem_P2, contagem_P1['Maki rolls'])

PONTOS_P1 += pontos_P1
PONTOS_P2 += pontos_P2

print(f'Pontuação final do Jogador 1: {PONTOS_P1}')
print(f'Pontuação final do Jogador 2: {PONTOS_P2}')
