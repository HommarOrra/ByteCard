import use_cases

todos_os_cartoes = use_cases.lista_cartoes()
print(f'Cartões pré-cadastrados: {len(todos_os_cartoes)}')

cartao_existente = use_cases.pesquisa_cartao_por_id(1)
cartao_inexistente = use_cases.pesquisa_cartao_por_id(1000)

print(f'Cartão existente: {cartao_existente}')
print(f'Cartão existente: {cartao_inexistente}')

use_cases.cadastra_cartao("João Miron", 5500.0)
for cartao in use_cases.lista_cartoes():
    print(cartao)

use_cases.cadastra_compra(2, 100.0, 'Alimentação', 'Pizzaria Romana')
use_cases.cadastra_compra(2, 150.0, 'Lazer', 'Show de jazz')
use_cases.cadastra_compra(3, 200.0, 'Alimentação', 'Rodízio de frutos do mar')
use_cases.cadastra_compra(3, 250.0, 'Lazer', 'Show de rock')
use_cases.cadastra_compra(3, 300.0, 'Educação', 'Assinatura da Alura')

for compra in use_cases.lista_compras():
    print(compra)

gastos_por_categoria = use_cases.monta_relatorio_gastos_por_categoria()

for categoria, total in gastos_por_categoria.items():
    print("Gastos por categoria:")
    print(categoria, "-", total)