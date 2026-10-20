print("Exercico 1")

produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", " caixa de som bluetooth " ]

def padronizar_texto(texto):
    texto = texto.strip()
    texto = texto.title()
    return texto

produtos_padronizados = []
for produto in produtos_baguncados:
    produtos_padronizado = padronizar_texto(produto)
    produtos_padronizados.append(produtos_padronizado)
print(produtos_padronizados)

print("Exercicio 2")

def calcular_iss(valor):
    if valor > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
    imposto = valor * taxa
    return imposto

print(calcular_iss(8000))
print(calcular_iss(2000))

print("Exercicio 3")

def analisar_margem(faturamento, custo):
    lucro = faturamento - custo
    margem = lucro / faturamento
    if margem >= 0.3:
        return "Margem Saudavel"
    else:
        return "Margem Baixa"
    

print(analisar_margem(10000,6000))

print("Exercicio 4")

equipe_vendas = { "João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200, "Paulo": 5000 }; meta_objetivo = 10000

def quem_bateu_meta(vendas_vendedores : dict, meta: float):
    for vendedor in vendas_vendedores:
        if vendas_vendedores[vendedor] >= meta:
            print(f"Vendedor {vendedor} bateu meta!")

meta = 10000
quem_bateu_meta(equipe_vendas, meta)

print("Exercicio 5")

def converter_para_real(valor_em_dolares, cotacao_dolar):
    valor_em_real = valor_em_dolares * cotacao_dolar
    return valor_em_real

def processar_lista_precos(lista_precos_dolar, cotacao_dolar):
    for item in lista_precos_dolar:
        valor_reais = converter_para_real(item, cotacao_dolar)
        print(f"O item custa US${item} e em reais: R${valor_reais}")

precos_usd = [100, 50, 250]
cotacao_dolar = 5.20

processar_lista_precos(precos_usd, cotacao_dolar)
