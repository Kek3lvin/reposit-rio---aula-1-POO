#QUESTÃO 1
a = int(input())
b = int(input())

x = a + b

print(f'X = {x}')

#QUESTÃO 2
a = float(input()) 
b = float(input())

MEDIA = (a * 3.5 +  b * 7.5) / 11

print(f'MEDIA = {MEDIA:.5f}')

#QUESTÃO 3
raio = float(input())
pi = 3.14159

volume = (4/3.0) * pi * (raio**3)

print(f"VOLUME = {volume:.3f}")

#QUESTÃO 4
c,n =map(int, input().split())

fim = c % n

print(fim)

#QUESTÃO  5

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'{d:.4f}')

#QUESTÃO 6

ap = t1 + t2 + t3 + t4 - 3

print(ap)