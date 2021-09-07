# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

k = float(input('Quantos Km foram percorridos? \n'))
d = int(input('Quantos dias de alguel? \n'))
custo_aluguel_dia = 60
custo_km_rodado = 0.15

total_valor_km = k * 0.15
total_valor_aluguel = d * custo_aluguel_dia

total_despesa = total_valor_km + total_valor_aluguel

print(f'Você tem a pagar um total de: R$ {total_despesa:.2f}.')
print(    f'Sendo o valor composto por: R$ {total_valor_km:.2f} referente ao Km rodado e R$ {total_valor_aluguel:.2f} pelo aluguel.')
