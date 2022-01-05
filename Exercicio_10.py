sexo=str(input("Digite o sexo(masculino ou feminino): "))
altura=float(input("Digite a altura: "))
sexo=sexo.title()

if sexo == "Masculino" :
    homens=(72.7*altura)-58
    print(f"O peso ideal é: {homens} ")
elif sexo=="Feminino":
    mulheres=(62.1*altura)-44.7
    print(f"O peso ideal é: {mulheres} ")
    