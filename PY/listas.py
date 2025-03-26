# Listas em Python

nome = 'João'
idade = 25
altura = 1.75


lista_de_alunos = ['João', 'Maria', 'José', 'Pedro', 'Ana',
                   'Paula', 'Carlos', 'Mariana', 'Felipe', 'Miguel']
lista_de_alunos2 = ['João', 25, 1.75]  # Lista com tipos diferentes
lsita_de_alunos3 = [nome, idade, altura]  # Lista com variáveis

print('==================================================================================================')
print(lista_de_alunos)  # Imprime a lista de alunos
print(lista_de_alunos[0])  # Imprime o primeiro elemento da lista
print(lista_de_alunos[1])  # Imprime o segundo elemento da lista
print(lista_de_alunos[:5])  # Imprime os 5 primeiros elementos da lista
print(lista_de_alunos[5:])  # Imprime os elementos da posição 5 até o final
print(lista_de_alunos[2:5])  # Imprime os elementos da posição 2 até a 5

# Adicionando um elemento na lista
lista_de_alunos.append('Marta')
print(lista_de_alunos)

# Removendo um elemento da lista
lista_de_alunos.remove('Marta')
print(lista_de_alunos)

# Adicionando um elemento na lista em uma posição específica
lista_de_alunos.insert(6, 'Marta')

# Removendo um elemento da lista em uma posição específica
lista_de_alunos.pop(0)

# Verificando se um elemento está na lista
if 'Marta' in lista_de_alunos:
    print('Marta está na lista')

# Verificando o tamanho da lista
print(len(lista_de_alunos))  # Imprime o tamanho da lista

# Ordenando a lista
lista_de_alunos.sort()
print(lista_de_alunos)

# Invertendo a lista
lista_de_alunos.reverse()
print(lista_de_alunos)

# remove todos os elementos da lista
lista_de_alunos.clear()

print('==================================================================================================')
