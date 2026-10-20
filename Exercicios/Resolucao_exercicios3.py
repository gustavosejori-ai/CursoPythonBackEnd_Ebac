print("Exercicio_1")

valor_bruto = input("Digite o faturamento:")
valor_bruto = valor_bruto.replace("R$"," ").replace(".","").replace(",",".")
valor_bruto = float(valor_bruto)
print(valor_bruto)

per_imp = 0.15
imposto = valor_bruto*per_imp

print(f"O valor do imposto foi de R${imposto:,.2f}")

print("Exercicio_2")

nome = input("Qual o nome do colaborador? ")
email_colaborador = input("Qual o e-mail do colaborador? ")

nome = nome.strip()
email_colaborador = email_colaborador.strip().lower()

espaco_a = nome.find(" ")
pri_nome = nome[ :espaco_a].capitalize()

mensagem = ("Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]")
mensagem = mensagem.replace("[Primeiro Nome]", pri_nome).replace("[E-mail padronizado]" , email_colaborador)
print(mensagem)

print("Exercicio_3")

faturamento_A = input("Qual o faturamento da loja A: ")
faturamento_B = input("Qual o faturamento da loja B: ")

faturamento_A = faturamento_A.replace("R$","").replace(".","").replace(",",".")
faturamento_A = float(faturamento_A)

faturamento_B = faturamento_B.replace("R$","").replace(".","").replace(",",".")
faturamento_B = float(faturamento_B)

fat_total = faturamento_A + faturamento_B
fat_med = fat_total / 2

print(f"O faturamento total foi de R$ {fat_total:,.2f} e a media foi de R${fat_med:,.2f}")