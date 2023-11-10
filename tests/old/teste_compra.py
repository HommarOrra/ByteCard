from datetime import datetime, date 
from model import Compra, Cartao, CompraCredito 

visa = Cartao(
    '1111 1111 1111 1111',
    date(2031, 1, 31),
    '321',
    1000.0,
    'Larissa Balduino') 

compra_farmacia = Compra(
    100.0,
    datetime(2023, 1, 1, 10, 0, 0),
    'Droga Raia',
    'Saúde',
    visa) 

compra_restaurante = Compra(
    89.9,
    datetime(2023, 1, 2, 12, 15, 0),
    'Caetanos Bar', 
'Lazer',
visa) 

compra_supermercado = Compra(
    475.5,
    datetime(2023, 2, 3, 7, 5, 5),
    'Sonda',
'Alimentação',
visa) 

print(compra_farmacia) 
print(compra_restaurante) 
print(compra_supermercado) 
print() 

compra_mercado_livre = CompraCredito(
    1000.0,
    datetime(2023, 2, 15, 19, 46, 17),
    'Mercado Livre',
    'Casa',
    visa,
    10) 

print(f'Compra a crédito: {compra_mercado_livre.valor} em {compra_mercado_livre.quantidade_parcelas}x de {compra_mercado_livre.valor_parcela}') 
print() 
fatura = [compra_farmacia, compra_restaurante, compra_supermercado, compra_mercado_livre] 
total = 0 
for compra in fatura:
    total += compra.valor 

print(f'O total da fatura é: {total}') 
