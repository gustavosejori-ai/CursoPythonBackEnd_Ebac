print("Exercicio 1")

coordenadas = (-23.5505, -46.6333)

latitude,longitude = coordenadas
print(f"Iniciando entrega. Latitude {latitude}, Longitude {longitude}")

print("Exercicio 2")

def calcular_folha(salario):
    imposto = 0.1
    desconto = salario * imposto
    salario_liquido = salario - desconto
    return desconto , salario_liquido

salario = 5000

des_salario , salario_liq = calcular_folha(salario)
print(f"O desconto foi de R${des_salario} e o salario liquido e de R${salario_liq}")

print("Exercicio 3")

vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]

for item, preco_unitario, quantidade in vendas_dia:
    print(f"Produto {item} | Total: R$ {preco_unitario*quantidade}") 



print("Exercicio 4")

dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}



def analisar_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return total_vendas , media_vendas

for filial in dados_filiais:
    vendas_filial = dados_filiais[filial]
    total_vendas_filial , media_vendas_filial = analisar_vendas(vendas_filial)
    print(f"Filial {filial} -> Total: R${total_vendas_filial}, Media: R${media_vendas_filial}")


print("Exercicio 5")

def resumo_chamados(lista_tempos_chamados):
    qtde_chamados = len(lista_tempos_chamados)
    tempo_maximo = max(lista_tempos_chamados)
    return qtde_chamados, tempo_maximo

tempos = [15, 45, 10, 120, 30]
qtde, tempo_maximo = resumo_chamados(tempos)

print(f"Foram abertos {qtde} chamados hoje. Tempo Máximo de SLA: {tempo_maximo} minutos")

