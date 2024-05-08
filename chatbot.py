import requests
import random
import os

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'

resposta = requests.get(url)

while True:

    os.system('cls||clear')

    data = resposta.json()
    valor_secreto = random.choice(data)
    palavra_secreta = valor_secreto['palavra']
    dica = valor_secreto['dica']

    print(f'A palavra secreta tem {len(palavra_secreta)} letras')
    print(f'A dica é {dica}')
    chute = input('Seu chute: ')

    if chute == palavra_secreta:
        print('Acertou')
    else:
        print(f'Errou... a palavra secreta era {palavra_secreta}')

    continuar = input('Deseja continuar? s/n ')
    if continuar == 'n':
        break

    print('\n')

