# import math 
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))

# soma = n1 + n2

# print(f"A soma dos dois números é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# n = int(input("Digite um número: "))

# resto_dividao = n % 2

# n_final = resto_dividao * 5

# print(f"O número final é: {n_final}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))

# multiplicacao = n1 * n2

# print(f"O resultado final da multiplicação entre esses dois números é: {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# try:
#     numero_01 = int(input("Inserir umnumero inteiro: "))
#     numero_02 = int(input("Inserir outro numero inteiro: "))
#     resultado = numero_01 // numero_01
#     print(resultado)
# except:
#     print("Erro")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# n = int(input("Digite um número: "))
# quadrado = n ** 2

# print(f"O quadrado de {n} é {quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# n1 = float(input("Digite o primeiro número flutuante: "))
# n2 = float(input("Digite o segundo número flutuante: "))

# adicao = n1 + n2

# print(f"A adição desses dois números é: {adicao}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))

# media = (n1 + n2) / 2

# print(f"A média entre os dois valores é: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# espoente = float(input("Digite o espoente: "))

# potencia = (base ** espoente) * base

# print(f"A potência é: {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = celsius * 1.8 + 32

# print(f"A temperatura em celsius {celsius} convertida para fahrenheit é {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# palavra = str(input("Digite uma palavra: "))
# palavra_maiuscula = palavra.upper()
# print(f"A palavra {palavra} convertida para maiúscula é {palavra_maiuscula}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = str(input("Digite seu nome completo com todas as letras maiúsculas: "))
# nome_minusculo = nome.lower()
# print(f"O nome em minúsculo fica: {nome_minusculo}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = str(input("Digite uma frase: "))
# n_de_caracter_frase = len(frase)
# frase_nova = frase.strip()
# frase_nova_n_caracteres = len(frase_nova)
# print(f"O n° de caracteres da frase COM espaços é: {n_de_caracter_frase}")
# print(f"O n° de caracteres da frase SEM espaços é: {frase_nova_n_caracteres}")


# 14. Faça um programa que peça ao usuário para digitar um dado no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite a data no formato dd/mm/aaaa: ")
# lista_dat_mes_ano = data.split("/")
# print(f"O elemento 1 é o: {lista_dat_mes_ano[0]}")
# print(f"O elemento 2 é o: {lista_dat_mes_ano[1]}")
# print(f"O elemento 3 é o: {lista_dat_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# palavra_01 = str(input("Digite a primeira palavra: "))
# palavra_02 = str(input("Digite a segunda palavra: "))
# frase = palavra_01 + " " + palavra_02
# print(f"As palavras juntas ficam: {frase}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = True
# valor2 = False
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# valor_1 = True
# valor_2 = False
# resultado = valor_1 or valor_2
# print(f"O resultado é: {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# entrada = input("Digite um valor booleano: ").strip()
# if entrada.lower() == "true":
#     valor = True
# elif entrada.lower() == "false":
#     valor = False
# else:
#     print(f"Entrada inválida. Digite 'True' ou 'False'.")

# valor_invertido = not valor
# print(f"Valor invertido: {valor_invertido}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 != n2:
    print("Os números são diferentes")
else:
    print("Os números são iguais")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura

# 22: Verificador de Palíndromo

# 23: Calculadora Simples

# 24: Classificador de Números

# 25: Conversão de Tipo com Validação