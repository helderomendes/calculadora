#JOGO DE PEDRA PAPEL TESOURA:
#utilize a biblioteca randint para gerar valores aleatórios
from random import randint


opcoes = ['pedra', 'papel', 'tesoura']

aleatorio = randint(0, 2)
print(opcoes[aleatorio])


# Criar um menu
# Esse opções ao usuário, usuário escolhe uma das opções.
# Usuário escolheu, máquina escolheu.

# Vitoria do jogador.
# J -> 'Pedra' - M - 'Tesoura'
# J -> 'Papel' - M - 'Pedra'
# J -> 'Tesoura - M - 'Papel'


def menugame():
    print('Bem-vindo ao Jokenpo! Seu oponente é a máquina. Tente vencê-la. Boa sorte!')
    input(f'Selecione sua opção entre:{opcoes}':)
    

menugame()