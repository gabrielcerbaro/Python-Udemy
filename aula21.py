# Resumo: Solicita uma senha, compara com a senha permitida e demonstra o uso do operador lógico 'not'.
senha = input("Senha: ")

if not senha == "123456":
    print('Senha incorreta')
else: 
    print('Senha correta')

# print(not True) # False
# print(not False) # True
