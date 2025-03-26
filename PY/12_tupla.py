# Tuplas em Python

alunos_tupla = ('João', 'Maria', 'José', 'Pedro',
                'Ana', 'Carlos', 'Joseane', 'Guilherme', 'Yasmin')  # Tuplas são imutáveis


print('==================================================================================================')
print(alunos_tupla)  # Imprime a lista de alunos
print(alunos_tupla[0])  # Imprime o primeiro elemento da tupla
print(alunos_tupla[1])  # Imprime o segundo elemento da tupla
print(alunos_tupla[:5])  # Imprime os 5 primeiros elementos da tupla
print(alunos_tupla[5:])  # Imprime os elementos da posição 5 até o final
print(alunos_tupla[2:5])  # Imprime os elementos da posição 2 até a 5
print('==================================================================================================')

# Pegar o indice de um elemento da tupla
print(alunos_tupla.index('Maria'))
print('==================================================================================================')

# alunos_tupla.append('Marta') # Não é possível adicionar mexer elementos em uma tupla
