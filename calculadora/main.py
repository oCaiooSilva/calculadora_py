numero1 = float(input("digite um numero: "))
numero2 = float(input("digite um numero: "))

print("escolha uma operação:")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

operacao = input("digite o numero da operação desejada: ")

if operacao == "1":
    resultado = numero1 + numero2
    print(f"resultado da soma: {resultado}")
elif operacao == "2":
    resultado = numero1 - numero2
    print(f"resultado da subtração: {resultado}")
elif operacao == "3":
    resultado = numero1 * numero2
    print(f"resultado da multiplicação: {resultado}")
elif operacao == "4":
    resultado = numero1 / numero2
    print(f"resultado da divisão: {resultado}")

