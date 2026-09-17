print("Exercicio 1")

valor_investimento = input("Qual o valor a investir? ")
valor_investimento = valor_investimento.replace("R$", "").replace(".", "").replace("," , ".")
valor_investimento = float(valor_investimento)

if valor_investimento < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor_investimento <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliarios")
else:
    valor_investimento > 5000
    print("Perfil arrojado: Sugerimos acoes")

print("Exercicio 2")

admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

login = input("E-mail de acesso ")
login = login.strip().lower()

if login in admins:
    print("Acesso liberado!")
else:
    print("Acesso negado, voce nao tem permissao de ADM")

print("Exercicio 3")

valor_compra = input("Qual o valor da compra? ")
valor_compra = valor_compra.replace("R$" , "").replace("." , "").replace("," ,".")
valor_compra = float(valor_compra)

if valor_compra > 500:
    print("Seu descontoe de 15%")
    perc_desc = 0.15
elif valor_compra > 200 and valor_compra < 500:
        print("Seu desconto e de 10%")
        perc_desc = 0.1
else:
     print("Sem desconto")
     perc_desc = 0

desconto = valor_compra * perc_desc
valor_total = valor_compra - desconto

print(f"O seu desconto foi de R${desconto} e o valor total e de R${valor_total}!")

print("Exercicio 4")

vendas_vendedor = input("Quantas vendas vc fez? ")
vendas_vendedor = float(vendas_vendedor)
meta_vendedor = 150
vendas_loja = input("Quantas vendas a loja fez? ")
vendas_loja = float(vendas_loja)
meta_loja = 500


if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    print("Parabens seeu bonus e de 20%!")
    perc_desco = 0.20
    bonus = vendas_vendedor *perc_desco
    print(f"E o total do seu bonus e R${bonus}")
else:
     print("Sem bonus :(")
     perc_desco = 0
     bonus = vendas_vendedor * perc_desco
     print(f"E o total do seu bonus e de R${bonus}")

print("Exercicio 5")

assunto_email = input("Qual o assunto do E-mail? ")
assunto_email = assunto_email.strip().lower()

if "pagamento" in assunto_email or "boleto" in assunto_email:
    print("Encaminhando para o financeiro")
elif "entrega" in assunto_email or "atraso" in assunto_email:
     print("Encaminhando para logistica")
else:
     print("Encaminhando para o suporte geral")