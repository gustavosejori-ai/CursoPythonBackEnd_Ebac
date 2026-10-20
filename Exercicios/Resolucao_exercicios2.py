print("Exercicio_1")

faturamento = 45000
custo = 23500

lucro = faturamento - custo
margem_lucro = lucro / faturamento

texto = f"O lucro foi de R${lucro:,.2f} e a margem de lucro foi de{margem_lucro: .0%}"
print(texto)

print("Exercicio_2")

nome = " mArCoS aNtOnIo rOcHa"
email = " MARCOS.ROCHA@GMAIL.COM"

nome = nome.title().strip()
email = email.lower().strip()

print(nome)
print(email)

print("Exercicio_3")

novo_dominio = "@grupocorp.com"
email = "andre_silva@empresa.com.br."

email = email.replace("empresa.com.br" , "grupocorp.com")
print(email)

posicao_a = email.find("@")
print(posicao_a)

email = email[:posicao_a] + novo_dominio
print(email)

print("Exercicio_4")

email = "beatriz.oliveira@grupocorp.com"

posicao_a = email.find("@")
print(posicao_a)
username = email[:posicao_a]
print(username)


print("Exercicio_5")

nome = "lucas ferreira souza"
mensagem = "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"

posicao_a = nome.find(" ")
pri_nome = nome[:posicao_a].capitalize()
mensagem = mensagem.replace("[Primeiro Nome]" , pri_nome)
print(mensagem)