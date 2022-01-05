num=int(input("Digite um número(entre 0 e 9999): "))
if num>0:
    u=num//1 %10
    d=num//10 %10
    c=num//100 %10
    m=num//1000 %10
    soma=m+c+d+u
    print(f"A soma dos números é igual a: {soma} ")
else:
    print("Número invalido")
