dia=int(input("Digite um número (entre 1 e 7): "))
if dia== 1:
    print("domingo")
elif dia==2:
    print("segunda")
elif dia==3:
    print("terça")
elif dia==4:
    print("quarta")
elif dia==5:
    print("quinta")
elif dia==6:
    print("sexta")
elif dia==7:
    print("sábado")
elif dia<1 or dia>7:
    print("Dia inexistente")
