nota1=float(input("Digite a 1ºnota: "))
nota2=float(input("Digite a 2ºnota: "))
media= (nota1+nota2)/2
if (nota1>=0) and (nota1<=10) and (nota2>=0) and (nota2<=10):
    print(f"A média das notas é: {media} ")
else:
    print("Nota inválida")
    