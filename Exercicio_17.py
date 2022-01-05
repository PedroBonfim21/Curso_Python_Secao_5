base_maior=float(input("Digite a base maior do trapézio: "))
base_menor=float(input("Digite a base menor do trapézio: "))
altura=float(input("Digite a altura do trapézio: "))
if base_maior==0 or base_menor==0:
    print("As bases devem ser maiores que 0")
else:
    area=((base_maior+base_menor)*altura)/2
    print(f"A área do trapézio é igual a: {area}")
