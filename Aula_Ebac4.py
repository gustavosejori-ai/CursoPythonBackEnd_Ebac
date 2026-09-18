livros = {}
historico_emprestimos = []

def adicionar_livro():
    livro = input("Qual o nome do livro? ").title().strip()
    autor_livro = input("Qual o autor do livro? ")
    quantidade = int(input("Qual a quantidade disponivel? "))
    livros[livro] = {"Autor" : autor_livro, "Quantidade": quantidade,}

def listar_livro():
    livros_ordenados = sorted(livros.items())
    for livro, informacao_livro in livros_ordenados:
        print(f"Livro {livro}, escrito por {informacao_livro['Autor']}, temos {informacao_livro['Quantidade']} unidades!")

def remover_livro():
    livro_a_remover = input("Qual o nome do livro que pretende remover? ").strip().title()
    if livro_a_remover in livros:
        livros.pop(livro_a_remover)
        print(f"Livro {livro_a_remover} removido com sucesso!")
    else:
        print(f"Erro,{livro_a_remover} nao encontrado!")

def atualizar_quant():
    livro = input("Qual o livro que deseja atualizar? ").strip().title()
    if livro in livros:
        nova_quant = int(input("Qual a nova quantidade? "))
        livros[livro]["Quantidade"] = nova_quant
        print(f"Livro {livro} atualizado com sucesso!")
    else:
        print(f"Erro, livro {livro} nao encontrdo!")

def register_emprestimo():
    nome_livro = input("Qual o titulo do livro? ").title().strip()
    if nome_livro in livros:
        quant_para_emprestar = int(input("Quantos livros vao ser emprestados? "))
        if quant_para_emprestar <= livros[nome_livro]["Quantidade"]:
            historico_emprestimos.append([nome_livro,quant_para_emprestar])
            livros[nome_livro]["Quantidade"] = livros[nome_livro]["Quantidade"] - quant_para_emprestar
            print("Emprestimo realizado!")
        else:
            print(f"Numero de exemplares do livro {nome_livro} insuficiente para esse emprestimo!")
    else:
        print(f"Erro, livro {nome_livro} nao encontrado!")

def exibir_historico():
    if not historico_emprestimos:
        print("Nenhum historico registrado!")
    else:
        for livro,quantidade in historico_emprestimos:
            print(f"Livro: {livro} | Quantidade emprestada: {quantidade}")

while True:
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Remover livro")        
    print("4 - Atualizar quantidade")
    print("5 - Registrar emprestimo")
    print("6 - Exibir historico")
    print("7 - Sair")
    escolha = input("Qual opcao voce deseja? ")
    if escolha == "1":
        adicionar_livro()
    elif escolha == "2":
        listar_livro()
    elif escolha == "3":
        remover_livro()
    elif escolha == "4":
        atualizar_quant()
    elif escolha == "5":
        register_emprestimo()
    elif escolha == "6":
        exibir_historico()
    elif escolha == "7":
        break
    else:
        print("Opcao invalida!")