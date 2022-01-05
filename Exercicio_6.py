num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
if num1>num2:
    diferença1=num1-num2
    print(f"O primeiro número ({num1}) é o maior")
    print(f"A diferença entre os números é de {diferença1} .")
else:
    diferença2=num2-num1
    print(f"O segundo número ({num2}) é o maior")
    print(f"A diferença entre os números é de {diferença2} .")
