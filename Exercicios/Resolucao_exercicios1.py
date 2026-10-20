

print("EXERCICIO 1")
faturamento_inicial = 50000

bonus = 0.10*faturamento_inicial
faturamento_final = faturamento_inicial - bonus
print("O bonus da impresa foi de",bonus,"reais, e o faturamento final foi de",faturamento_final,"reais!")


print("EXERCICIO 2")
estoque_inicial = 250
vendas_dia = 78
fornecimento = 100
estoque_final = estoque_inicial - vendas_dia + fornecimento
print("O estoque contem", estoque_final, "smartphones restantes")


print("EXERCICIO 3")
caixas_levar = 1250
caminhao = caixas_levar // 12
sobra_caixa = caixas_levar %12
print(caminhao,"caminhoes necessarios para levar a carga e um caminhao carregando", sobra_caixa, "caixas")


print("EXERCICIO 4")
fat = 15000
custos_fixos = 5000
perc_imp =0.15

imposto = fat*perc_imp
lucro_liquido = fat - custos_fixos - imposto
margem_lucro = lucro_liquido / fat
meta_batida = margem_lucro >0.3
print("Seu lucro foi de ", lucro_liquido,"reais, e sua margem de lucro e de ",margem_lucro)
print("Meta batida?", meta_batida)


print("EXERCICIO 5")
contrato = 40
anos = contrato //12
meses = contrato %12
print("Ainda resta",anos,"anos e ",meses,"meses")