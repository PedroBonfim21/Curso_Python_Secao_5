laboratorio=float(input("Digite a nota do trabalho de laboratorio: "))
semestral=float(input("Digite a nota da atividade semestral: "))
examefinal=float(input("Digite a nota do exame final: "))
media=(laboratorio*2)+(semestral*3)+(examefinal*5)/10
if media == 0 or media<=2.9:
    print("Você está reprovado.")
elif media == 3 or media<=4.9:
    print("Você está de recuperação.")
else:
    print("Parabéns você foi aprovado.")
    