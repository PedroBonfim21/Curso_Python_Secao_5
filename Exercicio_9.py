salario=float(input("Digite o seu salário: "))
emprestimo=float(input("Digite a prestação do empréstimo: "))
parcela_max=salario*(20/100)
if salario<parcela_max:
    print("Empréstimo concedido.")
else:
    print("Empréstimo não concedido")
