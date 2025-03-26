# Operadores em Python

print("================================================================")
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

somar = numero1 + numero2
subtrair = numero1 - numero2
multiplicar = numero1 * numero2
dividir = numero1 / numero2
dividir_inteiro = numero1 // numero2
resto = numero1 % numero2
potencia = numero1 ** numero2
maior = numero1 > numero2
menor = numero1 < numero2
igual = numero1 == numero2
diferente = numero1 != numero2
maior_ou_igual = numero1 >= numero2
menor_ou_igual = numero1 <= numero2


print("================================================================")
print(f'Soma: {somar}')
print(f'Subtração: {subtrair}')
print(f'Multiplicação: {multiplicar}')
print(f'Divisão: {dividir}')
print(f'Divisão inteira: {dividir_inteiro}')
print(f'Resto da divisão de {numero1} por {numero2} é: {resto}')
print(f'Potência do numero {numero1} por {numero2} é: {potencia}')
print(f'O numero {numero1} é maior que o numero {numero2}? {maior}')
print(f'O numero {numero1} é menor que o numero {numero2}? {menor}')
print(f'O numero {numero1} é igual ao numero {numero2}? {igual}')
print(f'O numero {numero1} é diferente do numero {numero2}? {diferente}')
print(f'O numero {numero1} é maior que {numero2}? {maior_ou_igual}')
print(f'O numero {numero1} é menor ou igual a {numero2}? {menor_ou_igual}')
print("================================================================")
