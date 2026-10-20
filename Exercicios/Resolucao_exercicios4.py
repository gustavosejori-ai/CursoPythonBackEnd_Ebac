print("Exercicio 1")

vendas = [1500, 2000, 800, 3500, 1200]

maior_venda = max(vendas)
menor_venda = min(vendas)
total_vendas = sum(vendas)
media_diaria = total_vendas / len(vendas)

print("O total foi de R$",total_vendas)
print("A media de vendas foi de R$",media_diaria)
print("O maior valor e de R$",maior_venda)
print("O menor valor e de R$",menor_venda)

print("Exercicio 2")

estoque = ["monitor", "teclado", "mouse", "headset"]

estoque.append("webcam")
posicao_teclado = estoque.index("teclado")
estoque[posicao_teclado] = "teclado mecanico"

impressora_tem = "impressora"in estoque
print("Tem impressora no estoque?",impressora_tem)

estoque.remove("mouse")

print(estoque)

print("Exercicio 3")

fretes = [50, 80, 20, 150, 40]

fretes.sort(reverse=True)
print(fretes)
top_list = fretes[:2]
print(top_list)

print("Exercicio 4")

rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]

rota.extend (novas_cidades)
posicao_sorocaba = rota.index("Sorocaba")+1

print(rota)
print(posicao_sorocaba)
print(f"Sorocaba e a {posicao_sorocaba}* cidade da rota")

print("Exercicio 5")

precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto","Champagne"]

vinho_escolido = input("Qual vinho a ser alterado? ")
preco_novo = input("Qual o novo valor? ")
preco_novo = preco_novo.replace("R$", "").replace(".","").replace(",",".")
preco_novo = float(preco_novo)

posicao_vinho = vinhos.index(vinho_escolido)
precos[posicao_vinho] = preco_novo

print(vinhos)
print(precos)