idade=float(input("Digite sua idade: "))
tempo=float(input("Digite seu tempo de trabalho: "))
if idade>=65 or tempo>=30 or idade>=60 and tempo>=20:
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar ainda.")
