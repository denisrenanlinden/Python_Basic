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

print("================================================================")
print(f'Soma: {somar}')
print(f'Subtração: {subtrair}')
print(f'Multiplicação: {multiplicar}')
print(f'Divisão: {dividir}')
print(f'Divisão inteira: {dividir_inteiro}')
print(f'Resto da divisão de {numero1} por {numero2} é: {resto}')
print(f'Potência do numero {numero1} por {numero2} é: {potencia}')
print("================================================================")
