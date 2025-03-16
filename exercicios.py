# import math 

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_01 = int(input("Inserir umnumero inteiro: "))
# numero_02 = int(input("Inserir outro numero inteiro: "))
# resultado = numero_01 // numero_01
# print(resultado)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")

# 14. Faça um programa que peça ao usuário para digitar um dado no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite a data no formato dd/mm/aaaa: ")
lista_dat_mes_ano = data.split("/")
print(f"O elemento 1 é o: {lista_dat_mes_ano[0]}")
print(f"O elemento 2 é o: {lista_dat_mes_ano[1]}")
print(f"O elemento 3 é o: {lista_dat_mes_ano[2]}")