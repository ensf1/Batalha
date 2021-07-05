from random import randint
from icecream import ic
#decide quem joga primeiro
proximo_a_jogar = 0 # randint(0, 1)
jogadores = []

def dano_fisico(atacante, atacado):
    dano = atacante['força'] * randint(4, 10)
    acerto = True if atacante['destreza'] * randint(1, 10) > 10 else False
    dano_real = 0
    if acerto:
        dano_real = dano - atacado['defesa'] * randint(1, 3)
    print('Seu ataque deu {} de dano e {} perdeu {} de vida!'.format(dano, atacado['nome'], dano_real) if dano > 0 else 'Que pena, você errou seu ataque!')
    return dano_real


def dano_magico(atacante, atacado):
    dano = atacante['poder_magico'] * randint(4, 10)
    dano_real = dano - atacado['defesa'] * randint(1, 3)
    print('Seu ataque deu {} de dano mágico e {} perdeu {} de vida!'.format(dano, atacado['nome'],dano_real))
    return dano_real


def buff_fisico(atacante):
    nova_forca = atacante['força'] + (0.01 * atacante['vida'])
    aumento = nova_forca - atacante['força']
    print('Força aumentada em',aumento)
    return nova_forca

def buff_magico(atacante):
    novo_poder_magico = atacante['poder_magico'] + (0.01 * atacante['vida'])
    aumento = novo_poder_magico - atacante['poder_magico']
    print('Poder mágico aumentado em',aumento)
    return novo_poder_magico 

def buff_defesa(atacante):
    nova_defesa = atacante['defesa'] * 2 
    print('Defesa aumentada em',atacante['defesa'])
    return nova_defesa

personagens = { # personagens
    'Canon': {  # Guerreiro tanker
        'nome': 'Canon, o Barbudo',
        'vida': 1500,
        'defesa': 15,
        'força': 10,
        'destreza': 5,
        'poder_magico': 0,
        'habilidades':[
            {
                'nome':'Soco de uma polegada',# Dano
                'acao': dano_fisico

            },
            {
                'nome': 'Fúria infernal',  # Buff de dano fisico
                'acao': buff_fisico

            },
            {
                'nome': 'Aura reforçada',  # Buff de defesa
                'acao': buff_defesa

            },
            {
                'nome': 'Carapaça de espinhos',  # Reflete o dano da próxima habilidade recebida

            },
        ]
    },
    'Elisa': {  # Mago
        'nome': 'Elisa, não é a Elsa',
        'vida': 750,
        'poder_magico': 20,
        'defesa': 10,
        'força': 0,
        'destreza': 0,
        'habilidades':[
            {
                'nome': 'Tempestade de neve',  # Dano
                'acao': dano_magico

            },
            {
                'nome': 'Chuva de granizos',  # Buff de dano mágico
                'acao': buff_magico
            },
            {
                'nome': 'Envólucro de gelo',  # Buff de defesa
                'acao': buff_defesa

            },
            {
                'nome': 'Brisa congelante',  # Declama uma bela melodia, congelando o inimigo por 1 turno

            },
        ]
    },
    'Jack': {  # Samurai
        'nome': 'Samurai Jack',
        'vida': 1000,
        'força': 15,
        'destreza': 10,
        'defesa': 5,
        'poder_magico': 0,
        'habilidades': [
            {
                'nome': 'Katana incisiva',  # Dano
                'acao': dano_fisico

            },
            {
                'nome': 'Lâmina corrompida',  # Buff de dano fisico
                'acao': buff_fisico

            },
            {
                'nome': 'Espírito da espada',  # Buff de defesa
                'acao': buff_defesa

            },
            {
                'nome': 'Último suspiro',  # Se a vida do oponente for menor que 10% , o hit é fatal

            },
        ]
    }
}


def quem_vai_jogar():
    global proximo_a_jogar
    jogador_atual = jogadores[proximo_a_jogar]
    if proximo_a_jogar == 1:
        proximo_a_jogar = 0
    elif proximo_a_jogar == 0:
        proximo_a_jogar = 1
    return jogador_atual


def receber_entrada(entradas_permitidas, mensagem_de_erro):
    while (entrada_recebida := input().capitalize()) not in entradas_permitidas:
        print('{}, digite novamente:\n'.format(mensagem_de_erro))
    return entrada_recebida

def conhecer_os_personagens():
    print('Nossos personagens são esses:\n')
    for personagem in personagens:
        print(personagem)
    print('Qual você deseja conhecer agora?')
    while (boneco := input().capitalize()) not in personagens.keys():
        print('Esse personagem não existe, digite novamente:\n')
        boneco = input().capitalize()
    for k, v in personagens[boneco].items():
        print(k + ": " + str(v))
    print('Deseja:\n'+
        '1.Retornar ao menu.\n'+
        '2.Conhecer mais personagens.\n')
    op = int(input())
    if op == 2:
        conhecer_os_personagens()


# for personagem in personagens:
# #     for k, v in personagem.items():
# #         print(k +": " +str(v))
def menu():
    print('Bem-vindos(as) nobres lutadores ao Perfect Legends!\n' +
          'Neste momento, vocês desejam:\n' +
          '1.Jogar\n' +
          '2.Conhecer os personagens\n' +
          '3.Sair\n')
    op = receber_entrada(entradas_permitidas=['1','2','3'], mensagem_de_erro='Essa opção não existe')
    if op == '1':
        print('Jogador X, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        boneco1 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores.append(personagens[boneco1])
        print('Jogador Y, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        boneco2 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores.append(personagens[boneco2])
        jogador_atual = quem_vai_jogar()
        print('{} qual ataque deseja executar:'.format(jogador_atual['nome']))
        for x, habilidade in enumerate(jogador_atual['habilidades'], 1):
            print('{}.{}'.format(x, habilidade['nome']))
        habilidade_escolhida = int(receber_entrada(entradas_permitidas=['1', '2',  '3', '4'], mensagem_de_erro='Essa habilidade não existe'))-1
        jogadores[proximo_a_jogar]['vida'] -= jogador_atual['habilidades'][habilidade_escolhida]['acao'](jogador_atual, jogadores[proximo_a_jogar])
        ic(jogadores[proximo_a_jogar]['vida'], jogador_atual['vida'])
        #if jogadores[proximo_a_jogar]['vida'] > 0:


    elif op == '2':
        conhecer_os_personagens()
    if op != '3':
        menu()


# def vencedor(batalha):
#     if batalha['player1']['hp'] > 0 and batalha['player2']['hp'] > 0:
#         return None
#     if batalha['player1']['hp'] > 0 and batalha['player2']['hp'] <= 0:
#         return batalha['player1']
#     if batalha['player1']['hp'] <= 0 and batalha['player2']['hp'] > 0:
#         return batalha['player2']
#     return batalha['player1']




menu()
print('Obrigada por se aventurar em Perfect Legends, aguardamos seu retorno!')

# for personagem in personagens:
#     for k, v in personagem.items():
#         print(k +": " +str(v))
# for personagem in personagens:
#     print(personagem['nome'])
# for personagem in personagens:
#     primeiro_nome = personagem['nome'].split(',')
#     print(primeiro_nome[0])
# for k, v in personagens[0].items():
#     print(k +": " +str(v))