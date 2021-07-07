import os
from pathlib import Path
from random import randint
from time import sleep

from icecream import ic

# ic.disable()


def ativar_buff(propriedade_afetada, afetado,habilidade):
    if afetado['habilidades'][habilidade]['acao'] and afetado['habilidades'][habilidade]['rounds'] > 0:
        buff_ativo = propriedade_afetada + (propriedade_afetada * afetado['habilidades'][habilidade]['aumento'])
        afetado['habilidades'][habilidade]['rounds'] -= 1
        if afetado['habilidades'][habilidade]['rounds'] == 0:
            afetado['habilidades'][habilidade]['acao'] = False
        print('{} está sob o efeito de {} por mais {} rodadas'.format(afetado['nome'],afetado['habilidades'][habilidade]['nome'], afetado['habilidades'][habilidade]['rounds']) if afetado['habilidades'][habilidade]['rounds'] > 0 else 'O efeito {} de {} acabou!'.format(afetado['habilidades'][habilidade]['nome'], afetado['nome']))
        return buff_ativo
    return propriedade_afetada
  
  
# Exibe o nome dos personagens
def exibir_personagens():
    for personagem in personagens:
        print(personagem)


# Habilidade 1 Canon e Jack
# Aplica o dano que será causado ao personagem atacado
# Possui taxa de acerto, calculada com base na destreza do atacante 
def dano_fisico(atacante, atacado):
    dano = atacante['força'] * randint(4, 10)
    dano = ativar_buff(dano, atacante, 1) # Habilidade 2: Aumenta o ataque - duração de 2 rounds
    acerto = True if atacante['destreza'] * randint(1, 10) > 10 else False
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    defesa_do_atacado = ativar_buff(defesa_do_atacado, atacado,2) # Habilidade 3: Aumenta a defesa - duração de 2 rounds
    dano_real = int(dano) - int(defesa_do_atacado)
    if acerto and dano > defesa_do_atacado:
        print('Seu ataque deu {} de dano e {} perdeu {} de vida!'.format(int(dano), atacado['nome'], dano_real))
    elif acerto:
        print('Que pena, {} se defendeu!'.format(atacado['nome']))
    else:
        print('Que pena, você errou seu ataque!')
    atacado['vida'] -= dano_real if (dano_real > defesa_do_atacado and acerto) else 0


# Habilidade 1 Elisa
# 100% de acerto 
def dano_magico(atacante, atacado):
    dano = atacante['poder_magico'] * randint(4, 10)
    dano = ativar_buff(dano, atacante, 1)
    defesa_do_atacado = atacado['defesa'] * randint(1, 3)
    defesa_do_atacado = ativar_buff(defesa_do_atacado, atacado,2)
    dano_real = int(dano) - int(defesa_do_atacado)
    print('Seu ataque deu {} de dano mágico e {} perdeu {} de vida!'.format(int(dano), atacado['nome'],dano_real) if dano_real > 0 else 'Que pena, {} se defendeu!'.format(atacado['nome']))
    atacado['vida'] -= dano_real if dano_real > defesa_do_atacado else 0


def dano_verdadeiro(atacante, atacado):
    dano_real= int(atacado['vida']*atacante['habilidades'][3]['dano_verdadeiro'])
    print('O ataque {} de {} tirou {}% da vida de {}'.format(atacante['habilidades'][3]['nome'], atacante['nome'], int(atacante['habilidades'][3]['dano_verdadeiro']*100), atacado['nome']))
    atacado['vida'] -= dano_real if dano_real <= atacado['vida'] else atacado['vida']


personagens = {  # personagens
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
                'descricao': 'Reúne toda sua força em um soco para aplicar dano ao inimigo',
                'acao': dano_fisico,
                'exibir': True

            },
            {
                'nome': 'Fúria infernal',
                'descricao': 'Reúne toda a fúria armazenada em sua grande barba, tornando seus socos mais fortes nos próximos ataques',
                'acao': False,
                'aumento': 0.05,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Aura reforçada',  # Buff de defesa
                'descricao': 'Reforça a defesa para se proteger do inimigo',
                'acao': False,
                'aumento': 0.15,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Espinhos penetrantes',  # Dano baseado na vida no inimigo
                'descricao': 'Crava espinhos aplicando 5% da vida do inimigo como dano',
                'acao': dano_verdadeiro,
                'dano_verdadeiro': 0.05,
                'exibir': True

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
                'nome': 'Chuva de granizos',  # Dano
                'descricao': 'Derrama seu poder mágico atráves de uma chuva de granizos para aplicar dano ao inimigo',
                'acao': dano_magico,
                'exibir': True

            },
            {
                'nome': 'Tempestade de neve',
                'descricao': 'Declama uma estonteante melodia que invoca uma tempestade de neve, aumentando seu dano nos próximos ataques',
                'aumento': 0.1,
                'acao': False,
                'rounds': 0,
                'exibir': True
            },
            {
                'nome': 'Envólucro de gelo',  # Buff de defesa
                'descricao': 'Conjura através do seu poder mágico um envólucro de gelo para se proteger dos próximos ataques do inimigo',
                'aumento':  0.1,
                'acao': False,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Brisa congelante',  # Dano baseado na vida no inimigo
                'descricao': 'Sopra uma brisa que aplica 10% da vida do inimigo como dano',
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
                'descricao': 'Golpeia o inimigo com a força de sua katana',
                'acao': dano_fisico,
                'exibir': True

            },
            {
                'nome': 'Lâmina corrompida',  # Buff de dano fisico
                'descricao': 'Invoca o espírito selado na espada, aumentando o dano dos próximos ataques',
                'acao': False,
                'aumento': 0.2,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Espírito da espada',  # Buff de defesa
                'descricao': 'O espírito assume o controle e protege seu portador dos próximos ataques',
                'acao': False,
                'aumento': 0.2,
                'rounds': 0,
                'exibir': True

            },
            {
                'nome': 'Último suspiro',
                'descricao': 'Concentra sua força em um único golpe que dilacera o inimigo, aplicando 20% da vida do inimigo como dano',
                'acao':dano_verdadeiro,
                'dano_verdadeiro': 0.2,  # Dano baseado na vida no inimigo, se a vida do oponente for menor que 20% , o hit é fatal
                'exibir': True

            },
        ]
    }
}


# Cria uma cópia das habilidades de um personagem do dicionário para adicionar no array jogadores
def copia_do_personagem(boneco):
    jogador = personagens[boneco].copy()
    jogador['habilidades'] = []
    for habilidade in personagens[boneco]['habilidades']:
        jogador['habilidades'].append(habilidade.copy())
    return jogador


# Cria uma cópia das habilidades de um personagem do dicionário para adicionar no array jogadores
def copia_dos_personagens(boneco1,boneco2):
    jogadores = []
    jogador = copia_do_personagem(boneco1)
    jogadores.append(jogador)
    jogador = copia_do_personagem(boneco2)
    jogadores.append(jogador)
    return jogadores


# Cria uma cópia das habilidades de um personagem do dicionário para adicionar no array jogadores
def quem_vai_jogar(proximo_a_jogar):
    if proximo_a_jogar == 1:
        primeiro_a_jogar = 0
    elif proximo_a_jogar == 0:
        primeiro_a_jogar = 1
    return primeiro_a_jogar


# Auto-explicativo 
def receber_entrada(entradas_permitidas, mensagem_de_erro):
    while (entrada_recebida := input().capitalize()) not in entradas_permitidas:
        ic(entrada_recebida)
        print('{}, digite novamente:\n'.format(mensagem_de_erro))
    return entrada_recebida


def receber_senha(entradas_permitidas):
    while (entrada_recebida := input()) not in entradas_permitidas:
        ic(entrada_recebida)
        print('Senha incorreta, digite novamente:\n')
    return entrada_recebida


# Exibe um menu, onde é possível visualizar os atributos e habilidades dos personagens
def conhecer_os_personagens():
    print('Nossos personagens são esses:\n')
    exibir_personagens()
    print('Qual você deseja conhecer agora?')
    while (boneco := input().capitalize()) not in personagens.keys():
        print('Esse personagem não existe, digite novamente:\n')
        boneco = input().capitalize()
    for k, v in personagens[boneco].items():
        if k == 'habilidades':
            print(k+': ')
            for x, habilidade in enumerate(personagens[boneco][k], 1):
                print('{}.{}:{}'.format(x, habilidade['nome'], habilidade['descricao']))
        else:
            print(k + ": " + str(v))
    print('Deseja:\n'+
        '1.Retornar ao menu.\n'+
        '2.Conhecer mais personagens.\n')
    op = receber_entrada(entradas_permitidas=['1','2'], mensagem_de_erro='Entrada inválida')
    if op == '2':
        conhecer_os_personagens()


# Cria uma cópia das habilidades de um personagem do dicionário para adicionar no array jogadores
def consumir_habilidade(jogador, habilidade):
    jogador['habilidades'][habilidade]['exibir'] = False
    if habilidade == 1 or habilidade == 2:
        jogador['habilidades'][habilidade]['acao']= True
        jogador['habilidades'][habilidade]['rounds']=2
    return jogador


# Seleção de personagem
def selecionar_personagem(personagem_utilizado=None):
    ic(personagem_utilizado)
    print('Escolha com qual personagem deseja jogar:\n')
    exibir_personagens()
    print('\n')
    if personagem_utilizado:
        while (boneco := receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')) == personagem_utilizado:
            print('Personagem {} já utilizado, escolha outro:\n'.format(personagem_utilizado))
    else:
        boneco = receber_entrada(entradas_permitidas=personagens.keys(), mensagem_de_erro='Esse personagem não existe')
    return boneco


def receber_usuario(entradas_proibidas, mensagem_de_erro):
    while (usuario := input().capitalize()) in entradas_proibidas:
        print('{}, digite novamente:\n'.format(mensagem_de_erro))
        exibir_personagens()
    return usuario


def criar_usuario(x=''):
    print('Jogador{}, informe o nome de usuário que deseja criar:\n'.format(' '+str(x) if x else ''))
    usuario = receber_usuario(entradas_proibidas=personagens.keys(), mensagem_de_erro='Usuário Inválido, o nome de usuário deve ser diferente do nome dos persongens abaixo')
    path_usuario = Path('usuario_' + usuario)
    while os.path.exists(path_usuario):
        print("Usuário ", usuario, " já existe")
        usuario = receber_usuario(entradas_proibidas=personagens.keys(), mensagem_de_erro='Usuário Inválido, o nome de usuário deve ser diferente do nome dos persongens abaixo')
        path_usuario = Path('usuario_' + usuario)
    else:
        os.makedirs(path_usuario)
    print('Informe a senha que deseja usar para acessar:\n')
    senha = input()
    path_senha = path_usuario.joinpath('senha')
    with open(path_senha, 'w') as arquivo_senha:
        arquivo_senha.write(senha)
    print("Usuário ", usuario, " criado com sucesso! ")


def login(x, personagem_utilizado=None):
    ic(personagem_utilizado)
    print('Jogador {}, informe seu usuário:\n'.format(x))
    usuario = input()
    path_usuario = Path('usuario_' + usuario)
    if os.path.exists(path_usuario) and not os.path.exists(path_usuario.joinpath('flag')):
        path_senha = path_usuario.joinpath('senha')
        with open(path_senha, 'r') as arquivo_usuario:
            senha_correta = arquivo_usuario.readline()
        print('Informe sua senha:\n')
        ic(senha_correta)
        senha = receber_senha(entradas_permitidas=senha_correta)
        print('Bem-vindo(a) {}'.format(usuario))
        flag = path_usuario.joinpath('flag')
        flag.open('w')
        path_personagem = path_usuario.joinpath('personagem')
        with open(path_personagem, 'w') as arquivo_personagem:
            arquivo_personagem.write(selecionar_personagem(personagem_utilizado))
        return usuario
    else:
        print('Usuário não encontrado ou já logado')
        print('Deseja:\n' +
              '1.Tentar novamente\n' +
              '2.Criar Usuário\n')
        op = receber_entrada(entradas_permitidas=['1', '2'], mensagem_de_erro='Essa opção não existe')
        if op == '1':
            return login(x)
        if op == '2':
            criar_usuario(x)
            return login(x)


def logins():
    usuarios = []
    usuarios.append(login(x=1))
    path_usuario = Path('usuario_' + usuarios[0])
    with open(path_usuario.joinpath('personagem')) as arquivo_personagem:
        personagem_utilizado = arquivo_personagem.readline()
    ic(usuarios.append(login(x=2,personagem_utilizado=personagem_utilizado)))
    menu(usuarios)


# Autenticação
def autenticacao():
    print('Bem-vindos(as) nobres lutadores ao Perfect Legends!\n' +
          'Neste momento, vocês desejam:\n' +
          '1.Fazer Login\n' +
          '2.Criar uma conta\n' +
          '3.Sair\n')
    op = receber_entrada(entradas_permitidas=['1', '2', '3'], mensagem_de_erro='Essa opção não existe')
    if op == '1':
        logins()
    if op == '2':
        criar_usuario()
        autenticacao()


# Menu principal
def menu(usuarios):
    jogadores = []
    proximo_a_jogar = randint(0, 1)  # decide quem joga primeiro
    print('Bem-vindos(as) nobres lutadores ao Perfect Legends!\n' +
          'Neste momento, vocês desejam:\n' +
          '1.Jogar\n' +
          '2.Conhecer os personagens\n' +
          '3.Exibir vencedores\n' +
          '4.Sair\n')
    op = receber_entrada(entradas_permitidas=['1', '2', '3', '4'], mensagem_de_erro='Essa opção não existe')
    path_usuario = Path('usuario_' + usuarios[0])
    with open(path_usuario.joinpath('personagem')) as arquivo_personagem:
        boneco1 = arquivo_personagem.readline()
    path_usuario1 = Path('usuario_' + usuarios[1])
    with open(path_usuario1.joinpath('personagem')) as arquivo_personagem:
        boneco2 = arquivo_personagem.readline()
    jogadores = copia_dos_personagens(boneco1, boneco2)
    if op == '1':
        primeiro_a_jogar = quem_vai_jogar(proximo_a_jogar)
        while jogadores[primeiro_a_jogar]['vida'] > 0 and jogadores[proximo_a_jogar]['vida'] > 0: # Início da batalha
            print('{} qual ataque deseja executar:'.format(jogadores[primeiro_a_jogar]['nome']))
            habilidades_permitidas = []
            for x, habilidade in enumerate(jogadores[primeiro_a_jogar]['habilidades'], 1):
                if habilidade['exibir']:
                    print('{}.{}'.format(x, habilidade['nome']))
                    habilidades_permitidas.append(str(x))
            habilidade_escolhida = int(receber_entrada(entradas_permitidas=habilidades_permitidas, mensagem_de_erro='Essa habilidade não existe'))-1
            if habilidade_escolhida == 0 or habilidade_escolhida == 3:  # Habilidades 1 ou 4
                jogadores[primeiro_a_jogar]['habilidades'][habilidade_escolhida]['acao'](jogadores[primeiro_a_jogar], jogadores[proximo_a_jogar])
                sleep(1)
            if habilidade_escolhida > 0 and habilidade_escolhida < 4:  # Habilidades 2, 3 ou 4
                jogadores[primeiro_a_jogar] = consumir_habilidade(jogadores[primeiro_a_jogar], habilidade_escolhida)
                if habilidade_escolhida == 1 or habilidade_escolhida == 2:
                    print('{} usou {}, {} aumentou em {}%'.format(jogadores[primeiro_a_jogar]['nome'], jogadores[primeiro_a_jogar]['habilidades'][habilidade_escolhida]['nome'], 'o ataque' if habilidade_escolhida==1 else 'a defesa', jogadores[primeiro_a_jogar]['habilidades'][habilidade_escolhida]['aumento']*100))
                    sleep(1)
            print('Vida atual de {}:{}, vida atual de {}:{}'.format(jogadores[primeiro_a_jogar]['nome'], jogadores[primeiro_a_jogar]['vida'], jogadores[proximo_a_jogar]['nome'], jogadores[proximo_a_jogar]['vida']))
            if jogadores[proximo_a_jogar]['vida'] <= 0:
                ic(boneco1, boneco2, jogadores[primeiro_a_jogar]['nome'], jogadores[proximo_a_jogar]['nome'])
                if boneco1 in jogadores[primeiro_a_jogar]['nome']:
                    ic('entrou 1')
                    print('{} ganhou!'.format(usuarios[0]))
                    vencedor = ('- ' + usuarios[0]+'\n')
                else:
                    ic('entrou2')
                    print('{} ganhou!'.format(usuarios[1]))
                    vencedor = ('- ' + usuarios[1]+'\n')
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
        menu(usuarios)
    os.remove(path_usuario.joinpath('flag'))
    os.remove(path_usuario1.joinpath('flag'))


autenticacao()
print('Obrigada por se aventurar em Perfect Legends, aguardamos seu retorno!')