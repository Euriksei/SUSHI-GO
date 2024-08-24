import pygame
import random
import os

Baralho = []
P1_Deck =[]
P2_Deck = []
Mesa_P1 = []
Mesa_P2 = []
Proxima_mao_P1 = []
Proxima_mao_P2 = []
Deck_temp = []
PONTOS_P1 =  0
PONTOS_P2 = 0

class Cartas:
    def __init__(self, card_name):
        self.card_name = card_name

gerar_Cartas = [
    Cartas('Tempura'),
    Cartas('Rolinho 1 Maki'),
    Cartas('Rolinho 2 Maki'),
    Cartas('Rolinho 3 Maki'),
    Cartas('Sashimi'),
    Cartas('Bolinho'),
    Cartas('Nigiri de lula'),
    Cartas('Nigiri de salmão'),
    Cartas('Nigiri de ovo'),
    Cartas('Wasabi'),
    Cartas('Sushi GO'),
    Cartas('Pudim'),
]

# Criar instâncias para cada carta específica
tempura_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Tempura')
maki_1_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Rolinho 1 Maki')
maki_2_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Rolinho 2 Maki')
maki_3_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Rolinho 3 Maki')
sashimi_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Sashimi')
bolinho_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Bolinho')
nigiri_lula_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Nigiri de lula')
nigiri_salmao_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Nigiri de salmão')
nigiri_ovo_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Nigiri de ovo')
wasabi_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Wasabi')
sushi_go_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Sushi GO')
pudim_card = next(carta for carta in gerar_Cartas if carta.card_name == 'Pudim')

# Montagem do baralho com as cartas

def limpar_tela():
    os.system('cls')

def montar_baralho():
    # Dicionário que mapeia cada carta ao número de vezes que ela deve aparecer no baralho
    cartas_quantidades = {
        tempura_card: 14,
        maki_1_card: 6,
        maki_2_card: 12,
        maki_3_card: 8,
        sashimi_card: 14,
        bolinho_card: 14,
        nigiri_lula_card: 5,
        nigiri_salmao_card: 10,
        nigiri_ovo_card: 5,
        wasabi_card: 6,
        sushi_go_card: 4,
        pudim_card: 10,
    }

    # Adicionar as cartas ao baralho
    for carta, quantidade in cartas_quantidades.items():
        Baralho.extend([carta] * quantidade)
    
    limpar_tela()
    print("Baralho pronto\n\n")

def mostrar_baralho():
    for i, carta in enumerate(Baralho):
        print(f"{i+1} - {carta.card_name}")
        
def montar_decks():
    while len(P1_Deck) < 10:
        random_card = random.choice(Baralho)
        P1_Deck.append(random_card)
        Baralho.remove(random_card)

    while len(P2_Deck) < 10:
        random_card = random.choice(Baralho)
        P2_Deck.append(random_card)
        Baralho.remove(random_card)
    
    #limpar_tela()
    print("Decks prontos\n\n")

def mostrar_decks():
    print('Deck do P1')
    print('------')
    for i, carta in enumerate(P1_Deck):
        print(f'{i+1} - {carta.card_name}')
    print('------\n\n')

    print('Deck do P2')
    print('------')
    for i, carta in enumerate(P2_Deck):
        print(f'{i+1} - {carta.card_name}')
    print('------\n\n')

def mao_P1():#funçao temporaria para somente ver a mao do jogador
    print('\nAs cartas do P1 são')
    print('--------')
    for i, carta in enumerate(P1_Deck):
        print(f"{i+1} - {carta.card_name}")
    print('--------\n')

    print('\nAs cartas do P2 são')
    print('--------')
    for i, carta in enumerate(P2_Deck):
        print(f"{i+1} - {carta.card_name}")
    print('--------\n')

def escolher_cartas_P1():
    print('\nAs cartas do P1 são:')
    print('--------')
    for i, carta in enumerate(P1_Deck):
        print(f"{i+1} - {carta.card_name}")
    print('--------\n')
    
    while True:
        try:
            carta_selecionada = int(input('Selecione uma carta (digite o número correspondente): ')) - 1
            if 0 <= carta_selecionada < len(P1_Deck):
                Mesa_P1.append(P1_Deck[carta_selecionada])
                P1_Deck.pop(carta_selecionada)
                Deck_temp.extend(P1_Deck)
                #limpar_tela()
                print("Carta do P1 Selecionada\n\n")
                break
                
            else:
                print('Escolha uma carta válida.')
            
        except (ValueError, IndexError):
            print('Escolha uma carta válida da sua mão.')
      
def escolher_cartas_P2():       
    print('\nAs cartas do P2 são:')
    print('--------')
    for i, carta in enumerate(P2_Deck):
        print(f"{i+1} - {carta.card_name}")
    print('--------\n')
    while True:
        try:
            carta_selecionada = int(input('Selecione uma carta (digite o número correspondente): ')) - 1
            if 0 <= carta_selecionada < len(P2_Deck):
                Mesa_P2.append(P2_Deck[carta_selecionada])
                P2_Deck.pop(carta_selecionada)
                #limpar_tela()
                print("Carta do P2 Selecionada\n\n")

                break
            else:
                print('Escolha uma carta válida.')
            
        except (ValueError, IndexError):
            print('Escolha uma carta válida da sua mão.')

def passar_decks():
    # Adiciona cartas de P2_Deck para P1_Deck e limpa P2_Deck
    P1_Deck.clear()
    P1_Deck.extend(P2_Deck)
    P2_Deck.clear()
    # Adiciona cartas de Deck_temp para P2_Deck e limpa Deck_temp
    P2_Deck.extend(Deck_temp)
    Deck_temp.clear()
    
    print('Decks Passados\n\n')
    
def mostrar_mesa():
    print('Cartas na mesa do P1\n')
    print('------')
    for i, carta in enumerate(Mesa_P1):
        print(f'{i-1} - {carta.card_name}')
    print('------\n\n')
    
    print('Cartas na mesa do P2\n')
    print('------')
    for i, carta in enumerate(Mesa_P2):
        print(f'{i-1} - {carta.card_name}')
    print('------\n')

def contar_cartas(mesa_jogador):# quando usar passar o parametro MesaP1 ou P2
    # Dicionário para armazenar a contagem de cada tipo de carta
    contagem_cartas = {
        'Tempura': 0,
        'Rolinho 1 Maki': 0,
        'Rolinho 2 Maki': 0,
        'Rolinho 3 Maki': 0,
        'Sashimi': 0,
        'Bolinho': 0,
        'Nigiri de lula': 0,
        'Nigiri de salmao': 0,
        'Nigiri de ovo': 0,
        'Wasabi': 0,
        'Pudim': 0,
    }

    # Contar as cartas na mesa do jogador
    for carta in mesa_jogador:
        if carta.card_name in contagem_cartas:
            contagem_cartas[carta.card_name] += 1

    # Calcular o total de maki rolls
    contagem_cartas['Maki rolls'] = (
        contagem_cartas['Rolinho 1 Maki'] +
        contagem_cartas['Rolinho 2 Maki'] +
        contagem_cartas['Rolinho 3 Maki']
    )

    return contagem_cartas

def exibir_contagem(cartas_contagem, jogador):
    print(f'O jogador {jogador} tem:')
    for nome_carta, quantidade in cartas_contagem.items():
        if quantidade > 0:
            print(f'{quantidade} - {nome_carta}')

# # Exemplo de uso para os jogadores 1 e 2
# contagem_P1 = contar_cartas(Mesa_P1)
# exibir_contagem(contagem_P1, 1)

# contagem_P2 = contar_cartas(Mesa_P2)
# exibir_contagem(contagem_P2, 2)

def calcular_pontuacao(contagem_cartas, contagem_makis_outro_jogador):# o argumento é contagem_P1 ou contagem_P2
    pontos = 0
    MAKI= 0
    
    # Pontuação para Tempura (2 Tempuras = 5 pontos)
    if contagem_cartas['Tempura'] >= 2:
        pontos += (contagem_cartas['Tempura'] // 2) * 5
    
    # Pontuação para Sashimi (3 Sashimis = 10 pontos)
    if contagem_cartas['Sashimi'] >= 3:
        pontos += (contagem_cartas['Sashimi'] // 3) * 10
    
    # Pontuação para Bolinho (varia conforme a quantidade)
    if contagem_cartas['Bolinho'] == 1:
        pontos += 1
    elif contagem_cartas['Bolinho'] == 2:
        pontos += 3
    elif contagem_cartas['Bolinho'] == 3:
        pontos += 6
    elif contagem_cartas['Bolinho'] >= 4:
        pontos += 10
    
    # Pontuação para Nigiri (Lula = 3 pontos, Salmão = 2 pontos, Ovo = 1 ponto)
    pontos += contagem_cartas['Nigiri de lula'] * 3
    pontos += contagem_cartas['Nigiri de salmao'] * 2
    pontos += contagem_cartas['Nigiri de ovo'] * 1
    
    # Pontuação para Wasabi (multiplica o próximo Nigiri)
    if contagem_cartas['Wasabi'] > 0:
        # Assume que Wasabi foi usado na melhor Nigiri disponível
        if contagem_cartas['Nigiri de lula'] > 0:
            pontos += 9
            contagem_cartas['Nigiri de lula'] -= 1
        elif contagem_cartas['Nigiri de salmao'] > 0:
            pontos += 6
            contagem_cartas['Nigiri de salmao'] -= 1
        elif contagem_cartas['Nigiri de ovo'] > 0:
            pontos += 3
            contagem_cartas['Nigiri de ovo'] -= 1

    # Contagem total de Makis para o jogador
    total_makis = (contagem_cartas['Rolinho 1 Maki'] * 1 +
                   contagem_cartas['Rolinho 2 Maki'] * 2 +
                   contagem_cartas['Rolinho 3 Maki'] * 3)
    
    # Comparar Makis entre os jogadores para atribuir pontuação
    if total_makis > contagem_makis_outro_jogador:
        pontos += 6  # Jogador com mais Makis ganha 6 pontos
    elif total_makis == contagem_makis_outro_jogador:
        pontos += 3  # Empate, ambos ganham 3 pontos
    
    return pontos, total_makis
    
    # Pontuação para Maki Rolls (não está completo; depende das regras específicas)
    # Exemplo básico: o jogador com mais Maki ganha 6 pontos, o segundo 3 pontos
    # A lógica para comparar os dois jogadores precisa ser adicionada depois

    return pontos

def atualizar_pontuacao():
    global PONTOS_P1, PONTOS_P2
    
    # Contar cartas na mesa dos jogadores
    contagem_P1 = contar_cartas(Mesa_P1)
    contagem_P2 = contar_cartas(Mesa_P2)
    
    # Calcular pontuações
    PONTOS_P1 += calcular_pontuacao(contagem_P1)
    PONTOS_P2 += calcular_pontuacao(contagem_P2)

    print(f'Pontuação do Jogador 1: {PONTOS_P1}')
    print(f'Pontuação do Jogador 2: {PONTOS_P2}')

# Exemplo de uso após as rodadas
# atualizar_pontuacao()

