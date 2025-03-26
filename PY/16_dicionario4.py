# Continuano Dicionário no Python

# Dicionário dentro de Dicionário
lista_de_alunos = {
    'Matheus': {
        'idade': 25,
        'altura': 1.75,
        'peso': 80,
        'sexo': ('Masculino', 'Feminino', 'Outros'),
    },
    'Carlos': {
        'idade': 45,
        'altura': 1.98,
        'peso': 115,
        'sexo': ('Masculino', 'Feminino', 'Outros'),
    },
}

print('==================================================================================================')
print(lista_de_alunos)
print('==================================================================================================')

print(lista_de_alunos['Matheus']['idade'])
print('==================================================================================================')

# Adicionando um novo elemento no Dicionário
lista_de_alunos['Matheus']['cor_dos_olhos'] = 'Castanho'
print(lista_de_alunos)
print('==================================================================================================')

# Removendo um elemento do Dicionário
del lista_de_alunos['Matheus']['cor_dos_olhos']
lista_de_alunos['Matheus'].pop('sexo')
print(lista_de_alunos)
print('==================================================================================================')
