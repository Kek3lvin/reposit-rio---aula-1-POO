import math

a,b,c = map(float, input().split())

delta = b**2 - 4*a*c
r_del = math.sqrt(delta)

if delta < 0 and a == 0:
 print('Impossivel calcular')
else:
 r1 = -b + r_del /2 * a
 r2 = -b - r_del /2 * a
print(f'r1 = {r1:.5f}')
print(f'r2 = {r2:.5f}')
