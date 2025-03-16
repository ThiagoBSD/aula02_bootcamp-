import math 

numero_01 = int(input("Inserir umnumero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_01
print(resultado)

raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")