# personagens
personagens = []
#Guerreiro tanker
elias = {
    'nome': 'Elias, o Bárbaro',
    'defesa': 15,
    'força': 10,
    'destreza': 5,
    'poder Mágico': 0,
    'habilidade1': 'Soco de uma polegada', #Dano
    'habilidade2': 'Fúria infernal', #Diminui o acerto do inimigo por 2 rounds
    'habilidade3': 'Aura reforçada', #Dobra a defesa no próximo round
    'habilidade4': 'Carapaça de espinhos', #Reflete o dano da próxima habilidade recebida
}
personagens.append(elias)
#Mago
pedro = {
    'nome': 'Pedro Frozen, o Mago',
    'poder Mágico': 20,
    'defesa': 10,
    'força': 0,
    'destreza': 0,
    'habilidade1': 'Tempestade de neve', #Dano
    'habilidade2': 'Brisa congelante', #Congela o inimigo por 1 turno
    'habilidade3': 'Envólucro de gelo', #Reduz o dano recebido no próximo ataque inimigo
    'habilidade4': 'Chuva de granizos', #Toma dano adicional por 2 turnos(dano da habilidade do round+dano da chuva de granizos)
}
personagens.append(pedro)
#Arqueiro
esther = {
    'nome': 'Esther, a Arqueira',
    'destreza': 15,
    'força': 10,
    'defesa': 5,
    'poder Mágico': 0,
    'habilidade1': 'Flecha perfurante', #Dano
    'habilidade2': 'Flecha taciturna', #Impede o inimigo de usar habilidades por 2 turnos(apenas habilidade de 2 a 4)
    'habilidade3': 'Aura galvânica', #Esquiva da próxima habilidade inimiga (taxa de sucesso)
    'habilidade4': 'Maestria letal', #Aumenta o dano do ataque básico por 2 turnos
}
personagens.append(esther)
#Samurai
joberval = {
    'nome': 'Joberval, o Samurai',
    'força': 15,
    'destreza': 10,
    'defesa': 3,
    'poder Mágico': 2,
    'habilidade1': 'Katana incisiva', # Dano
    'habilidade2': 'Lâmina corrompida', #Diminui a defesa do inimigo no próximo round
    'habilidade3': 'Espírito da espada', #Bloqueia o dano da próxima habilidade inimiga (porcentagem de dano)
    'habilidade4': 'Último suspiro', #Se a vida do oponente for menor que X, o hit é fatal

}
personagens.append(joberval)
# for personagem in personagens:
# #     for k, v in personagem.items():
# #         print(k +": " +str(v))


