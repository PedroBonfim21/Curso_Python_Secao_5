a = int(input("Digite o lado A de um triangulo: "))
b = int(input("Digite o lado B de um triangulo: "))
c = int(input("Digite o lado C de um triangulo: "))
if b + c < a or a + c < b or a + b < c:
    print("Incopativel. A soma de dois lados é inferior ao valor do terceiro. ")
elif a == b == c:
    print("O triangulo é equilatero")
elif a == b != c or a == c != b or c == b != a:
    print("O triangulo é isosceles")
elif a!=b!=c:
    print("O triangulo é escaleno")
    