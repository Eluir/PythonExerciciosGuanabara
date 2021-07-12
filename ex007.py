# Desenvolva um programa que leia as notas de um aluno, calcule e mostre sua média.

a = int(input('Digite sua nota do primeiro bimestre \n'))
b = int(input('Digite sua nota do segundo bimestre \n'))
c = int(input('Digite sua nota do terceiro bimestre \n'))
d = int(input('Digite sua nota do quarto bimestre \n'))
media = (a + b + c + d) / 4

print(f'Sua média foi de: {media}')
