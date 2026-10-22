"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um número inteiro: ")

# if numero.isdigit():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'O número {numero_int} é par.')
#     else:
#         print(f'O número {numero_int} é ímpar')
# else:
#     print('O valor digitado não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Insira uma hora em formato de número inteiro positivo: ')

# try:
#     hora_int = int(hora)

#     if hora_int >= 0 and hora_int <= 11:
#         print(f'Bom dia, ainda são {hora_int}h')
#     elif hora_int >= 12 and hora_int <= 17:
#         print(f'Boa tarde, já são {hora_int}h')
#     elif hora_int >= 18 and hora_int <= 23:
#         print(f'Boa noite, são {hora_int}h')
#     else:
#         print('Não conheço esse horário')
# except:
#     print(f'O valor: {hora} não é um valor real, por gentileza, informar um número inteiro positivo')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual o seu primeiro nome: ')
qtd_letras_nome = len(nome)

if qtd_letras_nome > 1:
    if qtd_letras_nome <= 4:
        print('O seu nome é curto')
    elif qtd_letras_nome <= 6:
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito grande')
else:
    print('Coloque um nome real')