from pathlib import Path
from random import randint
from time import sleep

from icecream import ic
#decide quem joga primeiro
proximo_a_jogar = randint(0, 1)

# Exibe o nome dos personagens
def personagem():
    for personagem in personagens:
        print(personagem)

# Habilidade 1 Canon e Jack
# Retorna o dano real que será causado ao personagem atacado (dano do atacante - defesa do atacado)
# Possui taxa de acerto, calculada com base na destreza do atacante 
def dano_fisico(atacante, atacado):
    dano = atacante['força'] * randint(4, 10)
    acerto = True if atacante['destreza'] * randint(1, 10) > 10 else False
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    dano_real = dano - defesa_do_atacado
    if acerto and dano > defesa_do_atacado:
        print('Seu ataque deu {} de dano e {} perdeu {} de vida!'.format(dano, atacado['nome'], dano_real))
    elif acerto:
        print('Que pena, {} se defendeu!'.format(atacado['nome']))
    else:
        print('Que pena, você errou seu ataque!')
    return dano_real if dano_real > defesa_do_atacado else 0

# Habilidade 1 Elisa
# 100% de acerto 
def dano_magico(atacante, atacado):
    dano = atacante['poder_magico'] * randint(4, 10)
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    dano_real = dano - defesa_do_atacado
    print('Seu ataque deu {} de dano mágico e {} perdeu {} de vida!'.format(dano, atacado['nome'],dano_real) if dano_real > 0 else 'Que pena, {} se defendeu!'.format(atacado['nome']))
    return dano_real if dano_real > defesa_do_atacado else 0

# Habilidade 2 Canon e Jack
# Aumenta a força com base em 10% da vida atual
# Duração de 2 rounds
def buff_fisico(atacante):
    nova_forca = int(atacante['força'] + (0.01 * atacante['vida']))
    aumento = nova_forca - atacante['força']
    print('Força aumentada em',aumento)
    return nova_forca

# Habilidade 2 Elisa
# Aumento no poder mágico com base em 10% da vida atual
# Duração de 2 rounds
def buff_magico(atacante):
    novo_poder_magico = atacante['poder_magico'] + (0.01 * atacante['vida'])
    aumento = novo_poder_magico - atacante['poder_magico']
    print('Poder mágico aumentado em',aumento)
    return novo_poder_magico 

# Habilidade 3 
# Dobra a defesa por 2 rounds
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
                'acao': buff_fisico,
                'rounds': 0

            },
            {
                'nome': 'Aura reforçada',  # Buff de defesa
                'acao': buff_defesa,
                'rounds': 0

            },
            {
                'nome': 'Carapaça de espinhos',  # Reflete o dano da próxima habilidade recebida
                'acao': '',
                'rounds': 0

            },
        ]
    },
    'Elisa': {  # Mago
        'nome': 'Elisa, a Rainha Gélida',
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
                'acao': buff_magico,
                'rounds': 0
            },
            {
                'nome': 'Envólucro de gelo',  # Buff de defesa
                'acao': buff_defesa,
                'rounds': 0

            },
            {
                'nome': 'Brisa congelante',  # Declama uma bela melodia, congelando o inimigo por 1 turno
                'acao':'',
                'rounds': 0

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
                'acao': buff_fisico,
                'rounds': 0

            },
            {
                'nome': 'Espírito da espada',  # Buff de defesa
                'acao': buff_defesa,
                'rounds': 0

            },
            {
                'nome': 'Último suspiro',  # Se a vida do oponente for menor que 10% , o hit é fatal
                'acao':'',
                'rounds': 0

            },
        ]
    }
}


def quem_vai_jogar(jogadores):
    global proximo_a_jogar
    jogador_atual = jogadores[proximo_a_jogar]
    if proximo_a_jogar == 1:
        proximo_a_jogar = 0
    elif proximo_a_jogar == 0:
        proximo_a_jogar = 1
    return jogador_atual

# Auto-explicativo 
def receber_entrada(entradas_permitidas, mensagem_de_erro):
    while (entrada_recebida := input().capitalize()) not in entradas_permitidas:
        print('{}, digite novamente:\n'.format(mensagem_de_erro))
    return entrada_recebida

# Exibe um menu, onde é possível visualizar os atributos e habilidades dos personagens
def conhecer_os_personagens():
    print('Nossos personagens são esses:\n')
    personagem()
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

# Menu inicial 
def menu():
    jogadores = []
    print('Bem-vindos(as) nobres lutadores(as) ao Perfect Legends!\n' +
          'Neste momento, vocês desejam:\n' +
          '1.Jogar\n' +
          '2.Conhecer os personagens\n' +
          '3.Exibir vencedores\n' +
          '4.Sair\n')
    op = receber_entrada(entradas_permitidas=['1','2','3','4'], mensagem_de_erro='Essa opção não existe')
    if op == '1':
        # Seleção de personagem
        print('Jogador X, escolha com qual personagem deseja jogar:\n')
        personagem()
        print('\n')
        boneco1 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores.append(personagens[boneco1].copy())
        print('Jogador Y, escolha com qual personagem deseja jogar:\n')
        personagem()
        print('\n')
        boneco2 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores.append(personagens[boneco2].copy())
        jogador_atual = quem_vai_jogar(jogadores) 
        # Início da batalha
        while jogador_atual['vida'] > 0 and jogadores[proximo_a_jogar]['vida'] > 0:
            print('{} qual ataque deseja executar:'.format(jogador_atual['nome']))
            for x, habilidade in enumerate(jogador_atual['habilidades'], 1):
                print('{}.{}'.format(x, habilidade['nome']))
            habilidade_escolhida = int(receber_entrada(entradas_permitidas=['1', '2',  '3', '4'], mensagem_de_erro='Essa habilidade não existe'))-1
            jogadores[proximo_a_jogar]['vida'] -= jogador_atual['habilidades'][habilidade_escolhida]['acao'](jogador_atual, jogadores[proximo_a_jogar])
            sleep(1)
            ic(jogadores[proximo_a_jogar]['vida'], jogador_atual['vida'])
            if jogadores[proximo_a_jogar]['vida'] > 0:
                print('{} qual ataque deseja executar:'.format(jogadores[proximo_a_jogar]['nome']))
                for x, habilidade in enumerate(jogadores[proximo_a_jogar]['habilidades'], 1):
                    print('{}.{}'.format(x, habilidade['nome']))
                habilidade_escolhida = int(receber_entrada(entradas_permitidas=['1', '2', '3', '4'], mensagem_de_erro='Essa habilidade não existe')) - 1
                jogador_atual['vida'] -= jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['acao'](jogadores[proximo_a_jogar], jogador_atual)
                sleep(1)
                if jogador_atual['vida'] <= 0:
                    print('{} ganhou!'.format(jogadores[proximo_a_jogar]['nome']))
                    print('Informe seu nome para ser adicionado a lista de vencedores:\n')
                    vencedor = ('- ', input())
                    vencedor = str(vencedor)
                    with open('vencedores', 'w') as vencedores:
                        vencedores.write(vencedor)
            else:
                print('{} ganhou!'.format(jogador_atual['nome']))
                print('Informe seu nome para ser adicionado a lista de vencedores:\n')
                vencedor  = '- ' + input() + '\n'
                with open('vencedores', 'a') as vencedores:
                    vencedores.write(vencedor)
    elif op == '2':
        conhecer_os_personagens()
    elif op == '3':
        print('Vencedores:')
        arquivo_de_vencedores = Path('vencedores')
        arquivo_de_vencedores.touch()
        with open(arquivo_de_vencedores, 'r') as vencedores:
            for line in vencedores:
                print(line, end='')
        print('')
        sleep(2)
    if op != '4':
        menu()
menu()
print('Obrigada por se aventurar em Perfect Legends, aguardamos seu retorno!')