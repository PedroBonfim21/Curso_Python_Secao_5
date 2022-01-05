operação=input("Escolha uma das opções: \n(+)Adiçao\n(-)Subtração\n(*)Multiplicação\n(/)Divisão\nDigite a operação: ")
num1=float(input("Digite um número: "))
num2=float(input("Digite um número: "))
if operação == "+":
    resultado = (num1 + num2)
    print(f"o resultado é: {resultado}.")
elif operação == "-":
    resultado = (num1 - num2)
    print(f"o resultado é: {resultado}.")
elif operação == "/":
    resultado = (num1 / num2)
    print(f"o resultado é: {resultado}.")
elif operação == "*":
    resultado = (num1 * num2)
else:
    print("Operação invalida")
