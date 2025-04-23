#QUESTÃO 1
def maior(x,y):
  k = max(x,y)
  return k
a = int(input()) 
b = int(input())
resultado = maior(a,b)
print(resultado)

#QUESTÃO 2
def maior(x,y,z):
  k = max(x,y,z)
  return k
a = int(input()) 
b = int(input())
c = int(input())
resultado = maior(a,b,c)
print(resultado)

# QUESTÇAO 3

def iniciais(nome):
    nomes = nome.split()  
    letras = [parte[0].upper() for parte in nomes]  
    return ''.join(letras)  

nome = input("Digite seu nome completo: ")
print("Suas iniciais são:", iniciais(nome))

# QUESTÃO 4
def aprovado(nota1,nota2):
   média = (nota1 * 2 + nota2 * 3)/5 >= 60
   return média
n1 = float(input())
n2 = float(input())
print(aprovado(n1,n2))

#QUESTÃO 5

def formatar_nome(nome):
    return nome.title()

nome = input("Digite seu nome completo: ")
print("Nome formatado:", formatar_nome(nome))

