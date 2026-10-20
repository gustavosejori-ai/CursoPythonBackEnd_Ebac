Pokemons = {}
historico_capturas = []

def adicionar_pokemon():
    pokemon = input("Qual o nome do Pokemon? ").title().strip()
    if pokemon in Pokemons:
        print("Este Pokemon ja foi registrado antes!")
    else:
        tipo = input("Qual o tipo desse Pokemon? ")
        while True:
            try:
                nivel = int(input("Qual o nivel desse Pokemon? "))
                if 1 <= nivel <= 100:
                    break
                else:
                    print("Digite um nivel entre 1 e 100!")
            except ValueError:
                print("Entrada invalida! Digite um numero inteiro.")
        Pokemons[pokemon] = {
            "Tipo":tipo,
            "Nivel":nivel,
            "Capturas":0}
        print("Pokemon adicionado com sucesso!")

def list_pokemon():
    if not Pokemons:
        print("Nenhum Pokemon cadastrado!")
    else:
        pokemon_ordenados = sorted(Pokemons.items())
        for pokemon, informacao_pokmeon in pokemon_ordenados:
            print(
                f"Nome: {pokemon} | "
                f"Tipo: {informacao_pokmeon['Tipo']} | "
                f"Nivel: {informacao_pokmeon['Nivel']} | "
                f"Captura: {informacao_pokmeon['Capturas']}")

def remover_pokemon():
    rem_pokemon = input("Qual o nome do Pokemon a ser removido? ").strip().title()
    if rem_pokemon in Pokemons:
        Pokemons.pop(rem_pokemon)
        print("Pokemon removido com sucesso!")
    else:
        print("Pokemon nao encontrado!")

def atualizar_nivel():
    pokemon = input("Qual o nome do Pokemon que vai ter o nivel atualizado? ").strip().title()
    if pokemon in Pokemons:
        while True:
            try:
                nivel_novo = int(input("Qual o nivel desse Pokemon? "))
                if 1 <= nivel_novo <= 100:
                    break
                else:
                    print("Digite um nivel entre 1 e 100!")
            except ValueError:
                print("Entrada invalida! Digite um numero inteiro.")
        Pokemons[pokemon]['Nivel'] =nivel_novo
        print("Nivel atualizado com sucesso!")
    else:
        print("Pokemon nao encontrado!")

def regis_capt():
    pokemon_capt = input("Qual Pokemon voce capturou? ").title().strip()
    if pokemon_capt not in Pokemons:
        print("Esse Pokemon nao tem registro!")
    else:
        while True:
            try:
                quant_capt = int(input("Quantos desse Pokemon voce capturou? "))
                if quant_capt >0:
                    break
                else:
                    print("Digite um numero de capturas valido!")
            except ValueError:
                print("Entrada invalida! Digite um numero inteiro.")
        Pokemons[pokemon_capt]['Capturas'] += quant_capt
        historico_capturas.append({
            "Pokemon" : pokemon_capt,
            "Quantidade" : quant_capt
        })
        print("Captura registrada com sucesso! Gotta catch 'em all!!!")

def mostrar_historico_capturas():
    if not historico_capturas:
        print("Nenhuma captura foi registrada ainda!")
    else:
        for captura in historico_capturas:
            print(f"Pokemon: {captura['Pokemon']} | Quantidade capturada: {captura['Quantidade']}")

while True:
    print("1 - Adicionar Pokemon")
    print("2 - Listar Pokemon")
    print("3 - Remover Pokemon")        
    print("4 - Atualizar Nivel")
    print("5 - Registrar Captura")
    print("6 - Exibir Historico de Captura")
    print("7 - Sair")
    escolha = input("Qual opcao voce deseja? ")
    if escolha == "1":
        adicionar_pokemon()
    elif escolha == "2":
        list_pokemon()
    elif escolha == "3":
        remover_pokemon()
    elif escolha == "4":
        atualizar_nivel()
    elif escolha == "5":
        regis_capt()
    elif escolha == "6":
        mostrar_historico_capturas()
    elif escolha == "7":
        print("Pokedex desligando...")
        break
    else:
        print("Opcao invalida!")