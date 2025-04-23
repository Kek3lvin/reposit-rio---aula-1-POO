# 1036
import math

A, B, C = map(float, input().split())

if A == 0 or (B**2 - 4*A*C) < 0:
    print("Impossivel calcular")
else:
    delta = B**2 - 4*A*C

    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
a,b = map(int, input().split())

# 1044
if a % b == 0 or b % a == 0:
    print('São multiplos')
else:
    print('Não sao multiplos')

# 1049
classe = input()
tipo = input()
dieta = input()

if classe == "vertebrado":
    if tipo == "mamifero":
        if dieta == "onivoro":
            print("homem")
        elif dieta == "herbivoro":
            print("vaca")
    elif tipo == "ave":
        if dieta == "carnivoro":
            print("aguia")
        elif dieta == "onivoro":
            print("pomba")
elif classe == "invertebrado":
    if tipo == "anelideo":
        if dieta == "hematofago":
            print("sanguessuga")
        elif dieta == "onivoro":
            print("minhoca")
    elif tipo == "inseto":
        if dieta == "hematofago":
            print("pulga")
        elif dieta == "herbivoro":
            print("lagarta")

# 1050
DDD = int(input())

if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
    
# 2424
x,y = map(int, input().split())

x,y = map(int, input().split())

if 0 <= x <= 432 and 0 <= y <= 468:
    print("dentro")
else:
    print("fora")

# 2670
A1 = int(input())
A2 = int(input())
A3 = int(input())


tempo_no_andar_1 = 0 * A1 + 2 * A2 + 4 * A3
tempo_no_andar_2 = 2 * A1 + 0 * A2 + 2 * A3
tempo_no_andar_3 = 4 * A1 + 2 * A2 + 0 * A3


menor_tempo = min(tempo_no_andar_1, tempo_no_andar_2, tempo_no_andar_3)


print(menor_tempo)

# 1059
for x in range(1,101):
    if x % 2 == 0:
        print(x)

# 1080
maior_valor = 0
posicao = 0

for i in range(1, 101):
    valor = int(input())
    if valor > maior_valor:
        maior_valor = valor
        posicao = i

print(maior_valor)
print(posicao)

# 1094
N = int(input())

total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0


for _ in range(N):
 entrada = input().split()
 Quantia = int(entrada[0])
 Tipo = entrada[1]

 total_cobaias += Quantia
 if Tipo == 'R':
     total_ratos += Quantia
 elif Tipo == 'S':
     total_sapos += Quantia
 elif Tipo == 'C':
     total_coelhos += Quantia


percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100


print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")

# 1114
senha = int(input())
correta = 2002

while senha != correta:
  print('Senha Invalida')
  senha = int(input())
  if senha == correta:
      print('Acesso Permitido')

# 1116
N = int(input()) 

for i in range(N):
    entrada = list(map(int, input().split()))  
    if entrada[1] == 0:  
        print('divisao impossivel')
    else:
        divisao = entrada[0] / entrada[1]  
        print(f'{divisao:.1f}') 

# 1151
N = int(input())

if 0 < N < 46:
    fibonacci = []
    a, b = 0, 1

    for i in range(N):
        fibonacci.append(a)
        a, b = b, a + b

    print(' '.join(map(str, fibonacci)))
