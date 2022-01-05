operação=int(input("Escolha uma das opções: \n(1)-Soma de dois números.\n(2)-Diferença entre dois números (maior pelo menor).\n(3)-Produto entre 2 números.\n(4)-Divisão entre dois números.\nDigite a opção(1,2,3 ou 4): "))
if operação==1:
    num1=float(input("Digite um número: "))
    num2=float(input("Digite um número: "))
    result=num1+num2
    print(result)
elif operação==2:
    num1=float(input("Digite um número: "))
    num2=float(input("Digite um número: "))
    if num1>num2:
        result= num1-num2
    elif num2>num1:
        result= num2-num1
    print(result)
elif operação==3:
    num1=float(input("Digite um número: "))
    num2=float(input("Digite um número: "))
    result=num1*num2
    print(result)
elif operação==4:
    num1=float(input("Digite o numerador: "))
    num2=float(input("Digite o denominador(diferente de 0): "))
    if num2<=0:
        print("Operação invalida, denominador = ou menor que 0 ")
    else:
        result=num1/num2
        print(result)
else:
    print("Operação invalida")
