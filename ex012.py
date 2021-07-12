# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

a = float(input('Qual o preço do produto? \n'))
v = a - (a * (5 / 100))

print(f'O valor com o desconto de 5% fica {v}')
