# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

a = float(input(f'Digite seu salário atual \n'))
b = a + (a * (15 / 100))

print(f'Seu salário após os 15% de aumento será: {b}')
