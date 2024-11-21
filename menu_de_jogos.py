#Projeto: MENU DE JOGOS
#Alunos: Ryan Luka Santos Oliveira - 121111046;
# Jailson Dantas Da Silva - 121111224;
# Gabriel Davi Rocha Nobelino - 121111256.
#----------------------------------
#ímpar ou par
def par_impar():
    from random import randint
    from time import sleep
    continuar = 0
    print('\n' * 5)
    print('=-' * 16)
    print('\t\33[1;33mVAMOS JOGAR PAR OU ÍMPAR\33[m')
    print('=-' * 16)
    while True:
        if continuar == 0:
            vitorias = 0
            while True:
                jogador = int(input('Digite um valor:'))
                pi = ' '
                while pi not in 'PI':
                    pi = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
                pc = randint(0, 10)
                total = jogador + pc
                impar_par = ''
                if (jogador + pc) % 2 == 0:
                    impar_par = 'PAR'
                elif (jogador + pc) % 2 != 0:
                    impar_par = 'ÍMPAR'
                print('_' * 45)
                print(f'Você jogou {jogador} e o computador {pc}. Total de {total} deu {impar_par}!')
                print('_' * 45)
                if (jogador + pc) % 2 != 0 and pi == 'I':
                    print('\33[1;32mVocê VENCEU!\33[m')
                    print('Vamos jogar novamente...')
                    print('-=' * 15)
                    vitorias += 1
                elif (jogador + pc) % 2 == 0 and pi == 'P':
                    print('\33[1;32mVocê VENCEU!\33[m')
                    print('Vamos jogar novamente...')
                    print('-=' * 15)
                    vitorias += 1
                else:
                    print('\33[1;31mVocê PERDEU!\33[m')
                    print('-=' * 15)
                    print(f'\33[1;31mGAME OVER!\33[m Você venceu {vitorias} vezes.')
                    break
            continuar = int(input('''
[0] Jogar novamente
[1] Voltar para o menu
opção:'''))
            print()
        elif continuar == 1:
            print()
            sleep(2)
            print('\n' * 5)
            break
    return
#adivinhe o número
def adv_num():
    from time import sleep
    from random import randint
    print('\n' * 5)
    print('-=-' * 20)
    print('\33[1;34mOlá! Vou pensar em um número entre 0 e 100. Tente adivinhar!\33[m')
    print('-=-' * 20)
    continuar = 0
    while True:
        if continuar == 0:
            pc = randint(0, 100)
            palpites = 0
            print('\33[1;33mVamos lá...\33[m')
            while True:
                jg = int(input('Qual é o seu palpite?'))
                palpites += 1
                if jg == pc:
                    print(f'\n\33[1;32mVocê acertou!\33[m Eu pensei no número {pc}.')
                    print(f'Você fez {palpites} palpites até acertar.')
                    break
                elif jg < pc:
                    print('Quase... Tente um número maior:')
                elif jg > pc:
                    print('Quase... Tente um número menor:')
            continuar = int(input('''
[0] Jogar novamente
[1] Voltar para o menu
opção:'''))
            print()
        elif continuar == 1:
            print()
            sleep(2)
            print('\n' * 5)
            break
    return
#jokenpô
def jokenpo():
    from time import sleep
    from random import randint
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    print('\n'*5)
    print('-='*20)
    print('\33[1;35m\t\tOlá! Vamos jogar Jokenpô!\33[m')
    print('-='*20)
    continuar = 0
    while True:
        if continuar == 0:
            print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
            jg = int(input('Qual é a sua jogada?'))
            print('\33[1;32mJO\33[m')
            sleep(1)
            print('\33[1;33mKEN\33[m')
            sleep(1)
            print('\33[1;34mPÔ!\33[m')
            sleep(1)
            print('-=' * 12)
            print(f'Computador jogou {itens[pc]}')
            print(f'Jogador jogou {itens[jg]}')
            print('-=' * 12)
            if jg == 0 and pc == 2 or jg == 2 and pc == 1 or jg == 1 and pc == 0:
                print('\33[1;32mJOGADOR VENCEU!\33[m')
            elif pc == 0 and jg == 2 or pc == 2 and jg == 1 or pc == 1 and jg == 0:
                print('\33[1;31mCOMPUTADOR VENCEU!\33[m')
            elif jg == pc:
                print('\33[1;33mEMPATE!\33[m')
            continuar = int(input('''
[0] Jogar novamente
[1] Voltar para o menu
opção:'''))
        elif continuar == 1:
            print()
            sleep(2)
            print('\n'*5)
            break
    return
#jogo da velha
def jogo_da_velha():
    from time import sleep
    from random import randint
    print('\n' * 5)
    print('-' * 20)
    print('\t\33[1;36mJOGO DA VELHA\33[m')
    print('-' * 20)
    print('\33[1;31mATENÇÃO!\33[m')
    print('As linhas são 0, 1 e 2')
    print('As colunas são 0, 1 e 2')
    print()
    continuar = 0
    while continuar == 0:
        print('\33[1;33mVamos lá...\33[m')
        layout = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        jogador = 'X'
        cont_jogadas = 0
        print('    0   1   2')
        print('0:  ' + layout[0][0] + ' | ' + layout[0][1] + ' | ' + layout[0][2])
        print('   -----------')
        print('1:  ' + layout[1][0] + ' | ' + layout[1][1] + ' | ' + layout[1][2])
        print('   -----------')
        print('2:  ' + layout[2][0] + ' | ' + layout[2][1] + ' | ' + layout[2][2])
        while True:
            # RESULTADO LINHA E COLUNA 1
            if layout[0][0] + layout[0][1] + layout[0][2] == 'XXX' or layout[0][0] + layout[1][0] + layout[2][0] == 'XXX':
                print('\33[1;32mParabéns, Você ganhou!\33[m')
                break
            elif layout[0][0] + layout[0][1] + layout[0][2] == 'OOO' or layout[0][0] + layout[1][0] + layout[2][0] == 'OOO':
                print('\33[1;31mO PC ganhou!\33[m')
                break
            # RESULTADO LINHA E COLUNA 2
            if layout[1][0] + layout[1][1] + layout[1][2] == 'XXX' or layout[0][1] + layout[1][1] + layout[2][1] == 'XXX':
                print('\33[1;32mParabéns, Você ganhou!\33[m')
                break
            elif layout[1][0] + layout[1][1] + layout[1][2] == 'OOO' or layout[0][1] + layout[1][1] + layout[2][1] == 'OOO':
                print('\33[1;31mO PC ganhou!\33[m')
                break
            # RESULTADO LINHA E COLUNA 3
            if layout[2][0] + layout[2][1] + layout[2][2] == 'XXX' or layout[0][2] + layout[1][2] + layout[2][2] == 'XXX':
                print('\33[1;32mParabéns, Você ganhou!\33[m')
                break
            elif layout[2][0] + layout[2][1] + layout[2][2] == 'OOO' or layout[0][2] + layout[1][2] + layout[2][2] == 'OOO':
                print('\33[1;31mO PC ganhou!\33[m')
                break
            # RESULTADO VERTICAL
            elif layout[0][0] + layout[1][1] + layout[2][2] == 'XXX' or layout[0][2] + layout[1][1] + layout[2][0] == 'XXX':
                print('\33[1;32mParabéns, Você ganhou!\33[m')
                break
            elif layout[0][0] + layout[1][1] + layout[2][2] == 'OOO' or layout[0][2] + layout[1][1] + layout[2][0] == 'OOO':
                print('\33[1;31mO PC ganhou!\33[m')
                break
            elif cont_jogadas == 9:
                print('\33[1;33mDeu velha!\33[m')
                break
            if jogador == 'X':
                print()
                print('Sua vez, faça sua jogada!')
                while True:
                    try:
                        l = int(input('Linha: '))
                        c = int(input('Coluna: '))
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'O'
                            break
                        else:
                            print('Esse campo já foi preenchido!')
                    except:
                        print('Opção Inválida!')
                sleep(1)
            elif jogador == 'O':
                print()
                print('Vez do PC!')
                while True:
                    if layout[0][0] == 'O' and layout[1][0] == 'O':
                        l = 2
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'O' and layout[0][1] == 'O':
                        l = 0
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'O' and layout[2][1] == 'O':
                        l = 2
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[1][0] == 'O' and layout[1][1] == 'O':
                        l = 1
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'O' and layout[1][1] == 'O':
                        l = 0
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][2] == 'O' and layout[1][1] == 'O':
                        l = 0
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'O' and layout[1][1] == 'O':
                        l = 2
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'O' and layout[1][1] == 'O':
                        l = 2
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'O' and layout[1][0] == 'O':
                        l = 0
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'O' and layout[0][1] == 'O':
                        l = 0
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][2] == 'O' and layout[2][1] == 'O':
                        l = 2
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][2] == 'O' and layout[1][2] == 'O':
                        l = 0
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'O' and layout[1][2] == 'O':
                        l = 2
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][1] == 'O' and layout[1][1] == 'O':
                        l = 2
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][1] == 'O' and layout[1][1] == 'O':
                        l = 0
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][1] == 'O' and layout[2][1] == 'O':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'O' and layout[2][0] == 'O':
                        l = 1
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'O' and layout[2][2] == 'O':
                        l = 1
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'O' and layout[0][2] == 'O':
                        l = 0
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'O' and layout[2][2] == 'O':
                        l = 2
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[1][0] == 'O' and layout[1][2] == 'O':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'O' and layout[2][0] == 'O':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'O' and layout[2][2] == 'O':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[1][1] == 'O' and layout[1][2] == 'O':
                        l = 1
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[1][0] == 'X' and layout[1][2] == 'X':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'X' and layout[1][0] == 'X':
                        l = 2
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'X' and layout[0][1] == 'X':
                        l = 0
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'X' and layout[2][1] == 'X':
                        l = 2
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[1][0] == 'X' and layout[1][1] == 'X':
                        l = 1
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'X' and layout[1][1] == 'X':
                        l = 0
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][2] == 'X' and layout[1][1] == 'X':
                        l = 0
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'X' and layout[1][1] == 'X':
                        l = 2
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'X' and layout[1][1] == 'X':
                        l = 2
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'X' and layout[1][0] == 'X':
                        l = 0
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'X' and layout[0][1] == 'X':
                        l = 0
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][2] == 'X' and layout[2][1] == 'X':
                        l = 2
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][2] == 'X' and layout[1][2] == 'X':
                        l = 0
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'X' and layout[1][2] == 'X':
                        l = 2
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][1] == 'X' and layout[1][1] == 'X':
                        l = 2
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][1] == 'X' and layout[1][1] == 'X':
                        l = 0
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][1] == 'X' and layout[2][1] == 'X':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'X' and layout[2][0] == 'X':
                        l = 1
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'X' and layout[2][2] == 'X':
                        l = 1
                        c = 2
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'X' and layout[0][2] == 'X':
                        l = 0
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[2][0] == 'X' and layout[2][2] == 'X':
                        l = 2
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][2] == 'X' and layout[2][0] == 'X':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[0][0] == 'X' and layout[2][2] == 'X':
                        l = 1
                        c = 1
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    if layout[1][1] == 'X' and layout[1][2] == 'X':
                        l = 1
                        c = 0
                        if ' ' in layout[l][c]:
                            layout[l][c] = jogador
                            jogador = 'X'
                            break
                    l = randint(0, 2)
                    c = randint(0, 2)
                    if ' ' in layout[l][c]:
                        layout[l][c] = jogador
                        jogador = 'X'
                        break
                sleep(1)
            cont_jogadas += 1
            print()
            print('    0   1   2')
            print('0:  ' + layout[0][0] + ' | ' + layout[0][1] + ' | ' + layout[0][2])
            print('   -----------')
            print('1:  ' + layout[1][0] + ' | ' + layout[1][1] + ' | ' + layout[1][2])
            print('   -----------')
            print('2:  ' + layout[2][0] + ' | ' + layout[2][1] + ' | ' + layout[2][2])
        continuar = int(input('''
[0] Jogar novamente
[1] Voltar para o menu
opção:'''))
        if continuar == 1:
            sleep(2)
            print('\n' * 5)
            break
    return
#soma, matemática
def soma():
    import random as rd
    import time
    print('\n'*5)
    print('-='*25)
    print('\t\33[1;34mOlá! Vamos ver se você é bom em matemática...\33[m')
    print('-='*25)
    continuar = 0
    while continuar == 0:
        pontos = 0
        cont = 0
        nivel = 0
        dif = 10
        notjog = 0
        print('O jogo irá começar, você tem 5 segundos para responder as questões!!')
        while True:
            iniciar = str(input('Pronto? [ s / n ]:').strip().lower()[0])
            if iniciar == 'n':
                print('Que pena.')
                notjog = 1
                break
            if iniciar != 's' or iniciar != 'n':
                print()
            if iniciar == 's':
                print('Prepare-se')
                break
        time.sleep(1)
        while True:
            if notjog == 1:
                break
            a = rd.randint(1, dif)
            b = rd.randint(1, dif)
            print(f'{a} +  {b} = ?')
            try:
                ini = time.time()
                c = int(input('resp: '))
                fim = time.time()
                contagem = fim - ini
                if contagem >= 5:
                    print('\33[1;31mDemorou muito!\33[m')
                    print(f'Resposta:{a + b}')
                    break
                if c == a + b:
                    pontos += 1
                    cont += 1
                    if cont == 3:
                        time.sleep(1)
                        print('Aumentando dificultade! Nível: ', nivel+1)
                        nivel += 1
                        dif += 5
                        cont = 0
                else:
                    print(f'Resposta:{a + b}')
                    break
            except:
                print('Aceitamos apenas valores numéricos!')
                print('\33[1;31mVocê perdeu!\33[m')
                break
        print('\33[1;31mVocê perdeu!\33[m')
        print('Fim de jogo!')
        print('Nível:', nivel)
        print('Pontos:', pontos)
        continuar = int(input('''
[0] Jogar novamente
[1] Voltar para o menu
opção:'''))
        if continuar == 1:
            time.sleep(2)
            print('\n'*5)
            break
    return
#palavra misteriosa
def palavra_mis():
    from time import sleep
    from random import choice
    print('\n'*5)
    print('-=' * 20)
    print('\033[1;34mSEJA BEM VINDO AO JOGO DA PALAVRA MISTERIOSA!\033[m')
    print('DIFICULDADE: \033[1;31mHARDCORE\033[m')
    print('-=' * 20)
    print()
    continuar = 0
    while continuar == 0:
        cont = 0
        while True:
            paises = ['Brasil', 'Argentina', 'Peru', 'Chile', 'Uruguai', 'Equador', 'Paraguai', 'Cuba', 'Espanha', 'França',
                      'Inglaterra', 'México', 'Canadá', 'Dinamarca', 'Venezuela', 'Egito', 'Venezuela', 'Portugal', 'China', 'Croácia']
            times = ['Santos', 'Palmeiras', 'Flamengo', 'Corinthians', 'Ceará', 'Fluminense', 'Internacional', 'Botafogo',
                      'Coritiba', 'Avaí', 'Barcelona', 'Liverpool', 'Juventos', 'Milan', 'Napoli', 'City', 'Tottenham', 'Arsenal',
                     'Chelsea', 'Newcastle', 'Everton', 'Valencia', 'Sevilla']
            frutas = ['BANANA', 'MAÇÃ', 'MELANCIA', 'ABACATE', 'UVA', 'PERA', 'LARANJA', 'MELÃO', 'MORANGO', 'ABACAXI',
                      'LIMÃO', 'Açaí', 'Acerola', 'Amora', 'Cajá', 'Cereja', 'Coco']
            objetos = ['colher', 'prato', 'mesa', 'celular', 'cama', 'travesseiro', 'computador', 'sapato', 'camisa',
                       'cobertor', 'relógio', 'faca', 'televisão', 'geladeira', 'fogão', 'fechadura', 'ventilador',
                       'carro', 'caneta', 'papel']
            animal = ['cachorro', 'gato', 'formiga', 'tartaruga', 'cavalo', 'onça', 'leão', 'tigre', 'pato', 'galinha',
                      'galo', 'abelha', 'golfinho', 'macaco', 'raposa', 'rato', 'vaca', 'ovelha', 'zebra', 'girafa',
                      'hiena', 'aranha', 'baleia', 'borboleta', 'cabra', 'camaleão', 'camelo', 'canguru', 'caranguejo',
                      'cobra', 'coelho', 'coruja', 'elefante', 'esquilo', 'jacaré', 'panda']
            lista = [paises, times, frutas, objetos, animal]
            escolhida = choice(lista)
            if escolhida == paises:
                print('\33[1;35mA palavra é um País\33[m')
            elif escolhida == frutas:
                print('\33[1;35mA palavra é uma Fruta\33[m')
            elif escolhida == objetos:
                print('\33[1;35mA palavra é um Objeto\33[m')
            elif escolhida == animal:
                print('\33[1;35mA palavra é um Animal\33[m')
            else:
                print('\33[1;35mA palavra é um time de Futebol\33[m')
            print()
            print('\33[1;34mTente adivinhar\33[m')
            palavra = choice(escolhida).strip().upper()
            letras = len(palavra)
            break
        print('Você tem 10 tentativas')
        while True:
            resp = str(input('Qual a palavra?')).strip().upper()
            if resp != palavra:
                print('Você errou...')
                cont += 1
                if cont == 2:
                    print()
                    print('Primeira dica:')
                    print(f'A palavra tem {letras} letras')
                if cont == 5:
                    print()
                    print('Segunda dica:')
                    print(f'A primeira letra é: {palavra[0]}')
                if cont == 7:
                    print()
                    print('Você desbloqueou uma ajuda!')
                    letra = str(
                        input('Digite uma letra para saber se está presente na PALAVRA MISTERIOSA:')).strip().upper()
                    print()
                    if letra in palavra:
                        print(f'A PALAVRA MISTERIOSA contém a letra: {letra}')
                    else:
                        print(f'A PALAVRA MISTERIOSA não contém a letra: {letra}')
                if cont == 10:
                    print('\033[1;31mQUE PENA, VOCÊ PERDEU!\033[m')
                    print(f'A palavra era: {palavra}')
                    break
            elif resp == palavra:
                print('\033[1;32mPARABÉNS, VOCÊ ACERTOU!\033[m')
                break
        continuar = int(input('''
[0] Jogar novamente
[1] voltar para o menu
opção:'''))
        print()
        if continuar == 1:
            sleep(2)
            print('\n'*5)
            break
    return
def munu_principal():
    while True:
        from time import sleep
        print('=-='*11)
        print('\t\t\33[1;36mMENU DE JOGOS\33[m')
        print('=-='*11)
        sleep(1)
        op = int(input("""\nEscolha um jogo:
    [1] PAR ou ÍMPAR
    [2] TENTE ADIVINHAR O NÙMERO
    [3] JOKENPÔ
    [4] JOGO DA VELHA
    [5] SOMA
    [6] PALAVRA MISTERIOSA
    
    \33[1;31m[9] ENCERRAR PROGRAMA\33[m
    OPÇÃO:"""))
        if op == 1:
            par_impar()
        elif op == 2:
            adv_num()
        elif op == 3:
            jokenpo()
        elif op == 4:
            jogo_da_velha()
        elif op == 5:
            soma()
        elif op == 6:
            palavra_mis()
        elif op == 9:
            break
    return
print('\t\33[1;32m\tSeja Bem Vindo!\33[m\n')
munu_principal()
