import math

#QUESTÃO 1
print('Digite seu nome abaixo:')
nome = input()
print(f'Bem-vindo(a) ao Python, {nome.split()[0]}')

#QUESTÃO 2
b1 = int(input("Digite aqui sua nota do primeiro bimestre:"))
b2 = int(input("Digite aqui sua nota do segundo bimestre:"))
média_parcial = (b1 * 2 + b2 * 3)//5
print(f'Essa é sua média na matéria semestral: {média_parcial}')

#QUESTÃO 3
print("\nCálculos com um retângulo")
base = int(input('base:'))
altura = int(input('altura:'))
área = (base * altura)
perímetro = (base * 2 + altura * 2)
diagonal = math.sqrt(base**2 + altura**2)
print(f'Aqui estão as medidas: Área = {área} - Perímetro = {perímetro} - Diagonal = {diagonal}')

#QUESTÃO 4
frase = input('Escreva uma frase:')
fim_palavra = frase.rsplit(maxsplit=1)[-1]
print(fim_palavra)