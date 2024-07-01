#Escreva as funções para as outras operações (subtração, multiplicação, divisão)

#//Arquivo calculadora.py

#A função de Menu tem por objetivo gerar um funcionamento continuo, e é uma interface onde o usuário poderá escolher a operação que deseja realizar.

from operacoes import soma, subtracao, multiplicacao, divisao

def menu():
    print('Bem vindo a calculadora')
    print('Qual operação deseja executar?')
    print('1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão', '5 - Sair', sep='\n')
    oper = input('Escolha a operação: ')
    
    if oper == '5':
        print('Operação finalizada.')
    elif oper =='1':
        print ('Você escolheu soma')
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print(f'O resultado da soma é {soma(a,b)}')
    elif oper == '2':
        print ('Você escolheu subtração')
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print(f'O resultado da subtração é {subtracao(a,b)}')
    elif oper == '3':
        print ('Você escolheu multiplicação')
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print(f'O resultado da multiplicação é {multiplicacao(a,b)}')
    elif oper == '4':
        print ('Você escolheu multiplicação')
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print(f'O resultado da divisão é {divisao(a,b)}')
    else: 
        print('Operação inválida, Tente novamente.')
        return menu()
        
    continuar = input('Você deseja fazer outra operação?(Sim/Não): ')
    if continuar.lower() in ['sim', 's']:
        return menu()
    else:
        print('Operação finalizada')
         
menu()