#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
v = []
c = 0
c2 = []

for i in range(10):
  n = input('{}/10 - Digite uma letra:'.format(i+1))
  v.append(n)

for i in range(10):
  if (v[i] == 'a' or 'e' or 'i' or 'u'):
    c = +1
    c2.append(v[i])