#JOGO DO ÍMPAR OU PAR
from random import randint as ri
print('\033[1;34m!!!JOGO DO ÍMPAR OU PAR!!!\n')

numCPU = ri(0, 10)
print('\033[1;97mCPU ESCOLHEU O NÚMERO!\n')

numPlayer = int(input('Digite um número: '))
escolhaPlayer = ''

num = numCPU + numPlayer
if num % 2 == 0:
    escolha = 'PAR'
else:
    escolha = 'IMPAR'

while True:
    escolhaPlayer = str(input('Escolha entre ÍMPAR e PAR: ')).strip().upper()
    if 'PAR' == escolhaPlayer or 'IMPAR' == escolhaPlayer or 'ÍMPAR' == escolhaPlayer:
        if escolhaPlayer == escolha:
            print('\033[1;32mVocê acertou! =)')
            print(f'\033[1;97mO número da CPU foi {numCPU} e o seu número foi {numPlayer}, somando temos {num}.')
            break
        else:
            print('\033[1;91mNão foi dessa vez! =(')
            print(f'\033[1;97mO número da CPU foi {numCPU} e o seu número foi {numPlayer}, somando temos {num}.')
            break
    else:
        print('Digite um caractere válido!')
print('\033[2;97;101m!!!GAME OVER!!!')