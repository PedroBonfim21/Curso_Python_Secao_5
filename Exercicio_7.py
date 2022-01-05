num1=float(input("Digite um número: "))
num2=float(input("Digite um número: "))
if num1>num2:
    print(f"primeiro número({num1}) maior que o segundo({num2}).")
elif num2>num1:
    print(f"segundo número({num2}) maior que o primeiro({num1}).")
elif num1==num2:
    print("Os números são iguais.")
