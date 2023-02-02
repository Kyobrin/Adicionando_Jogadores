jogadores = {}

def registro():
    jogador = str(input('Digite o nome do jogador: '))
    partidas = None
    while not isinstance(partidas, int):
        try:
            partidas = int(input('Quantas partidas ele(a) jogou: '))
        except ValueError:
         print('Digite um número inteiro.')
         continue
        gols = []
        totalgol = 0
        for g in range(partidas):
            gol = int(input(f'Quantos gols ele(a) fez na {g+1} .a partida: '))
            gols.append(gol)
            totalgol += gol
        jogadores[jogador] = {'Partidas': partidas, 'Gols': gols, 'Soma Gols': totalgol}
        break
    return jogadores

def tabela():
    print ('-'*100)
    print (f'{"TABELA DE JOGADORES":^100}')
    print ('-'*100)
    print (f'{"codigo":<15} {"Jogador":<30} {"Gols":<30} {"Soma Gols":<15} ')
    for i, k in enumerate (jogadores.keys()):
        v = jogadores[k]
        print (f'{i:<15} {k:<30} {str(v["Gols"]):<30} {v["Soma Gols"]:<15}')
        print ('-'*100)



while True:
    print ('-'*50)
    registro()
    res = str(input('Quer continuar a registrar? [S/N] '))
    while res not in "SsNn":
        print('Digite uma opção válida!')
        res = str(input('Quer continuar a registrar? [S/N] '))
        if res in 'Nn':
            print (f'\n' * 170)
            tabela()
            break
    if res in 'Nn':
        print (f'\n' * 170)
        tabela()
        break