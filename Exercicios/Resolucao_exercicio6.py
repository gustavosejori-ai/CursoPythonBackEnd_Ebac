print("Exercicio 1")

clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}

clientes["Alon"] = clientes["Alon"] + 1500

clientes["Marcos"] = 2000

print(clientes)

print("Exercicio 2")

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}

prd_est = input("Qual o nome do pruduto? ")
prd_est = prd_est.lower().strip()

if prd_est in estoque:
    print(f"Produto encontrado! {estoque[prd_est]} unidades restantes")
else:
    print("Produto nao encontrado no sistema")

print("Exercicio 3")

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

print(vendas_regiao.values())

fat_total = sum(vendas_regiao.values())
print(f"O faturamento total foi de R${fat_total}")

fat_med = fat_total / len(vendas_regiao.keys())
print(f"Seu faturamento medio foi de R${fat_med}")

print("Exercicio 4")

desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}

print(desempenho["Paula"])
notas_paula = sum(desempenho["Paula"])
med_paula = notas_paula / len(desempenho["Paula"])


print(f"A media de Paula foi de {med_paula}")

print("Exercicio 5")

produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}

print(produtos["radio"])
produtos.pop("radio")


item_existe = "celular" in produtos 
print("Celular no estoque?",item_existe)
print(produtos)

