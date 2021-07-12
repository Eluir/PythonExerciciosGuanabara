# Faça um programa que leia um numero qualquer e mostre sua tabuada.

a = int(input('Digite um número\n'))
c = 1

while c < 11:
    print(f'{a} x {c} = {a * c}')
    c = c + 1
