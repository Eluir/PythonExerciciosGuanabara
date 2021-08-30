##Faça um programa q leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintar sabendo q cada 1l de tinta pinta uma area de 2m²

alt = float(input('Qual a altura da parede?\n'))
lar = float(input(f'Qual a largura da parede? \n'))
a = alt * lar
t = a // 2

print(f'A área da parede é {a :.2f}m² e serão necessários {t : .0f} litros de tinta para pintá-la.')
