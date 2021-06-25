# personagens
personagens = {
    'Elias': {  # Guerreiro tanker
        'nome': 'Elias, o Bruto',
        'defesa': 15,
        'força': 10,
        'destreza': 5,
        'poder Mágico': 0,
        'habilidade1': 'Soco de uma polegada',  # Dano
        'habilidade2': 'Fúria infernal',  # Diminui o acerto do inimigo por 2 rounds
        'habilidade3': 'Aura reforçada',  # Dobra a defesa no próximo round
        'habilidade4': 'Carapaça de espinhos',  # Reflete o dano da próxima habilidade recebida
    },
    'Pedro': {  # Mago
        'nome': 'Pedro, o Let it Go',
        'poder Mágico': 20,
        'defesa': 10,
        'força': 0,
        'destreza': 0,
        'habilidade1': 'Tempestade de neve',  # Dano
        'habilidade2': 'Brisa congelante',  # Declama uma bela melodia, congelando o inimigo por 1 turno
        'habilidade3': 'Envólucro de gelo',  # Reduz o dano recebido no próximo ataque inimigo
        'habilidade4': 'Chuva de granizos',
        # Toma dano adicional por 2 turnos(dano da habilidade do round+dano da chuva de granizos)
    },
    'Esther': {  # Arqueira
        'nome': 'Esther, a Galadriel da 25 de março',
        'destreza': 15,
        'força': 10,
        'defesa': 5,
        'poder Mágico': 0,
        'habilidade1': 'Flecha perfurante',  # Dano
        'habilidade2': 'Flecha taciturna',
        # Impede o inimigo de usar habilidades por 2 turnos(apenas habilidade de 2 a 4)
        'habilidade3': 'Aura galvânica',  # Esquiva da próxima habilidade inimiga (taxa de sucesso)
        'habilidade4': 'Maestria letal',  # Aumenta o dano do ataque básico por 2 turnos
    },
    'Joberval': {  # Samurai
        'nome': 'Joberval, o Miyamoto Musashi manco',
        'força': 15,
        'destreza': 10,
        'defesa': 3,
        'poder Mágico': 2,
        'habilidade1': 'Katana incisiva',  # Dano
        'habilidade2': 'Lâmina corrompida',  # Diminui a defesa do inimigo no próximo round
        'habilidade3': 'Espírito da espada',  # Bloqueia o dano da próxima habilidade inimiga (porcentagem de dano)
        'habilidade4': 'Último suspiro',  # Se a vida do oponente for menor que X, o hit é fatal
    }

}


def conhecer_os_personagens():
    print('Nossos personagens são esses:\n')
    for personagem in personagens:
        print(personagem)
    print('Qual você deseja conhecer agora?')
    while boneco := input().capitalize() not in personagens.keys():
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
    op = int(input())
    while 3 > op >0:
        print('Essa opção não existe, tente novamente:\n')
        op = int(input())
    if op == 1:
        print('Primeiro jogador, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        while boneco1 := input().capitalize() not in personagens.keys():
            print('Esse personagem não existe, digite novamente:\n')
        print('Segundo jogador, escolha com qual personagem deseja jogar:\n')
        for personagem in personagens:
            print(personagem)
        print('\n')
        while boneco2 := input().capitalize() not in personagens.keys():
            print('Esse personagem não existe, digite novamente:\n')
    elif op == 2:
        conhecer_os_personagens()
    if op != 3:
        menu()
    print('Obrigada por se aventurar em Perfect Legends, aguardamos seu retorno!')

menu()

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