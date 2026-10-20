print("Caluculadora Iniciada")
import math


while True:
    operador = input("Escolha um operador valido (+, -, *, /, ^, sqrt) ou digite sair!: ")
    operador = operador.lower().strip()

    if operador == "sair":
        print("Calculadora Encerrada!!!")
        break

    elif operador == "sqrt":
        num_um = float(input("Qual numero voce quer tirar a raiz? "))
        resultado = math.sqrt(num_um)
        print(f"Seu resultado e {resultado}")
    elif operador == "+":
        num_um = float(input("Qual o primeiro numero? "))
        num_dois = float(input("Qual o segundo numero? "))
        resultado = num_um + num_dois
        print(f"Seu resultado e {resultado}")
    elif operador == "-":
        num_um = float(input("Qual o primeiro numero? "))
        num_dois = float(input("Qual o segundo numero? "))
        resultado = num_um - num_dois
        print(f"Seu resultado e {resultado}")
    elif operador == "/":
        num_um = float(input("Qual o primeiro numero? "))
        num_dois = float(input("Qual o segundo numero? "))
        resultado = num_um / num_dois
        print(f"Seu resultado e {resultado}")
    elif operador == "*":
        num_um = float(input("Qual o primeiro numero? "))
        num_dois = float(input("Qual o segundo numero? "))
        resultado = num_um * num_dois
        print(f"Seu resultado e {resultado}")
    elif operador == "^":
        num_um = float(input("Qual o primeiro numero? "))
        num_dois = float(input("Qual o segundo numero? "))
        resultado = num_um**num_dois
        print(f"Seu resultado e {resultado}")
    else:
        print("Operador invalido escolha outro!")
