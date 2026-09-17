produtos_estoque = {}



def adicionar_produto():
    produto = input("Qual o nome do produto? ").title().strip()
    quantidade = int(input("Qual a quantidade? "))
    preco = float(input("Qual o preco? ").replace(".", "").replace(",","."))
    produtos_estoque[produto] = {"Quantidade": quantidade, "Preco":preco}

def listar_produtos():
    produtos_ordenados = sorted(produtos_estoque.items(), key=lambda item:item[0])
    for nome_produto, informacoes_produto in produtos_ordenados:
        print(f"Produto {nome_produto}: Quantidade {informacoes_produto['Quantidade']} - Preco ${informacoes_produto['Preco']}")

def remover_produto():
    prod_rem = input("Qual produto a ser removido? ").title().strip()
    if prod_rem in produtos_estoque:
        produtos_estoque.pop(prod_rem)
        print("Produto removido!")
    else:
        print("Erro, produto nao encontrado!")

def atualizar_quant():
    produto = input("Qual o produto que deseja atualizar? ").strip().title()
    if produto in  produtos_estoque:
        nova_quant = int(input("Qual a nova quantidade? "))
        produtos_estoque[produto]["Quantidade"] = nova_quant
    else:
        print("Erro, produto nao encontrado!")

while True:
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("4 - Atualizar quantidade")
    print("5 - Sair")
    escolha = input("Escolha uma opcao: ")
    if escolha == "1":
        adicionar_produto()
    elif escolha == "2":
        listar_produtos()
    elif escolha == "3":
        remover_produto()
    elif escolha == "4":
        atualizar_quant()
    elif escolha == "5":
        break
    else:
        print("Opcao invalida!")






