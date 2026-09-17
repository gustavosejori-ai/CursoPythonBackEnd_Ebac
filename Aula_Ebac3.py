# soma = lambda x,y : x + y
# subtracao = lambda x,y : x - y
# divisao = lambda x,y : x / y
# multiplicacao = lambda x,y : x * y

# while True:
#     print("Calculadora iniciada!")
#     try:
#         num_1 = float(input("Qual o primeiro numero? "))
#         num_2 = float(input("Qual o segundo numero? "))
#     except ValueError:
#                 print("Coloque um numero valido!")
#                 continue
#     operacoes = ["Soma", "Subtracao", "Multiplicacao", "Divisao"]
#     menu = [f"{i + 1} - {operacao}" for i, operacao in enumerate(operacoes)]
#     for opcao in menu:
#            print(opcao)
#     operador = int(input("Escolha uma opcao! "))
#     if operador == 1:
#            resultado = soma(num_1,num_2)
#            print(f"Seu resultado e {resultado}")
#     elif operador == 2:
#             resultado = subtracao(num_1,num_2)
#             print(f"Seu resultado e {resultado}")
#     elif operador == 3:
#            resultado = multiplicacao(num_1,num_2)
#            print(f"Seu resultado e {resultado}")
#     elif operador == 4:
#            try:
#                 resultado = divisao(num_1,num_2)
#                 print(f"Seu resultado e,{resultado}")
#            except ZeroDivisionError:
#                   print("Nao existe divisao por zero!")
#                   while num_2 == 0:
#                     num_2 = float(input("Escolha um numero denovo! "))
#                     if num_2 == 0:
#                         print("Nao pode ser zero! ")
#                     resultado = divisao(num_1,num_2)
#                     print(f"Seu resultado e {resultado}")
#     else:
#            print("Digite uma operacao valida!")
#            continue

#     continuar = input("Deseja realizar outra operacao? (S/N):").strip().upper()
#     if continuar == "N":
#           print("Calculadora encerrada! ")
#           break
#     elif continuar == "S":
#           continue
#     else:
#          print("Opcao invalida! Digite S ou N")
         

while True:

    # Entrada dos números
    while True:
        try:
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            break
        except ValueError:
            print("Erro: insira apenas números válidos.")

    # Operações usando funções lambda
    operacoes = {
        "Soma": lambda a, b: a + b,
        "Subtração": lambda a, b: a - b,
        "Multiplicação": lambda a, b: a * b,
        "Divisão": lambda a, b: a / b
    }

    # Menu usando list comprehension
    opcoes = [f"{i + 1} - {operacao}" for i, operacao in enumerate(operacoes)]

    print("\nEscolha uma operação:")
    print("\n".join(opcoes))

    # Escolha da operação
    while True:
        escolha = input("Digite o número da operação: ")

        if escolha in ["1", "2", "3", "4"]:
            break
        else:
            print("Erro: operação inválida. Escolha uma opção de 1 a 4.")

    nome_operacao = list(operacoes.keys())[int(escolha) - 1]

    print(f"Você escolheu: {nome_operacao}")

    # Tratamento da divisão por zero
    if nome_operacao == "Divisão":
        while num2 == 0:
            try:
                num2 = float(input(
                    "Divisão por zero não é permitida. "
                    "Por favor, insira outro número: "
                ))

                if num2 == 0:
                    print("Erro: o divisor não pode ser zero.")

            except ValueError:
                print("Erro: insira apenas um número válido.")

    # Realiza a operação
    resultado = operacoes[nome_operacao](num1, num2)

    print(f"O resultado é: {resultado}")

    # Pergunta se deseja continuar
    while True:
        continuar = input(
            "Deseja realizar outra operação? (S/N): "
        ).strip().upper()

        if continuar == "S":
            break
        elif continuar == "N":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Digite apenas S ou N.")

    if continuar == "N":
        break
