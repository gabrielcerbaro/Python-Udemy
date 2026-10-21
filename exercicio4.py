nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if idade:
    idade_int = int(idade)

espacos = nome.count(' ')

if nome and idade: 
    print(f'{nome}, seu nome invertido é {nome[::-1]} seu nome tem {espacos} espaços e no total tem {len(nome)} letras. '
          f'A primeira letra do seu nome é {nome[0].upper()} e a última é {nome[-1].upper()}')
else: 
    print('Desculpe, você deixou campos vazios.')