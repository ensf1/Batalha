from pathlib import Path
from random import randint
from time import sleep

from icecream import ic
ic.disable()

#decide quem joga primeiro
proximo_a_jogar = randint(0, 1)


def dano_fisico(atacante, atacado):
    dano = atacante['força'] * randint(4, 10)
    if atacante['habilidades'][1]['acao']:
        dano *= 1.1
        ic('Ataque buff', atacante['nome'],atacante['habilidades'][1]['acao'],atacante['habilidades'][1]['rounds'])
    acerto = True if atacante['destreza'] * randint(1, 10) > 10 else False
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    if atacado['habilidades'][2]['acao']:
        defesa_do_atacado *= 1.1
        ic('Def buff', atacado['nome'],atacado['habilidades'][2]['acao'],atacado['habilidades'][2]['rounds'])
    dano_real = int(dano) - int(defesa_do_atacado)
    if acerto and dano > defesa_do_atacado:
        print('Seu ataque deu {} de dano e {} perdeu {} de vida!'.format(int(dano), atacado['nome'], dano_real))
    elif acerto:
        print('Que pena, {} se defendeu!'.format(atacado['nome']))
    else:
        print('Que pena, você errou seu ataque!')
    return dano_real if dano_real > defesa_do_atacado else 0


def dano_magico(atacante, atacado):
    dano = atacante['poder_magico'] * randint(4, 10)
    if atacante['habilidades'][1]['acao']:
        dano *= 1.1
        ic('Ataque buff', atacante['nome'] ,atacante['habilidades'][1]['acao'], atacante['habilidades'][1]['rounds'])
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    if atacado['habilidades'][2]['acao']:
        defesa_do_atacado *= 1.1
        ic('Def buff', atacado['nome'], atacado['habilidades'][2]['acao'], atacado['habilidades'][2]['rounds'])
    dano_real = int(dano) - int(defesa_do_atacado)
    print('Seu ataque deu {} de dano mágico e {} perdeu {} de vida!'.format(int(dano), atacado['nome'],dano_real) if dano_real > 0 else 'Que pena, {} se defendeu!'.format(atacado['nome']))
    return dano_real if dano_real > defesa_do_atacado else 0



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
                'acao': dano_fisico,
                'exibir': True

            },
            {
                'nome': 'Fúria infernal',
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Aura reforçada',  # Buff de defesa
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Carapaça de espinhos',  # Reflete o dano da próxima habilidade recebida
                'acao': '',
                'rounds': 0,
                'exibir': True

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
                'acao': dano_magico,
                'exibir': True

            },
            {
                'nome': 'Chuva de granizos',
                'acao': False,
                'rounds': 0,
                'exibir': True
            },
            {
                'nome': 'Envólucro de gelo',  # Buff de defesa
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Brisa congelante',  # Declama uma bela melodia, congelando o inimigo por 1 turno,
                'acao':'',
                'rounds': 0,
                'exibir': True

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
                'acao': dano_fisico,
                'exibir': True

            },
            {
                'nome': 'Lâmina corrompida',  # Buff de dano fisico
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Espírito da espada',  # Buff de defesa
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Último suspiro',  # Se a vida do oponente for menor que 10% , o hit é fatal
                'acao':'',
                'rounds': 0,
                'exibir': True

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



def menu():
    jogadores = []
    print('Bem-vindos(as) nobres lutadores ao Perfect Legends!\n' +
          'Neste momento, vocês desejam:\n' +
          '1.Jogar\n' +
          '2.Conhecer os personagens\n' +
          '3.Exibir vencedores\n' +
          '4.Sair\n')
    op = receber_entrada(entradas_permitidas=['1','2','3','4'], mensagem_de_erro='Essa opção não existe')
    if op == '1':
        print('Jogador X, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        boneco1 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores.append(personagens[boneco1].copy())
        print('Jogador Y, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        boneco2 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores.append(personagens[boneco2].copy())
        jogador_atual = quem_vai_jogar(jogadores)
        while jogador_atual['vida'] > 0 and jogadores[proximo_a_jogar]['vida'] > 0:
            print('{} qual ataque deseja executar:'.format(jogador_atual['nome']))
            habilidades_permitidas = []
            for x, habilidade in enumerate(jogador_atual['habilidades'], 1):
                if habilidade['exibir']:
                    print('{}.{}'.format(x, habilidade['nome']))
                    habilidades_permitidas.append(str(x))
            habilidade_escolhida = int(receber_entrada(entradas_permitidas=habilidades_permitidas, mensagem_de_erro='Essa habilidade não existe'))-1
            if habilidade_escolhida == 0:
                jogadores[proximo_a_jogar]['vida'] -= jogador_atual['habilidades'][habilidade_escolhida]['acao'](jogador_atual, jogadores[proximo_a_jogar])
                sleep(1)
                if jogador_atual['habilidades'][1]['acao'] and jogador_atual['habilidades'][1]['rounds'] > 0:
                    jogador_atual['habilidades'][1]['rounds'] -= 1
                    ic('atacante', jogador_atual['nome'])
                    if jogador_atual['habilidades'][1]['rounds'] == 0:
                        jogador_atual['habilidades'][1]['acao'] = False
                if jogadores[proximo_a_jogar]['habilidades'][2]['acao'] and jogadores[proximo_a_jogar]['habilidades'][2]['rounds'] > 0:
                    jogadores[proximo_a_jogar]['habilidades'][2]['rounds'] -= 1
                    ic('atacado', jogador_atual['nome'])
                    if jogadores[proximo_a_jogar]['habilidades'][2]['rounds'] == 0:
                        jogadores[proximo_a_jogar]['habilidades'][2]['acao'] = False
            elif habilidade_escolhida == 1 or habilidade_escolhida == 2:
                print('{} usou {}, {} aumentou em 10%'.format(jogador_atual['nome'],jogador_atual['habilidades'][habilidade_escolhida]['nome'], 'o ataque' if habilidade_escolhida==1 else 'a defesa'))
                sleep(1)
                ic(jogador_atual['habilidades'][habilidade_escolhida]['exibir'])
                jogador_atual['habilidades'][habilidade_escolhida]['exibir'] = False
                ic(jogador_atual['habilidades'][habilidade_escolhida]['exibir'])
                jogador_atual['habilidades'][habilidade_escolhida]['acao']= True
                jogador_atual['habilidades'][habilidade_escolhida]['rounds'] = 2
                ic(jogador_atual['nome'])
            ic(jogadores[proximo_a_jogar]['vida'], jogador_atual['vida'])
            if jogadores[proximo_a_jogar]['vida'] > 0:
                print('{} qual ataque deseja executar:'.format(jogadores[proximo_a_jogar]['nome']))
                habilidades_permitidas = []
                for x, habilidade in enumerate(jogadores[proximo_a_jogar]['habilidades'], 1):
                    if habilidade['exibir']:
                        print('{}.{}'.format(x, habilidade['nome']))
                        habilidades_permitidas.append(str(x))
                habilidade_escolhida = int(receber_entrada(entradas_permitidas=habilidades_permitidas, mensagem_de_erro='Essa habilidade não existe')) - 1
                if habilidade_escolhida == 0:
                    jogador_atual['vida'] -= jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['acao'](jogadores[proximo_a_jogar], jogador_atual)
                    sleep(1)
                    if jogadores[proximo_a_jogar]['habilidades'][1]['acao'] and jogadores[proximo_a_jogar]['habilidades'][1]['rounds']>0:
                        jogadores[proximo_a_jogar]['habilidades'][1]['rounds']-=1
                        ic('atacante',jogadores[proximo_a_jogar]['nome'])
                        if jogadores[proximo_a_jogar]['habilidades'][1]['rounds'] == 0:
                            jogadores[proximo_a_jogar]['habilidades'][1]['acao'] = False
                    if jogador_atual['habilidades'][2]['acao'] and jogador_atual['habilidades'][2]['rounds']>0:
                        jogador_atual['habilidades'][2]['rounds']-=1
                        ic('atacado',jogador_atual['nome'])
                        if jogador_atual['habilidades'][2]['rounds'] == 0:
                            jogador_atual['habilidades'][2]['acao'] = False

                elif habilidade_escolhida == 1 or habilidade_escolhida == 2:
                    print('{} usou {}, {} aumentou em 10%'.format(jogadores[proximo_a_jogar]['nome'], jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['nome'], 'o ataque' if habilidade_escolhida == 1 else 'a defesa'))
                    sleep(1)
                    ic(jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['exibir'])
                    jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['exibir'] = False
                    ic(jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['exibir'])
                    jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['acao'] = True
                    jogadores[proximo_a_jogar]['habilidades'][habilidade_escolhida]['rounds'] = 2
                    ic(jogadores[proximo_a_jogar]['nome'])
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