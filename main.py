from pathlib import Path
from random import randint
from time import sleep

from icecream import ic
# ic.disable()


def dano_fisico(atacante, atacado):
    ic(atacante['nome'],atacado['nome'])
    dano = atacante['força'] * randint(4, 10)
    if atacante['habilidades'][1]['acao'] and atacante['habilidades'][1]['rounds'] > 0:
        dano += (dano*atacante['habilidades'][1]['aumento'])
        atacante['habilidades'][1]['rounds'] -= 1
        if atacante['habilidades'][1]['rounds'] == 0:
            atacante['habilidades'][1]['acao'] = False
        ic('Ataque buff', atacante['nome'],atacante['habilidades'][1]['acao'],atacante['habilidades'][1]['rounds'])
    acerto = True if atacante['destreza'] * randint(1, 10) > 10 else False
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    if atacado['habilidades'][2]['acao'] and atacado['habilidades'][2]['rounds'] > 0:
        defesa_do_atacado += (defesa_do_atacado*atacado['habilidades'][2]['aumento'])
        atacado['habilidades'][2]['rounds'] -= 1
        if atacado['habilidades'][2]['rounds'] == 0:
            atacado['habilidades'][2]['acao'] = False
        ic('Def buff', atacado['nome'],atacado['habilidades'][2]['acao'],atacado['habilidades'][2]['rounds'])
    dano_real = int(dano) - int(defesa_do_atacado)
    if acerto and dano > defesa_do_atacado:
        print('Seu ataque deu {} de dano e {} perdeu {} de vida!'.format(int(dano), atacado['nome'], dano_real))
    elif acerto:
        print('Que pena, {} se defendeu!'.format(atacado['nome']))
    else:
        print('Que pena, você errou seu ataque!')
    atacado['vida'] -= dano_real if (dano_real > defesa_do_atacado and acerto) else 0


def dano_magico(atacante, atacado):
    dano = atacante['poder_magico'] * randint(4, 10)
    if atacante['habilidades'][1]['acao'] and atacante['habilidades'][1]['rounds'] > 0:
        dano += (dano*atacante['habilidades'][1]['aumento'])
        atacante['habilidades'][1]['rounds'] -= 1
        if atacante['habilidades'][1]['rounds'] == 0:
            atacante['habilidades'][1]['acao'] = False
        ic('Ataque buff', atacante['nome'] ,atacante['habilidades'][1]['acao'], atacante['habilidades'][1]['rounds'])
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    if atacado['habilidades'][2]['acao'] and atacado['habilidades'][2]['rounds'] > 0:
        defesa_do_atacado += (defesa_do_atacado*atacado['habilidades'][2]['aumento'])
        atacado['habilidades'][2]['rounds'] -= 1
        if atacado['habilidades'][2]['rounds'] == 0:
            atacado['habilidades'][2]['acao'] = False
        ic('Def buff', atacado['nome'], atacado['habilidades'][2]['acao'], atacado['habilidades'][2]['rounds'])
    dano_real = int(dano) - int(defesa_do_atacado)
    print('Seu ataque deu {} de dano mágico e {} perdeu {} de vida!'.format(int(dano), atacado['nome'],dano_real) if dano_real > 0 else 'Que pena, {} se defendeu!'.format(atacado['nome']))
    atacado['vida'] -= dano_real if dano_real > defesa_do_atacado else 0


def dano_verdadeiro(atacante, atacado):
    dano_real= int(atacado['vida']*atacante['habilidades'][3]['dano_verdadeiro'])
    print('O ataque {} de {} tirou {}% da vida de {}'.format(atacante['habilidades'][3]['nome'], atacante['nome'], int(atacante['habilidades'][3]['dano_verdadeiro']*100), atacado['nome']))
    atacado['vida'] -= dano_real if dano_real <= atacado['vida'] else atacado['vida']



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
                'aumento': 0.05,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Aura reforçada',  # Buff de defesa
                'acao': False,
                'aumento': 0.15,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Carapaça de espinhos',  # Reflete o dano da próxima habilidade recebida
                'acao': dano_verdadeiro,
                'dano_verdadeiro': 0.05,
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
                'aumento': 0.1,
                'acao': False,
                'rounds': 0,
                'exibir': True
            },
            {
                'nome': 'Envólucro de gelo',  # Buff de defesa
                'aumento':  0.05,
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Brisa congelante',  # Declama uma bela melodia, congelando o inimigo por 1 turno,
                'acao':dano_verdadeiro,
                'dano_verdadeiro': 0.1,
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
                'aumento': 0.2,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Espírito da espada',  # Buff de defesa
                'acao': False,
                'aumento': 0.1,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Último suspiro',
                'acao':dano_verdadeiro,
                'dano_verdadeiro': 0.2, # Se a vida do oponente for menor que 10% , o hit é fatal
                'exibir': True

            },
        ]
    }
}


def copia_do_personagem(boneco):
    jogador = personagens[boneco].copy()
    jogador['habilidades']  = []
    for habilidade in personagens[boneco]['habilidades']:
        jogador['habilidades'].append(habilidade.copy())
    return jogador


def copia_dos_personagens(boneco1,boneco2):
    jogadores = []
    jogador = copia_do_personagem(boneco1)
    jogadores.append(jogador)
    jogador = copia_do_personagem(boneco2)
    jogadores.append(jogador)
    return jogadores



def quem_vai_jogar(proximo_a_jogar):
    if proximo_a_jogar == 1:
        primeiro_a_jogar = 0
    elif proximo_a_jogar == 0:
        primeiro_a_jogar = 1
    return primeiro_a_jogar


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


def consumir_habilidade(jogador,habilidade):
    jogador['habilidades'][habilidade]['exibir'] = False
    if habilidade == 1 or habilidade == 2:
        jogador['habilidades'][habilidade]['acao']= True
        jogador['habilidades'][habilidade]['rounds']=2
    return jogador


def ativar_buff(atacante,atacado):
    return None


def menu():
    jogadores = []
    proximo_a_jogar = randint(0, 1) #decide quem joga primeiro
    print('Bem-vindos(as) nobres lutadores ao Perfect Legends!\n' +
          'Neste momento, vocês desejam:\n' +
          '1.Jogar\n' +
          '2.Conhecer os personagens\n' +
          '3.Exibir vencedores\n' +
          '4.Sair\n')
    op = receber_entrada(entradas_permitidas=['1','2','3','4'], mensagem_de_erro='Essa opção não existe')
    if op == '1':
        ic(jogadores)
        print('Jogador X, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        boneco1 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        ic(personagens[boneco1].copy())
        print('Jogador Y, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        boneco2 = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
        jogadores = copia_dos_personagens(boneco1,boneco2)
        ic(personagens[boneco2].copy())
        primeiro_a_jogar = quem_vai_jogar(proximo_a_jogar)
        while jogadores[primeiro_a_jogar]['vida'] > 0 and jogadores[proximo_a_jogar]['vida'] > 0:
            ic(primeiro_a_jogar,proximo_a_jogar)
            print('{} qual ataque deseja executar:'.format(jogadores[primeiro_a_jogar]['nome']))
            habilidades_permitidas = []
            for x, habilidade in enumerate(jogadores[primeiro_a_jogar]['habilidades'], 1):
                if habilidade['exibir']:
                    print('{}.{}'.format(x, habilidade['nome']))
                    habilidades_permitidas.append(str(x))
            habilidade_escolhida = int(receber_entrada(entradas_permitidas=habilidades_permitidas, mensagem_de_erro='Essa habilidade não existe'))-1
            if habilidade_escolhida == 0 or habilidade_escolhida == 3:
                ic(primeiro_a_jogar, proximo_a_jogar)
                jogadores[primeiro_a_jogar]['habilidades'][habilidade_escolhida]['acao'](jogadores[primeiro_a_jogar], jogadores[proximo_a_jogar])
                ic(primeiro_a_jogar,proximo_a_jogar)
                sleep(1)
            if habilidade_escolhida > 0 and habilidade_escolhida < 4:
                jogadores[primeiro_a_jogar] = consumir_habilidade(jogadores[primeiro_a_jogar],habilidade_escolhida)
                if habilidade_escolhida == 1 or habilidade_escolhida == 2:
                    print('{} usou {}, {} aumentou em {}%'.format(jogadores[primeiro_a_jogar]['nome'],jogadores[primeiro_a_jogar]['habilidades'][habilidade_escolhida]['nome'], 'o ataque' if habilidade_escolhida==1 else 'a defesa', jogadores[primeiro_a_jogar]['habilidades'][habilidade_escolhida]['aumento']*100))
                    sleep(1)
            if jogadores[proximo_a_jogar]['vida'] <= 0:
                print('{} ganhou!'.format(jogadores[primeiro_a_jogar]['nome']))
                print('Informe seu nome para ser adicionado a lista de vencedores:\n')
                vencedor = ('- ', input())
                vencedor = str(vencedor)
                with open('vencedores', 'a') as vencedores:
                    vencedores.write(vencedor)
            proximo_a_jogar = primeiro_a_jogar
            primeiro_a_jogar = quem_vai_jogar(proximo_a_jogar)
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